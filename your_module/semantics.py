from enum import Enum, auto


class GateDecision(Enum):
    """
    Semantic authorization outcomes.
    The gate never executes actions.
    """
    ALLOW = auto()
    DENY = auto()
    ESCALATE = auto()
    UNDEFINED = auto()
