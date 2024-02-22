import math
import os

critical_values = (
    math.nan,   # 0
    3.841,      # 1
    5.991,      # 2...
    7.815,
    9.488,
    11.070,
    12.592,
    14.067,
    15.507,
    16.919,
    18.307,
    19.675,
    21.026,
    22.362,
    23.685,
    24.996      # 15
)

def chi_square(observed, expected, degrees_freedom, num_places):
    chi = ((observed - expected) ** 2) / expected
    print("--------------------------")
    print("Observed - Expected      : " + str(round(observed - expected, num_places)))
    print("(Observed - Expected)^2  : " + str(round((observed - expected)**2, num_places)))
    print("Chi-square value         : " + str(round(chi, num_places)))
    print("Critical value           : " + str(critical_values[degrees_freedom]))
    if (chi <= critical_values[degrees_freedom]):
        print("Accept null hypothesis.")
    else:
        print("Reject null hypothesis.")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    observed = float(input("Enter the observed: "))
    expected = float(input("Enter the expected: "))
    while True:
        try:
            degrees_freedom = int(input("Enter the number of options: ")) - 1
            if degrees_freedom < 0 or degrees_freedom >= len(critical_values):
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer between 2 and " + str(len(critical_values) - 1))

    num_places_str = input("Round to how many decimal places? ")
    if num_places_str.strip() == "":
        print("Rounding to 3 decimal places.\n")
        num_places = 3
    else:
        num_places = int(num_places_str)
        if num_places < 0:
            num_places = -num_places
            print("Rounding to " + str(num_places) + " decimal places.")
    chi_square(observed, expected, degrees_freedom, num_places)

if __name__ == "__main__":
    main()
