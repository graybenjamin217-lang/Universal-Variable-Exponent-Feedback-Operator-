import os
import numpy as np
import matplotlib.pyplot as plt

# Ensure output directory exists
os.makedirs("figures", exist_ok=True)

# 1. Simulation Setup
N = 300
steps = np.arange(N)
K = 0.08      # Coupling Gain
y0 = 0.5      # Initial Condition
A = 0.8       # Exponent Modulation Amplitude

# Pre-allocate arrays
y_linear = np.zeros(N)
y_quadratic = np.zeros(N)
y_dynamic = np.zeros(N)

y_linear[0] = y0
y_quadratic[0] = y0
y_dynamic[0] = y0

# 2. Benchmark Model 1: Static Exponent (alpha = 1.0)
for n in range(1, N):
    dy = K * np.sin(y_linear[n-1]) * (abs(y_linear[n-1]) ** 0.0)
    y_linear[n] = y_linear[n-1] + dy

# 3. Benchmark Model 2: Static Exponent (alpha = 2.0)
for n in range(1, N):
    dy = K * np.sin(y_quadratic[n-1]) * (abs(y_quadratic[n-1]) ** 1.0)
    y_quadratic[n] = y_quadratic[n-1] + dy

# 4. Proposed Dynamic Variable-Exponent Operator
for n in range(1, N):
    alpha = 1.0 + A * np.sin(0.05 * n)
    dy = K * np.sin(y_dynamic[n-1]) * (abs(y_dynamic[n-1]) ** (alpha - 1.0))
    y_dynamic[n] = y_dynamic[n-1] + dy

# 5. Render Comparison Plot
plt.figure(figsize=(9, 5.5))
plt.plot(steps, y_linear, 'k--', label=r'Static Baseline ($\alpha = 1.0$)', alpha=0.75, linewidth=1.5)
plt.plot(steps, y_quadratic, 'b-.', label=r'Static Baseline ($\alpha = 2.0$)', alpha=0.75, linewidth=1.5)
plt.plot(steps, y_dynamic, 'r-', label=r'Dynamic Operator ($\alpha(n) = 1.0 + A\sin(0.05n)$)', linewidth=2.0)

plt.title("Figure 4: Benchmark Trajectory Comparison", fontsize=12, fontweight='bold')
plt.xlabel("Iteration Step ($n$)", fontsize=11)
plt.ylabel("State Trajectory ($y_n$)", fontsize=11)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=10, loc='upper left')
plt.tight_layout()

# Save PNG and render inline
plt.savefig("figures/fig4_benchmark_comparison.png", dpi=300)
plt.show()

print("Status: Figure 4 successfully generated and saved to 'figures/fig4_benchmark_comparison.png'")
