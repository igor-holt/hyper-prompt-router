"""JAX-jitted Evaluation Functions."""
import jax.numpy as jnp
from jax import jit
from .tiers import TieredClassifier, Tier
from .matrix import AnthagonalTensionMatrix
from .kgraph import KGraph

@jit
def project_embedding(emb: jnp.ndarray, mask: jnp.ndarray) -> jnp.ndarray:
    masked = emb * mask
    return jnp.softmax(masked)

def evaluate_prompt(prompt: str, constraints: dict = None) -> dict:
    """Vectorized evaluation entry point."""
    classifier = TieredClassifier()
    matrix = AnthagonalTensionMatrix()
    kg = KGraph()
    # Placeholder: real path uses embedding model + constraint masking
    tier = classifier.classify({"text": prompt})
    return {
        "tier": int(tier),
        "kgraph": kg.to_dict(),
        "equilibrium": matrix.evaluate(0.05, 0.02, 0.08),
        "constraints_passed": True,
    }
