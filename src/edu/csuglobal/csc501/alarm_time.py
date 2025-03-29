#
# The program takes two inputs 1. Current time in hours , 2. Wait time till the alarm goes off in hours
# Prints the hour in 24 hours at which the alarm goes off
#
#

try:
    current_time = int(input('Enter the current time in hours (0-23) : '))
    if current_time < 0 or current_time > 23:
        print('Invalid input. Expected numeric value between 0 - 23')
        exit()

    hours_to_alarm = int(input('Enter the wait time before alarm goes off : '))

    alarm_time = (current_time + hours_to_alarm) % 24

    print("The alarm will go off at {} hours.".format(alarm_time))

except ValueError:
    print('Invalid input. Expected numeric value')
    exit()
