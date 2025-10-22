---
id: c89bc724-6ca4-4174-bf79-83d9683b9c5c
name: Check for interesting permissions on accounts
type: command
executor: bash
data: Invoke-ACLScanner -ResolveGUIDs | ?{$_.IdentinyReferenceName -match "RDPUsers"}
output: null
created_at: '2023-04-06T03:56:06.700649+00:00'
updated_at: '2023-04-10T20:26:07.517652+00:00'
---

# Check for interesting permissions on accounts

```bash
Invoke-ACLScanner -ResolveGUIDs | ?{$_.IdentinyReferenceName -match "RDPUsers"}
```
