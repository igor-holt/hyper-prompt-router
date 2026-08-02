# Hyper-Prompt Routing Architecture

A novel AI system for competitive strategy analysis using tiered classification, Anthagonal Tension Matrix evaluation, and vectorized knowledge graph routing.

## Overview

The Hyper-Prompt Routing Architecture is a complete, integrated system for analyzing competitive positioning and generating actionable business moat artifacts. It combines:

- **4-Tier Competitive Framework**: Commodity Offer (Tier 1) through Ecosystem Dominance (Tier 4)
- **Anthagonal Tension Matrix Evaluator**: Three perpendicular axes (Perceptual/Cognitive, Scale/Exponential, Strategic/Proactive)
- **Constraint/Weight Matrix**: Explicit bounds for decay, factuality, switching costs
- **KGraph Compressed Topological Map**: Node/edge weights with linear_upgrade, perceptual_shift, structural_lockin, preemptive_jump, ecosystem_leap relations
- **JAX-jitted Evaluation Functions**: Vectorized embedding projection with constraint masking and softmax

## Architecture Components

### 1. Tiered Classification Engine

```
Tier 1: Commodity Offer / Standard Offer Engine
  - Persona: Transactional Auditor
  - Artifacts: Price comparison, feature parity matrices
  - Metrics: Cost per unit, marginal efficiency

Tier 2: Feature Advantage
  - Persona: Direct Competitor Analyst  
  - Artifacts: Differentiation maps, upgrade paths
  - Metrics: Friction coefficient, feature velocity

Tier 3: Pre-Emptive Advantage / Cognitive Monopoly Frame
  - Persona: Category Storyteller
  - Artifacts: Narrative frameworks, perceptual positioning
  - Metrics: Narrative authority, cognitive lock-in

Tier 4: Exponential Monopoly / Ecosystem Dominance
  - Persona: Ecosystem Architect
  - Artifacts: Platform blueprints, network effect models
  - Metrics: Network effect exponent, ecosystem leverage
```

### 2. Anthagonal Tension Matrix

Operates on three perpendicular axes:
- **Axis A**: Perceptual/Tangible vs. Cognitive
- **Axis B**: Scale/Linear vs. Exponential  
- **Axis C**: Strategic/Reactive vs. Proactive

Equilibrium rules apply when all three axis functions (F_A, F_B, F_C) converge within tolerance thresholds.

### 3. Constraint Matrix

| Constraint | Bound | Consequence |
|------------|-------|-------------|
| C1: Decay Time | τ_decay ≤ 6 months | Demotion to lower tier |
| C2: Factuality | ≥ 0.95 | Rejection if violated |
| C3: Switching Cost | > 5× acquisition cost | Required for Tier 3+ |
| C4: Network Effect | Exponent > 1.0 | Required for Tier 4 |
| C5: Cognitive Lock-in | Measurable narrative authority | Required for Tier 3+ |

### 4. KGraph Topology

```json
{
  "nodes": {
    "commodity": {"weight": 1.0, "tier": 1},
    "differentiated": {"weight": 2.5, "tier": 2},
    "cognitive_monopoly": {"weight": 5.0, "tier": 3},
    "ecosystem_dominance": {"weight": 10.0, "tier": 4}
  },
  "edges": {
    "linear_upgrade": {"from": "commodity", "to": "differentiated", "weight": 1.2},
    "perceptual_shift": {"from": "differentiated", "to": "cognitive_monopoly", "weight": 3.0},
    "structural_lockin": {"from": "differentiated", "to": "cognitive_monopoly", "weight": 2.5},
    "preemptive_jump": {"from": "cognitive_monopoly", "to": "ecosystem_dominance", "weight": 4.0},
    "ecosystem_leap": {"from": "commodity", "to": "ecosystem_dominance", "weight": 8.0}
  }
}
```

## Implementation

See [core/](core/) for JAX implementation and [service/](service/) for Podman deployment.

## Marketplace Integration

- **GitHub**: Source repository with MIT license
- **Apify**: Actor for distributed evaluation jobs
- **Stripe**: Primary payment processing
- **Square**: Failover payment processing

## Quick Start

```bash
# Clone and setup
git clone https://github.com/igor-holt/hyper-prompt-router.git
cd hyper-prompt-router

# Install dependencies
pip install -r requirements.txt

# Run evaluation
python -m hyper_prompt_router.evaluate --input prompts.json

# Start service (Podman)
podman-compose up -d
```

## License

MIT License - See [LICENSE](LICENSE) for details.
