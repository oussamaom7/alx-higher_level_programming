#!/usr/bin/python3
 def print_last_digit(number):
    # Take the absolute value to handle negative numbers
    last_digit = abs(number) % 10
    print(last_digit, end='')

    return last_digit

