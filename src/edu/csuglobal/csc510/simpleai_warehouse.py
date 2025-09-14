#!/usr/bin/env python3

from simpleai.search import SearchProblem, astar
import sys

"""
Legend:
    #  = wall (impassable)
    .  = normal floor (cost = 1)
    ~  = rough terrain (cost = 3)
    S  = start position
    G  = goal position
"""

MAPS = {
    "A": [
        list("###############"),
        list("#S....#....~G#"),
        list("#.##..#..##..#"),
        list("#....##.....##"),
        list("###..#..###..#"),
        list("#....#.....~.#"),
        list("#..####..##..#"),
        list("#..~....#....#"),
        list("##############"),
    ],
    "B": [
        list("####################"),
        list("#S.....#........~G#"),
        list("#.###..#.######...#"),
        list("#...#..#....~..#..#"),
        list("###.#..#######.#..#"),
        list("#...#........#.#..#"),
        list("#.~.########.#.#..#"),
        list("#...#......~.#.#..#"),
        list("##############.#..#"),
        list("#................##"),
        list("###################"),
    ],
}

# Moves
DIRS = [
    (-1, 0, "UP"),
    (1, 0, "DOWN"),
    (0, -1, "LEFT"),
    (0, 1, "RIGHT"),
]


def in_bounds(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


def tile_cost(ch):
    # '.' normal floor cost 1
    # '~' rough terrain cost 3
    # 'S' and 'G' treated like '.' (cost 1)
    if ch == "~":
        return 3
    return 1


def find_positions(grid):
    start = goal = None
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "S":
                start = (r, c)
            elif grid[r][c] == "G":
                goal = (r, c)
    return start, goal

def normalize_grid(grid):
    """Pad shorter rows with walls so all rows have equal length."""
    maxw = max(len(row) for row in grid)
    for row in grid:
        if len(row) < maxw:
            row.extend(['#'] * (maxw - len(row)))
    return grid



class WarehouseProblem(SearchProblem):

    def __init__(self, grid, initial_state, goal):
        self.grid = grid
        self.goal_pos = goal
        self.expanded = 0
        super().__init__(initial_state=initial_state)

    def actions(self, state):
        self.expanded += 1
        r, c = state
        acts = []
        for dr, dc, name in DIRS:
            nr, nc = r + dr, c + dc
            if in_bounds(self.grid, nr, nc) and self.grid[nr][nc] != "#":
                acts.append(name)
        return acts

    def result(self, state, action):
        r, c = state
        for dr, dc, name in DIRS:
            if name == action:
                nr, nc = r + dr, c + dc
                return (nr, nc)
        return state

    def is_goal(self, state):
        return state == self.goal_pos

    def cost(self, state, action, state2):
        r2, c2 = state2
        ch = self.grid[r2][c2]
        return tile_cost(ch)

    def heuristic(self, state):
        r, c = state
        gr, gc = self.goal_pos
        return abs(r - gr) + abs(c - gc)


def grid_to_str(grid):
    return "\n".join("".join(row) for row in grid)


def annotate_path(grid, path_states, start, goal):
    g2 = [row[:] for row in grid]
    for (r, c) in path_states:
        if (r, c) != start and (r, c) != goal:
            g2[r][c] = "*"
    return g2


def prompt_yes_no(msg, default="y"):
    while True:
        ans = input(f"{msg} [{'Y/n' if default=='y' else 'y/N'}]: ").strip().lower()
        if ans == "" and default:
            return default == "y"
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("Please answer y or n.")


def read_coord(grid, name):
    while True:
        try:
            raw = input(f"Enter {name} as 'row,col' (0-indexed): ").strip()
            r, c = map(int, raw.split(","))
            if not in_bounds(grid, r, c):
                print("Out of bounds. Try again.")
                continue
            if grid[r][c] == "#":
                print("Cannot place on a wall. Try again.")
                continue
            return (r, c)
        except Exception:
            print("Invalid format. Try again (e.g., 1,3).")


def main():
    print("=== Warehouse Robot Pathfinding with SimpleAI (A* Search) ===")
    print("Legend: '#' wall, '.' floor(cost=1), '~' rough(cost=3), 'S' start, 'G' goal\n")

    choice = None
    while choice not in MAPS:
        print("Choose a map:")
        for k in MAPS:
            dims = (len(MAPS[k]), len(MAPS[k][0]))
            print(f"  {k}) {dims[0]}x{dims[1]}")
        choice = input("Enter map key (A/B): ").strip().upper()
        if choice not in MAPS:
            print("Invalid choice.")

    grid = [row[:] for row in MAPS[choice]]
    grid = normalize_grid(grid)
    start, goal = find_positions(grid)

    if start is None or goal is None:
        print("Map must contain S (start) and G (goal). Exiting.")
        sys.exit(1)

    print("\nSelected map:\n")
    print(grid_to_str(grid), "\n")

    if prompt_yes_no("Do you want to move S and G to custom coordinates?", default="n"):
        sr, sc = start
        gr, gc = goal
        grid[sr][sc] = "."
        grid[gr][gc] = "."
        start = read_coord(grid, "START")
        goal = read_coord(grid, "GOAL")
        grid[start[0]][start[1]] = "S"
        grid[goal[0]][goal[1]] = "G"
        print("\nUpdated map:\n")
        print(grid_to_str(grid), "\n")

    # Build and solve the SimpleAI problem with A*
    problem = WarehouseProblem(grid=grid, initial_state=start, goal=goal)
    print("Running A* (SimpleAI) with Manhattan heuristic...")
    result = astar(problem, graph_search=True)
    if result is None:
        print("\nNo path found. Try moving S/G or tweak walls (~/#).")
        return

    path = result.path()
    ordered_states = [step[1] for step in path]
    actions = [step[0] for step in path if step[0] is not None]

    annotated = annotate_path(grid, ordered_states, start, goal)

    print("\n=== RESULTS ===")
    print(f"Path cost:      {result.cost}")
    print(f"Expanded nodes: {problem.expanded}")
    print(f"Path length:    {len(ordered_states) - 1} steps")
    print(f"Actions:        {', '.join(actions) if actions else '(none)'}")
    print("\nPath on map (*):\n")
    print(grid_to_str(annotated))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted.")
