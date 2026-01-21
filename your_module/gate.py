# your_module/gate.py
from .semantics import GateDecision

class Gate:
    """
    Quantized Authorization Gate.
    Determines if an action is allowed based on semantic rules.
    """

    def __init__(self):
        self.rules = {}  # maps actions to GateDecision

    def set_rule(self, action: str, decision: GateDecision):
        """
        Set a semantic rule for a given action.
        """
        self.rules[action] = decision

    def decide(self, action: str) -> GateDecision:
        """
        Return the semantic decision for the given action.
        Defaults to UNDEFINED if no rule exists.
        """
        return self.rules.get(action, GateDecision.UNDEFINED)


# Example usage
if __name__ == "__main__":
    gate = Gate()
    gate.set_rule("read_file", GateDecision.ALLOW)
    gate.set_rule("delete_file", GateDecision.DENY)

    print("read_file:", gate.decide("read_file"))
    print("delete_file:", gate.decide("delete_file"))
    print("unknown_action:", gate.decide("unknown_action"))
