import numpy as np
import matplotlib.pyplot as plt

# =====================================================================
# Figure 6: DSI Convergence Matrix & Noise Immunity Efficiency
# Framework: Universal Feedback Operator (Gray, 2026)
# Parameters: Stability Threshold delta ~ 0.27417, Quadratic Constant C_delta ~ 2.813
# =====================================================================

def omega_scalar(x):
    """Scalar generator f(x) = x^(1/x - 1) for x > 0."""
    with np.errstate(all='ignore'):
        res = np.where(x > 0, x**(1.0/x - 1.0), 0.0)
    return res

def simulate_dsi_iterations(h0, noise_sigma, max_iter=20, tolerance=1e-6):
    """
    Simulates iterative DSI convergence starting from perturbation h0
    with continuous sub-critical noise sigma added at each step.
    Returns the number of iterations required to reach tolerance, or max_iter.
    """
    x = 1.0 + h0
    for i in range(max_iter):
        if np.abs(x - 1.0) < tolerance:
            return i
        # Apply operator mapping
        x = omega_scalar(x)
        # Add continuous noise bounded by sigma
        if noise_sigma > 0:
            noise = np.random.normal(0, noise_sigma)
            x += noise
            x = max(x, 1e-5) # Ensure domain validity
    return max_iter

# Set up grid parameters (extended X-axis to 0.30 to clearly frame the threshold line)
n_points = 60
h0_vals = np.linspace(0.01, 0.30, n_points)  
sigma_vals = np.linspace(0.0, 0.05, n_points) # Sub-critical noise amplitude range

convergence_grid = np.zeros((len(sigma_vals), len(h0_vals)))

np.random.seed(42)
for i, sig in enumerate(sigma_vals):
    for j, h0 in enumerate(h0_vals):
        convergence_grid[i, j] = simulate_dsi_iterations(h0, sig, max_iter=15)

# Plotting the Convergence Matrix Heatmap
plt.figure(figsize=(10, 6), dpi=300)
plt.imshow(convergence_grid, extent=[h0_vals[0], h0_vals[-1], sigma_vals[-1], sigma_vals[0]], 
           aspect='auto', cmap='viridis')
plt.colorbar(label='Iterations to Convergence (tol < 1e-6)')
plt.title('Figure 6: DSI Convergence Matrix & Noise Immunity Efficiency', fontsize=12, fontweight='bold')
plt.xlabel('Initial Perturbation Magnitude ||H_0||', fontsize=11)
plt.ylabel('Continuous Noise Amplitude ($\sigma$)', fontsize=11)
plt.grid(True, linestyle='--', alpha=0.3)

# Draw stability threshold boundary line at x = 0.27417
thresh = 0.27417
plt.axvline(x=thresh, color='red', linestyle=':', linewidth=2.0)

# Direct text annotation placed cleanly in the upper-left area to avoid blocking matrix values
plt.text(0.03, 0.005, 'Stability Threshold\n$\\delta \\approx 0.27417$', 
         color='white', fontsize=9, fontweight='bold', 
         bbox=dict(facecolor='black', alpha=0.75, edgecolor='red', boxstyle='round,pad=0.5'))

plt.tight_layout()
plt.savefig('fig.6_convergence_matrix.png', dpi=300)
plt.show()
print("Figure 6 updated and saved successfully as 'fig.6_convergence_matrix.png'.")
