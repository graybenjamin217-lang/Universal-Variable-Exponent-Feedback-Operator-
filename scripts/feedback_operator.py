import numpy as np
import matplotlib.pyplot as plt

def variable_exponent(t: np.ndarray, alpha_0: float = 1.0, k: float = 0.5) -> np.ndarray:
    """
    Defines time-varying exponent alpha(t).
    
    Parameters:
        t       : Time vector
        alpha_0 : Base exponent value
        k       : Modulation amplitude or rate
    """
    # Example: Sinusoidally modulated exponent alpha(t) = alpha_0 + k * sin(omega * t)
    return alpha_0 + k * np.sin(0.5 * np.pi * t)

def simulate_feedback_operator(
    t: np.ndarray, 
    x: np.ndarray, 
    beta: float = 0.25, 
    alpha_func=variable_exponent
) -> tuple[np.ndarray, np.ndarray]:
    """
    Simulates a discrete-time non-linear feedback operator of the form:
    y[n] = x[n] + beta * sign(y[n-1]) * |y[n-1]|^alpha(t[n])
    """
    N = len(t)
    y = np.zeros(N)
    alpha_vals = alpha_func(t)
    
    # Initialize with first input step
    y[0] = x[0]
    
    # Time-stepping feedback loop
    for n in range(1, N):
        prev_y = y[n - 1]
        a_n = alpha_vals[n]
        
        # Calculate non-scalar / non-linear feedback term
        feedback_term = beta * np.sign(prev_y) * (np.abs(prev_y) ** a_n)
        
        # State update
        y[n] = x[n] + feedback_term
        
    return y, alpha_vals

def plot_results(t: np.ndarray, x: np.ndarray, y: np.ndarray, alpha_vals: np.ndarray):
    """Generates two-panel plot for system input, variable exponent, and output."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
    
    # Panel 1: Exponent alpha(t) evolution
    ax1.plot(t, alpha_vals, color='tab:purple', linewidth=2, label=r'Exponent $\alpha(t)$')
    ax1.set_ylabel(r'Exponent Value $\alpha$', fontsize=11)
    ax1.set_title('Variable Exponent Feedback Operator Simulation', fontsize=13, fontweight='bold')
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.legend(loc='upper right')
    
    # Panel 2: Input x(t) vs Operator Output y(t)
    ax2.plot(t, x, 'k--', label=r'Input Drive $x(t)$', alpha=0.7)
    ax2.plot(t, y, color='tab:blue', linewidth=2, label=r'Operator Output $y(t)$')
    ax2.set_xlabel('Time $t$', fontsize=11)
    ax2.set_ylabel('Amplitude', fontsize=11)
    ax2.grid(True, linestyle='--', alpha=0.6)
    ax2.legend(loc='upper right')
    
    plt.tight_layout()
    plt.savefig('figures/operator_response.png', dpi=300)
    plt.show()

if __name__ == "__main__":
    # 1. Define time domain
    t_span = np.linspace(0, 10, 1000)
    
    # 2. Define input driving signal x(t) (e.g., harmonic excitation)
    x_in = np.sin(2 * np.pi * 0.5 * t_span)
    
    # 3. Run simulation
    y_out, alpha_t = simulate_feedback_operator(t_span, x_in, beta=0.3)
    
    # 4. Render and save plots
    plot_results(t_span, x_in, y_out, alpha_t)
