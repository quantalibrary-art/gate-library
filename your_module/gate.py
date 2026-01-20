from .semantics import GateDecision


class Gate:
    """
    Quantized Authorization Gate

    The gate:
    - never executes actions
    - never mutates external state
    - only returns semantic decisions
    """

    def __init__(self):
        self._rules = {}  # action -> GateDecision

    def set_rule(self, action: str, decision: GateDecision):
        if not isinstance(decision, GateDecision):
            raise TypeError("decision must be a GateDecision")
        self._rules[action] = decision

    def decide(self, action: str) -> GateDecision:
        return self._rules.get(action, GateDecision.UNDEFINED)
