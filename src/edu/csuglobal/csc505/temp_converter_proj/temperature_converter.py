def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    print("Temperature Converter")
    print("1: Convert Celsius to Fahrenheit")
    print("2: Convert Fahrenheit to Celsius")

    try:
        choice = int(input("Enter your choice (1 or 2): "))
        if choice == 1:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F")
        elif choice == 2:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit:.2f}°F is equal to {celsius:.2f}°C")
        else:
            print("Invalid choice. Please select either 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter numerical values only.")


if __name__ == "__main__":
    main()
