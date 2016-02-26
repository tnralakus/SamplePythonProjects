__author__ = 'alakus'

import winsound, time, os, platform


def sound():
    for i in range(2):  # Number of repeats
        for j in range(9):  # Number of beeps
            winsound.Beep(10000, 200)
        time.sleep(2)  # How long between beeps

def alarm(n):
    print('Wait time:', n, 'seconds.')
    time.sleep(n)  # Waits 'n' seconds before playing sound
    sound()

def input_destinations(user_input):
    options = {'1' : hour,
               '2' : min,
               '3' : sec,
               '4' : comb
               }
    if user_input in options.keys():
        wait_seconds=options[user_input]()
        alarm(wait_seconds)
    else:
        main()


def hour():
    user_input = int(raw_input("Enter the desired hours: "))
    return (user_input * 60) * 60

def min():
    user_input = int(raw_input("Enter the desired minutes: "))
    return user_input * 60

def sec():
    user_input = int(raw_input("Enter the desired seconds: "))
    return user_input

def comb():
    hours = int(raw_input("Hours: "))
    minutes = int(raw_input("Minutes: "))
    seconds = int(raw_input("Seconds: "))
    return ((hours * 60) * 60) + (minutes * 60) + seconds

def main():
    main_input = raw_input("What unit of time do you want to wait?\n (1) Hours\n (2) Minutes\n (3) Seconds\n (4) Combination : ")
    input_destinations(main_input)
    return

if __name__ == '__main__':
    main()