#!/usr/bin/python3

#
# File:         main.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         12-Aug-2021
# Description:  Runs the pre-defined functions and time how long each
#               function takes to execute.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#

# ------------------------------- Module Imports ------------------------------
"""
The time module has a function called time which is able to perform the timing.
The check-prime-functions module comprises 3 functions to measure.
"""

from time import time

import prime_checker_functions as func


# ------------------------------- Main Function -------------------------------
def main() -> None:
    print(
        "A program to check if a number is prime.",
        "Return True if it is, False otherwise.",
        "Also compares which function is the fastest.",
        sep="\n",
    )

    try:
        user_input = input("\nEnter a number for evaluation: ")
        n = int(user_input)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    except EOFError:
        return

    func.line()

    # function_a
    t0 = time()
    print(f"{n:,} is {func.is_prime_a(n)}")
    func.prime_lessthan(func.is_prime_a)
    t1 = time()
    print(f"Function A: time taken = {round(t1 - t0, 4)} seconds.")

    func.line()

    # function_b
    t2 = time()
    print(f"{n:,} is {func.is_prime_b(n)}")
    func.prime_lessthan(func.is_prime_b)
    t3 = time()
    print(f"Function B: time taken = {round(t3 - t2, 4)} seconds.")

    func.line()

    # function_c
    t4 = time()
    print(f"{n:,} is {func.is_prime_c(n)}")
    func.prime_lessthan(func.is_prime_c)
    t5 = time()
    print(f"Function C: time taken = {round(t5 - t4, 4)} seconds.")


# --------------------------- Call the Main Function --------------------------
if __name__ == "__main__":
    main()
