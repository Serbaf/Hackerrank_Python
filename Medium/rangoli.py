#!/usr/bin/env python3

def build_rangoli(size):
        # Calculate and initialize the necessary variables
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
        rows = (size * 2) - 1
        columns = ((size + (size - 1)) * 2) - 1
        reduced_alph = alphabet[:size]
        central_row = rows // 2
        
        for row in range(0, central_row + 1):
                first_letter = ((columns // 2) + 1 - (2 * row)) - 1
                last_letter = ((columns // 2) + 1 + (2 * row)) - 1
                for column in range(0, first_letter): 
                        print("-", end="")
                counter = len(reduced_alph) - 1
                for column in range(first_letter, last_letter+1):
                        if (column % 2) == 0:
                                print(reduced_alph[counter], end="")
                                if (column < columns//2):
                                        counter -= 1
                                else:
                                        counter += 1
                        else:
                                print("-", end="")
                for column in range(last_letter + 1, columns):
                        print("-", end="")
                print()

        bottom_lines = list(range(0, (rows - central_row) - 1))
        bottom_lines.reverse()

        for row in bottom_lines:
                first_letter = ((columns // 2) + 1 - (2 * row)) - 1
                last_letter = ((columns // 2) + 1 + (2 * row)) - 1
                for column in range(0, first_letter): 
                        print("-", end="")
                counter = len(reduced_alph) - 1
                for column in range(first_letter, last_letter+1):
                        if (column % 2) == 0:
                                print(reduced_alph[counter], end="")
                                if (column < columns // 2):
                                        counter -= 1
                                else:
                                        counter += 1
                        else:
                                print("-", end="")
                for column in range(last_letter + 1, columns):
                        print("-", end="")
                print()

n = int(input("Please enter the size of the Rangoli (1-26): "))
build_rangoli(n)
