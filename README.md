# Universal Feedback Operator: Autonomous Renormalization in $C^*$-Algebras

[![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23137306.svg)](https://doi.org/10.5281/zenodo.23137306)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview & Scope

This repository houses the mathematical framework, operator definitions, and numerical simulation suite for the universal feedback operator 
$\hat{\Omega}_G$

defined over the positive cone 
$\mathcal{A}_+$ 

of a unital $C^*$-algebra. The framework formalizes non-linear operator dynamics, autonomous renormalization, and discrete state integration, proving that the identity serves as a superattracting fixed point with controlled stability thresholds.

---

## Nomenclature & Glossary

| Symbol / Term | Definition |
| :--- | :--- |
| **$\mathcal{A}_+$** | Positive cone of a unital $C^*$-algebra. |
| **$\hat{\Omega}_G$** | Universal feedback operator defined via functional calculus as $\hat{\Omega}_G(\hat{A}) = \hat{A}^{-(\mathbf{I} - \hat{A}^{-1})}$. |
| **$\delta \approx 0.27417$** | Local derivative-based stability radius and contraction threshold around the identity. |
| **$C_\delta \approx 2.813$** | Quadratic error bound constant governing local convergence speed. |
| **DSI** | Discrete State Integration framework for autonomous nonlinear error suppression. |

---

## Theorem & Spectral Summary

* **Theorem 1 (Superattracting Fixed Point):** The identity operator $\mathbf{I}$ acts as a superattracting fixed point with a vanishing first Fréchet derivative $D\hat{\Omega}_G(\mathbf{I}) = 0$.
* **Theorem 2 (Quadratic Error Reduction):** Perturbations about the identity are suppressed to second order in the operator norm where $C_\delta \approx 2.813$.
* **Theorem 3 (Spectral Mapping):** By the Spectral Mapping Theorem, iterative application $\hat{\Omega}_G^n(\hat{A})$ causes spectra within the attraction basin to converge rapidly toward the identity spectrum $\sigma(\mathbf{I}) = \{1\}$.
* **Theorem 4 (Non-Abelian Shear Shielding):** Baker-Campbell-Hausdorff (BCH) expansion of symmetric multi-operator configurations $e^{\hat{X}/2} e^{\hat{Y}} e^{\hat{X}/2}$ demonstrates that linear commutator noise vanishes identically at first order.

---

## Repository Directory & Simulation Suite

Run the scripts in the `scripts/` directory to execute the numerical validation suite, with corresponding output assets saved to the `figures/` directory:

* `scripts/fig.1_feedback_fixed_points.py` — Evaluates scalar recurrence maps $f(x) = x^{(1/x - 1)}$, tracking superattracting fixed points at $x=1$ and repellers at $x=1/2$.
* `scripts/fig.2_frechet_expansion.py` — Computes operator Taylor expansions and verifies the vanishing first Fréchet derivative $D\hat{\Omega}_G(\mathbf{I}) = 0$ around identity.
* `scripts/fig.3_stability_threshold.py` — Maps derivative-based stability boundaries, identifying $x_{\text{crit}} \approx 0.7258$ and the local contraction radius $\delta \approx 0.27417$.
* `scripts/fig.4_dsi_filtering.py` — Simulates Discrete State Integration (DSI) under sub-critical continuous phase fluctuations to demonstrate quadratic error suppression toward unity.
* `scripts/fig.5_bch_shear_suppression.py` — Evaluates symmetric multi-operator configurations $e^{\hat{X}/2} e^{\hat{Y}} e^{\hat{X}/2}$ via Baker-Campbell-Hausdorff expansion to verify the suppression of linear commutator noise.

---

## Citation

If you utilize this feedback operator framework or numerical simulation suite in your research, please cite the corresponding Zenodo record:

```bibtex
@article{Gray2026FeedbackOperator,
  title={The Universal Variable-Exponent Feedback Operator},
  author={Gray, Benjamin Edward},
  journal={Zenodo},
  year={2026},
  doi={10.5281/zenodo.23137306}
}
