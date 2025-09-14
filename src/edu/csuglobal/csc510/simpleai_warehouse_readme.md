# Warehouse Robot Pathfinding – Testing Instructions

This program finds the least-cost path for a warehouse robot from a start point (S) to a goal (G) on a grid using the A* search algorithm from the SimpleAI library.

## Legend
#  = wall (impassable)
.  = floor (cost = 1)
~  = rough terrain (cost = 3)
S  = start position
G  = goal position

## 1. Install dependencies
Make sure Python 3 is installed, then install SimpleAI:
pip install simpleai

## 2. Run the program
python3 simpleai_warehouse.py

## 3. Choose a map
- A → Smaller 9×15 map
- B → Larger 11×20 map

Type A or B and press Enter.

## 4. (Optional) Move S and G
You will be asked if you want to change the start (S) and goal (G) positions.
- Type y to set custom coordinates (row,col)
- Type n to keep the default positions

## 5. View results
The program will display:
- Path cost
- Expanded nodes
- Path length (steps)
- Action list (UP/DOWN/LEFT/RIGHT)
- Map with the path marked as *

## 6. Test variations
Try running it with both maps and changing S and G to see how the path changes.
