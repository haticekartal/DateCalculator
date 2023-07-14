import datetime
import sys

# (year, month, day, hour, minute, second)
# Provide the dates and times in the format: year, month, day, hour, minute, second
try:
    a = datetime.datetime(2015, 555, 28, 0, 0, 0)
except Exception as e:
    print(" a icin gecerli tarih girin",e)
    sys.exit(1) #0 ve 1

try:
    b = datetime.datetime(2020, 3, 1, 0, 0, 89)

except:
    print(" b icin gecerli tarih girin")
    sys.exit(1) #0 ve 1



try:

    # Calculate the time difference
    c = a - b
    print('Difference: ', c)

    # Ensure the difference is non-negative
    if c.total_seconds() < 0:
        raise ValueError('Invalid input: Second date is earlier than the first date.Please change it.')

    if a.month > 12 or a.day > 30 or a.hour > 23 or a.minute or a.second > 59:
        raise ValueError('Invalid input: Difference exceeds the limits.')
    elif b.month > 12 or b.day > 30 or b.hour > 23 or b.minute or b.second > 59:
        raise ValueError('Invalid input: Difference exceeds the limits.')


    # Function to calculate the number of years, months, and days
    def number_of_years_months_days(number_of_days):
        years = number_of_days // 365
        number_of_days %= 365
        months = number_of_days // 30
        days = number_of_days % 30
        return years, months, days


    difference_in_days = c.days
    years, months, days = number_of_years_months_days(difference_in_days)

    print(
        "Difference: {} day, also equal to: {} year, {} month, {} day".format(difference_in_days, years, months, days))

    # Calculate the total difference in minutes
    minutes = c.total_seconds() / 60
    print('Total difference in minutes: ', minutes)

    # Calculate the difference in hours
    hours = c.total_seconds() / 3600
    print('Difference in hours: ', hours)

except ValueError as e:
    print(e)



