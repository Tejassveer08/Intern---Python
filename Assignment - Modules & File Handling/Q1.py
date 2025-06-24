import numpy as np

def solve_polynomial(coefficients): # Function to solve a polynomial equation
    try:
        roots = np.roots(coefficients) # Find the roots of the polynomial
        print("Roots of the polynomial:", roots) # Print the roots
    except Exception as e: # Handle any exceptions that may occur
        print("Error solving polynomial:", e) # Print any error that occurs

# Example: Solve x^3 - 6x^2 + 11x - 6 = 0
solve_polynomial([1, -6, 11, -6]) # This will output the roots of the polynomial equation.
