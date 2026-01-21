# your_module/semantics.py
from enum import Enum

class GateDecision(str, Enum):
    """
    Semantic decisions for the Gate Library.
    These are the only valid outcomes when querying the gate.
    """
    ALLOW = "allow"
    DENY = "deny"
    ESCALATE = "escalate"
    UNDEFINED = "undefined"
