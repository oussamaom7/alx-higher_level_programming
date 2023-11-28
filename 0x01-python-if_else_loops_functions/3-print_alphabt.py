#!/usr/bin/env python3

# Print the ASCII alphabet in lowercase excluding 'q' and 'e' without a new line
for i in range(ord('a'), ord('z') + 1):
    if chr(i) not in ['q', 'e']:
        print(chr(i), end='')

# Print a new line after the loop
print()

