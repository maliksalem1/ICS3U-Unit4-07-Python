#!/usr/bin/env python3
# Created by: Kyanh Pham
# Created on: Oct 2022
# This program uses loops in if statements
#  and vice versa


def main():

    counter = 0

    # Process and Output
    for counter in range(1000, 2001):
        if counter % 5 == 0:
            print("")
            print(counter, end=" ")
        else:
            print("{0} ".format(counter), end="")

    print("\nDone.")


if __name__ == "__main__":
    main()
