__author__ = 'dwight'

# Write a program that asks the user to enter a number of seconds, and works as follows:
# • There are 60 seconds in a minute. If the number of seconds entered by the user is greater than or equal to 60, the
#   program should display the number of minutes in that many seconds.
# • There are 3,600 seconds in an hour. If the number of seconds entered by the user is greater than or equal to 3,600,
#   the program should display the number of hours in that many seconds.
# • There are 86,400 seconds in a day. If the number of seconds entered by the user is greater than or equal to 86,400,
#   the program should display the number of days in that many seconds.


SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600
SECONDS_IN_DAY = 86400


def main():
    seconds = int(input('Enter number of seconds: '))

    if seconds >= SECONDS_IN_MINUTE:
        print('There are', calc_minutes(seconds), 'minutes in', seconds, 'seconds.')
    if seconds >= SECONDS_IN_HOUR:
        print('There are', calc_hours(seconds), 'hours in', seconds, 'seconds.')
    if seconds >= SECONDS_IN_DAY:
        print('There are', calc_days(seconds), 'days in', seconds, 'seconds.')


def calc_minutes(seconds):
    return int(seconds / SECONDS_IN_MINUTE)


def calc_hours(seconds):
    return int(seconds / SECONDS_IN_HOUR)


def calc_days(seconds):
    return int(seconds / SECONDS_IN_DAY)


main()