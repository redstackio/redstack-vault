---
id: fc9323be-73cf-4e50-b031-0e712e6dc470
name: Check if TRUSTED_FOR_DELEGATION is enabled
type: command
executor: bash
data: Get-ADComputer -Identity 'ComputerName' -Properties TrustedForDelegation
output: null
created_at: '2023-04-06T03:56:07.426068+00:00'
updated_at: '2023-04-10T20:36:05.043995+00:00'
---

# Check if TRUSTED_FOR_DELEGATION is enabled

```bash
Get-ADComputer -Identity 'ComputerName' -Properties TrustedForDelegation
```
