"""KGraph Compressed Topological Map."""
from typing import Dict, Any

NODES = {
    "commodity": {"weight": 1.0, "tier": 1},
    "differentiated": {"weight": 2.5, "tier": 2},
    "cognitive_monopoly": {"weight": 5.0, "tier": 3},
    "ecosystem_dominance": {"weight": 10.0, "tier": 4},
}

EDGES = {
    "linear_upgrade": {"from": "commodity", "to": "differentiated", "weight": 1.2},
    "perceptual_shift": {"from": "differentiated", "to": "cognitive_monopoly", "weight": 3.0},
    "structural_lockin": {"from": "differentiated", "to": "cognitive_monopoly", "weight": 2.5},
    "preemptive_jump": {"from": "cognitive_monopoly", "to": "ecosystem_dominance", "weight": 4.0},
    "ecosystem_leap": {"from": "commodity", "to": "ecosystem_dominance", "weight": 8.0},
}

class KGraph:
    def __init__(self):
        self.nodes = NODES
        self.edges = EDGES

    def path_weight(self, edge_name: str) -> float:
        return self.edges.get(edge_name, {}).get("weight", 0.0)

    def to_dict(self) -> Dict[str, Any]:
        return {"nodes": self.nodes, "edges": self.edges}
