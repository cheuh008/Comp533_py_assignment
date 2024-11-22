# =======================================================================================================================================
# What is the Collatz Conjecture?
# =======================================================================================================================================
# The Collatz conjecture is a mathematical sequence defined as follows for any integer 𝑛:
    # If 𝑛 is even, divide it by 2: n = n/2
    # If 𝑛 is odd, multiply it by 3 and add 1: n=3n+1.
    # If 𝑛 = 1, stop.

# The "path length" of a nber is the count of steps required to reach 1. For example:
    # For n=1, path length = 0.
    # For 𝑛 =2, path = 2 → 1, path length = 1.
    # For 𝑛 = 5, path = 5 → 16 → 8 → 4 → 2 → 1, path length = 5.
# =======================================================================================================================================

# Recursion Error for n > 1000
# def collatz(n, path=0):
#     if n == 1:
#         return path
#     elif n % 2 == 0:
#         return collatz(n // 2, path + 1)
#     else:
#         return collatz(3 * n + 1, path + 1)

import pandas as pd
import os

def collatz(n, path=0):
    """ Compute the path length for n in the Collatz sequence """
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        path += 1
    return path

def modified(n, visited=None, path = 0):
    """ Computes the path length for n in a modified Collatz sequence """
    visited = visited or set()  # if Visited is empty(none), creates a new set
    while n != 1:               # Iterates until n = 1 (and the sequence is finished)
        if n in visited:        # Checks to see if we have started looping by storing n
            return path, "red"  # returns the path length up to the loop as re group
        visited.add(n)          # if its not a loop, add this particular n to a set to be checked
        if n % 2 == 0:          # if even
            n //= 2             # divide by 2 
        else:                   # else (if odd)
            n = 3 * n - 1       # use modified rule 2 
        path += 1               # add 1 to the path length
    return path, "blue"         # returns path length if n is 1, in group blue

def path_finder(type, n):
    """ Compute, saves and returns Collatz sequence data as np array"""
    filename = f"data/{type}_{n}path.csv"
    if os.path.exists(filename):
        print(f"Loading precomputed data from {filename}...")
        data = pd.read_csv(filename)
    else:
        print(f"Computing {type} sequence lengths for n = 1 to {n}...")
        if type == "collatz":
            paths = [collatz(i) for i in range(1, n + 1)]
            data = pd.DataFrame({"n": range(1, n + 1), "paths": paths})
        elif type == "modified":
            paths, group = zip(*[modified(i) for i in range(1, n + 1)])
            data = pd.DataFrame({"n": range(1, n + 1), "paths": paths, "group":group})
        data.to_csv(filename, index=False)
        print(f"Data saved to {filename}.")
    return data

def get_data(type="collatz", n = 1_000_000):
    """Unpack DataFrame columns based on type."""
    data = path_finder(type, n)
    if type == "modified":
        return data["n"].to_numpy(), data["paths"].to_numpy(), data["group"].to_numpy()
    return data["n"].to_numpy(), data["paths"].to_numpy()


if __name__ == "__main__":
    collatz_data = path_finder(n=1_000_000, type="collatz")
    modified_data = path_finder(n=1_000_000, type="modified")
