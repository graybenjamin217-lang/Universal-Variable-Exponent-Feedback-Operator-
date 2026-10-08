import os
import numpy as np
import matplotlib.pyplot as plt

# Ensure output directory exists
os.makedirs("figures", exist_ok=True)

# 1. Simulation Setup
N = 300
steps = np.arange(1, N)
K = 0.08
A = 0.8
y0 = 0.5

# Run discrete operator trajectory
y = np.zeros(N)
y[0] = y0

for n in range(1, N):
    alpha = 1.0 + A * np.sin(0.05 * n)
    dy = K * np.sin(y[n-1]) * (np.abs(y[n-1]) ** (alpha - 1.0))
    y[n] = y[n-1] + dy

# 2. Compute Convergence & Residual Error Metrics
step_error = np.abs(np.diff(y))
cumulative_mse = np.cumsum(step_error**2) / np.arange(1, N)

# 3. Render Convergence Error Plot
plt.figure(figsize=(9, 5.5))

plt.semilogy(steps, step_error, 'b-', label=r'Absolute Step Residual $|y_n - y_{n-1}|$', alpha=0.85, linewidth=1.5)
plt.semilogy(steps, cumulative_mse, 'r--', label=r'Cumulative Mean Squared Error (MSE)', linewidth=2.0)

plt.title("Figure 5: Convergence Error & Residual Analysis", fontsize=12, fontweight='bold')
plt.xlabel("Iteration Step ($n$)", fontsize=11)
plt.ylabel("Error Magnitude (Log Scale)", fontsize=11)
plt.grid(True, which="both", linestyle=':', alpha=0.6)
plt.legend(fontsize=10, loc='upper right')
plt.tight_layout()

# Save PNG and render inline
plt.savefig("figures/fig5_convergence_error.png", dpi=300)
plt.show()

print("Status: Figure 5 successfully generated and saved to 'figures/fig5_convergence_error.png'")
