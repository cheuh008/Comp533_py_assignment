## Task 4: Changes in distribution with varying \( p \)

### Overview

- Runing multiple instances of P.py for varying values p \(0.25, 0.5, 0.75\)
- The shape of the multiplicity distribution appears similar across different \( p \) values.

- no obvious changes in multiplicity were observed but subtle changes can be noted and infered.
- Differences become noticeable for larger \( n \), particularly in the tail of the distribution where longer paths occur.

#### Analysis

1. **For \( p = 0.5 \):**

   - The distribution of rules: \( 3n + 1 \) and \( 3n - 1 \) were equally distributed,
   - As such, the results looked similar to the original Collatz sequence: [M_plot.png](plots\M_plot.png).

2. **For \( p = 0.25 \):**

   - The probabilistic distribution biases towards \( 3n - 1 \) reduces \( n \) more effectively,
   - Paths tend to be shorter on average as terminations were faster.
   - In general the std and mean is subtly smaller, the peak appears narrower .
   -

3. **For \( p = 0.75 \):**
   - Bias towards \( 3n + 1 \) increases \( n \), elongating the path lengths.
   - Paths take longer to terminate on average.

## Conclusion

- The core behavior of the Collatz sequence, reducing \( n \) over time, remains intact regardless of \( p \).
- such that: Probabilistic choices influence individual paths, but do not drastically alter the overall structure.
- The shape of multiplicity Averages out over a large range of \( n \), smoothing out the differences caused by probabilistic biases.
- Howver:
  - \( p = 0.25 \) results in shorter paths clustering around lower path lengths.
  - \( p = 0.75 \) shifts clusters of higher multiplicities towards longer paths.
