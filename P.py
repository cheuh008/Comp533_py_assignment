from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from random import random

def probs(n, p, path=0):
    """Compute the path length for n in the probabilistic Collatz sequence."""
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            if random() < p:
                n = 3 * n + 1
            else:
                n = 3 * n - 1
        path += 1
    return path

def path_finder(n, p, instance):
    """Compute, save, and return probabilistic Collatz sequence data."""
    filename = f"data/P_{p}_{instance}_path.csv"
    if os.path.exists(filename):
        print(f"Loading precomputed data from {filename}...")
        data = pd.read_csv(filename)
    else:
        print(f"Computing Probability Collatz sequence lengths for n = 1 to {n} with p = {p}...")
        paths = [probs(i, p=p) for i in range(1, n + 1)]
        data = pd.DataFrame({"n": range(1, n + 1), "paths": paths})
        data.to_csv(filename, index=False)
        print(f"Data saved to {filename}.")
    return data

def plot_multiplicity(data, p, instance):
    """Plot multiplicity (frequency) of path lengths."""
    counts = Counter(data["paths"])
    unique_lengths = np.array(list(counts.keys()))
    frequencies = np.array(list(counts.values()))
    mean_fq = np.mean(frequencies)
    std_fq = np.std(frequencies)

    plt.figure(figsize=(12, 6))
    plt.scatter(unique_lengths, frequencies, color="red", s=5, alpha=0.7, label="Frequencies")
    plt.axhline(mean_fq, color="red", linestyle="--", label=f"Mean = {mean_fq:.2f}")
    plt.axhline(mean_fq + std_fq, color="green", linestyle="--", label=f" + 1 SD: {mean_fq + std_fq:.2f}")
    plt.axhline(mean_fq - std_fq, color="green", linestyle="--", label=f" - 1 SD: {mean_fq - std_fq:.2f}")

    plt.title(f"Multiplicity of Collatz Path Lengths (p = {p}, Instance {instance})")
    plt.xlabel("Path Lengths")
    plt.ylabel("Frequency (Multiplicity)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plot = f"plots/P_{p}_{instance}_plot.png"
    plt.savefig(plot)
    plt.show()
    print(f"Plot saved to {plot}")

def main():
    n = 1_000_000
    probabilities = [0.25, 0.5, 0.75]
    instances = 6

    for p in probabilities:
        for instance in range(4, instances + 1):
            data = path_finder(n, p, instance)
            plot_multiplicity(data, p, instance)

if __name__ == "__main__":
    main()
