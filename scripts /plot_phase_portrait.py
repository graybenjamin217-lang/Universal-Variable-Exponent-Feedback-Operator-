import os
import numpy as np
import matplotlib.pyplot as plt

# Create output folder if it doesn't exist
os.makedirs("figures", exist_ok=True)

# 1. Run Variable-Exponent Simulation Engine
N = 500
y = np.zeros(N)
y[0] = 0.5  # Initial state

for n in range(1, N):
    alpha = 1.0 + 0.5 * np.sin(0.05 * n)  # Dynamic variable exponent
    y[n] = y[n-1] + 0.05 * (np.sin(y[n-1]) * (abs(y[n-1]) ** (alpha - 1.0)))

# 2. Phase-Space Extraction (y[n] vs y[n-1])
y_prev = y[:-1]  # State at n-1
y_curr = y[1:]   # State at n

plt.figure(figsize=(7, 6))

# Plot Trajectory & Boundaries
plt.plot(y_prev, y_curr, color='#0066cc', lw=1.2, alpha=0.85, label="Operator Trajectory")
plt.plot(y_prev[0], y_curr[0], 'go', markersize=8, label="Start $y_0$")
plt.plot(y_prev[-1], y_curr[-1], 'ro', markersize=8, label="End $y_N$")

# Fixed-Point Reference Line (y[n] = y[n-1])
axis_min = min(np.min(y_prev), np.min(y_curr))
axis_max = max(np.max(y_prev), np.max(y_curr))
plt.plot([axis_min, axis_max], [axis_min, axis_max], 'k--', alpha=0.35, label="Equilibrium ($y_n = y_{n-1}$)")

plt.title("Figure 2: Phase-Space Portrait ($y_n$ vs $y_{n-1}$)", fontsize=12, fontweight='bold')
plt.xlabel("Previous State $y[n-1]$", fontsize=11)
plt.ylabel("Current State $y[n]$", fontsize=11)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc="upper left")
plt.tight_layout()

# Save & Force Display
plt.savefig("figures/fig2_phase_portrait.png", dpi=300)
plt.show()

print("Status: Figure 2 successfully generated and saved to 'figures/fig2_phase_portrait.png'")
