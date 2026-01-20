import pytest
from your_module import Gate, GateDecision

def test_gate_basic_rules():
    gate = Gate()
    gate.set_rule("read_file", GateDecision.ALLOW)
    gate.set_rule("delete_file", GateDecision.DENY)

    assert gate.decide("read_file") == GateDecision.ALLOW
    assert gate.decide("delete_file") == GateDecision.DENY
    assert gate.decide("unknown_action") == GateDecision.UNDEFINED

def test_gate_escalate_rule():
    gate = Gate()
    gate.set_rule("modify_settings", GateDecision.ESCALATE)
    assert gate.decide("modify_settings") == GateDecision.ESCALATE

def test_gate_type_check():
    gate = Gate()
    with pytest.raises(TypeError):
        gate.set_rule("read_file", "ALLOW")  # must be GateDecision
