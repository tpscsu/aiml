def calculate_rainfall():
    years = int(input('Enter the number of years : '))

    month_map = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    total_rainfall = 0
    total_months = 0

    for year in range(1, years + 1):

        for month in range(1, 13):
            rainfall = float(
                input('Enter the inches of rainfall for year {} in the month of {} : '.format(year, month_map[month])))
            total_rainfall += rainfall
            total_months += 1

    average_rainfall = total_rainfall / total_months
    print(f"\nTotal number of months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f}")
    print(f"Average rainfall per month: {average_rainfall:.2f}")


calculate_rainfall()