"""Anthagonal Tension Matrix Evaluator."""
import jax.numpy as jnp
from jax import jit

@jit
def axis_a(perceptual: float, cognitive: float) -> float:
    return jnp.tanh(cognitive - perceptual)

@jit
def axis_b(scale: float, exponential: float) -> float:
    return jnp.log1p(exponential) - scale

@jit
def axis_c(reactive: float, proactive: float) -> float:
    return proactive - reactive

class AnthagonalTensionMatrix:
    def evaluate(self, fa: float, fb: float, fc: float, tol: float = 0.1) -> bool:
        """Equilibrium when all three converge within tolerance."""
        return (jnp.abs(fa) < tol) and (jnp.abs(fb) < tol) and (jnp.abs(fc) < tol)
