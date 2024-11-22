from collatz import get_data
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

def main():
    """Plot multiplicity (frequency) of path lengths."""
    n, paths = get_data()

    counts = Counter(paths)
    unique_lengths = np.array(list(counts.keys()))
    frequencies = np.array(list(counts.values()))
    mean_fq = np.mean(frequencies)
    std_fq = np.std(frequencies)

    plt.figure(figsize=(12, 6))
    plt.scatter(unique_lengths, frequencies, color="red", s=5, alpha=0.7, label="Frequencies")
    plt.axhline(mean_fq, color="red", linestyle="--", label=f"Mean = {mean_fq:.2f}")
    plt.axhline(mean_fq + std_fq, color="green", linestyle="--", label=f" + 1 SD: {mean_fq + std_fq:.2f}")
    plt.axhline(mean_fq - std_fq, color="green", linestyle="--", label=f" - 1 SD: {mean_fq - std_fq:.2f}")
    
    plt.title("Multiplicity of Collatz Path Lengths")
    plt.xlabel("Path Lengths")
    plt.ylabel("Frequency (Multiplicity)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("plots/M_plot.png")
    plt.show()

if __name__ == "__main__":
    main()
