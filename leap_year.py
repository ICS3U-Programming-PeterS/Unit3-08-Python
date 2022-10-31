#!/usr/bin/env python3

# Created By: Peter Sobowale
# Date: October 26, 2022
# This program asks the user to enter a year and it tells the user if it is a leap year.
import math


def main():
    # Get the year as a string
    year_as_a_string = input("Please enter a year: ")

    # try catch to make sure year is an integer
    try:

        # convert year_as_a_string into year
        year = int(year_as_a_string)

        # if year mod 4 is equal to 0
        if year % 4 == 0:

            # if year mod 100 is equal to 0
            if year % 100 == 0:

                # if year mod 400 is equal to 400
                if year % 400 == 0:
                    print(str(year) + " is definitely a leap year!")
                else:
                    print(str(year) + " is not a leap year.")
            else:
                print(str(year) + " is definitely a leap year!")
        else:
            print(str(year) + " is not a leap year.")
    except ValueError:
        print("Invalid input!")
    finally:
        # print final message
        print("\nDone.")


if __name__ == "__main__":
    main()
