# Gate Library — Formal Authorization Contract

## Purpose

The Gate Library provides a **semantic authorization gate**.
It determines whether an action is permitted, forbidden, requires escalation,
or is undefined.

The gate **does not execute actions**.
The gate **does not mutate system state**.
The gate **only emits semantic decisions**.

---

## Core Definitions

### Gate
A deterministic decision engine that maps symbolic actions to semantic outcomes.

### Action
A string identifier representing an intent (e.g. "read_file", "delete_user").

### Decision (GateDecision)
One of the following semantic values:

- ALLOW — Explicitly permitted
- DENY — Explicitly forbidden
- ESCALATE — Requires higher authority
- UNDEFINED — No rule exists (defaults to deny)

---

## Invariants (Non-Negotiable)

1. The gate MUST NOT execute actions.
2. The gate MUST NOT return booleans or numeric values.
3. The gate MUST return a GateDecision for every query.
4. UNDEFINED MUST NOT imply ALLOW.
5. ESCALATE MUST be explicit.
6. The gate MUST be deterministic for the same inputs.
7. The gate MUST be side-effect free.

---

## Security Guarantees

- No implicit privilege escalation
- No default allow behavior
- No execution coupling
- No state leakage
- No numeric ambiguity

---

## Execution Layer Responsibility

Any execution layer consuming this gate:

- MUST explicitly interpret GateDecision values
- MUST implement DENY and UNDEFINED as non-execution
- MUST NOT assume ALLOW implies success
- MUST log or handle ESCALATE explicitly

---

## Version Stability

The semantic meaning of GateDecision values is stable across versions.
New values may be added, but existing meanings MUST NOT change.

---

## License Notice

This contract applies to all uses of the Gate Library under:
- AGPL-3.0-or-later
- Commercial License

Any use that violates these invariants is considered an incorrect integration.
