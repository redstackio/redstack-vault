---
id: 2a1f309f-bdb1-42c1-8de5-445ad968ae75
name: Mimikatz-Debug-and-Logon-Passwords
type: code
language: text
verified: true
created_at: '2023-04-06T03:56:27.446213+00:00'
updated_at: '2024-10-01T12:00:00+00:00'
platforms:
  - Windows
tags:
  - mimikatz
  - credential-dumping
validated: true
---

# Mimikatz-Debug-and-Logon-Passwords

## Code

```text
privilege::debug
ts::logonpasswords
```

## Description

This code snippet contains the exact Mimikatz module commands to enable debug privileges and dump logon passwords (including RDP sessions) from LSASS memory. It is intended for interactive use within the Mimikatz shell when non-interactive execution is not feasible or for step-by-step verification.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | These are fixed Mimikatz commands with no variables | N/A |

## Usage

On a compromised Windows system with admin rights, download and run mimikatz.exe. At the "mimikatz #" prompt:
1. Enter "privilege::debug" to elevate privileges (expect "Privilege '20' OK").
2. Enter "ts::logonpasswords" to extract and display logon credentials.
3. Review output for RDP-related sessions and type "exit" to quit.
This is useful in environments where command-line arguments are logged, as interactive input may evade some detections. Deliver via initial access vectors like SMB share or in-memory loading.

## Detection

- PowerShell or cmd logging capturing "privilege::debug" or "ts::logonpasswords" inputs.
- EDR alerts on SeDebugPrivilege token modification or LSASS handle opens by mimikatz.exe.
- Behavioral analytics for unusual interactive console sessions with security tool patterns.
- File integrity monitoring on Mimikatz binaries or renamed variants.

## Related

- [[procedures/Windows-Mimikatz-RDP-Password-Extraction]]
- [[tools/Mimikatz]]
