from collatz import get_data
import matplotlib.pyplot as plt
import numpy as np

def main():
    """Plot Collatz Path Lengths for Integers 1 to 1,000,000 """

    n, paths = get_data()
    p_mean = np.mean(paths)
    p_std = np.std(paths)
    
    plt.figure(figsize=(12, 6))
    plt.scatter(n,  paths, color="blue", s=3, alpha=1, label="Path Lengths")
    plt.axhline(p_mean, color="red", linestyle="-", label=f"Mean = {p_mean:.2f}")
    plt.axhline(p_mean + p_std, color="green", linestyle="--", label=f" + 1 SD: {p_mean + p_std:.2f}")
    plt.axhline(p_mean - p_std, color="green", linestyle="--", label=f" - 1 SD: {p_mean - p_std:.2f}")
    
    plt.title("Collatz Path Lengths for Integers 1 to 1,000,000")
    plt.xlabel("Integers n 1 to 1,000,000")
    plt.ylabel("Path Lengths")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("plots/L_plot.png")
    plt.show()

if __name__ == "__main__":
    main()
