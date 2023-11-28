#!/usr/bin/python3
def uppercase(s):
    for  char in s:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert the character to uppercase using ASCII values
            print(chr(ord(char) - ord('a') + ord('A')), end='')
        else:
        
            print(char, end='')
    print()
