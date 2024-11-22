from collatz import get_data
import matplotlib.pyplot as plt

def main():
    """Plot a Modified Collatz Path Lengths for Integers 1 to 1,000,000 """

    n, paths, group = get_data("modified")
    colors = ["blue" if g == "blue" else "red" for g in group]

    plt.figure(figsize=(12, 6))
    plt.scatter(n, paths, color=colors, s=3, alpha=1, label="Path Lengths")
    plt.title("Collatz Path Lengths for Integers 1 to 1,000,000")
    plt.xlabel("Integers n 1 to 1,000,000")
    plt.ylabel("Path Lengths")
    plt.legend(["Blue Group", "Red Group"])
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("plots/N_plot.png")
    plt.show()

if __name__ == "__main__":
    main()
