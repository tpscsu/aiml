import math


def calculate_circle():
    try:
        radius = float(input("Enter the radius of the circle: "))
        if radius < 0:
            print("Invalid Input , radius cannot be negative.")
            return

        circle_area = math.pi * radius ** 2
        circle_circ = 2 * math.pi * radius

        print(f"Area of the circle: {circle_area: .2f}")
        print(f"Circumference of the circle: {circle_circ: .2f}")
    except ValueError:
        print("Invalid input.Expecting a numerical value.")


if __name__ == "__main__":
    calculate_circle()
