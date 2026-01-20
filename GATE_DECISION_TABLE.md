# Gate Library — Decision Table

This table defines **all possible queries to the Gate** and their expected semantic outcomes.

| Action           | Rule Set Value      | Expected Decision      | Notes                                |
|-----------------|------------------|----------------------|-------------------------------------|
| read_file       | ALLOW             | ALLOW                | Explicitly allowed                   |
| read_file       | DENY              | DENY                 | Explicitly denied                    |
| read_file       | ESCALATE          | ESCALATE             | Requires higher authority            |
| read_file       | UNDEFINED         | UNDEFINED            | Defaults to deny if interpreted     |
| delete_file     | ALLOW             | ALLOW                | Explicitly allowed                   |
| delete_file     | DENY              | DENY                 | Explicitly denied                    |
| delete_file     | ESCALATE          | ESCALATE             | Requires higher authority            |
| delete_file     | UNDEFINED         | UNDEFINED            | Defaults to deny if interpreted     |
| unknown_action  | any               | UNDEFINED            | Any undefined action returns UNDEFINED|

## Notes

- **UNDEFINED** must always be interpreted as deny in execution layers.
- **ESCALATE** requires explicit handling.
- No action may implicitly become ALLOW.
- Every action query is deterministic.
