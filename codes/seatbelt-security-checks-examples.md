---
id: e65aa469-e0f9-499d-bc8d-404c5089e945
type: code
name: seatbelt-security-checks-examples
language: cmd
verified: true
created_at: '2023-04-06T03:56:28.513966+00:00'
updated_at: '2023-04-10T20:37:50.960310+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - remote
validated: true
---

# seatbelt-security-checks-examples

## Code

```cmd
Seatbelt.exe -group=all -full
Seatbelt.exe -group=system -outputfile="C:\Temp\system.txt"
Seatbelt.exe -group=remote -computername=dc.theshire.local -computername=192.168.230.209 -username=THESHIRE\sam -password="yum \"po-ta-toes\"" 
```

## Description

Examples of Seatbelt.exe invocations for local full checks, system output to file, and remote enumeration with credentials.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| computername | Target host/IP | dc.theshire.local |
| username | Auth username | THESHIRE\sam |
| password | Auth password | yum "po-ta-toes" |
| outputfile | Output path | C:\Temp\system.txt |

## Usage

Use in post-exploitation for host surveying; adapt credentials for lateral movement scenarios.

## Detection

- Seatbelt.exe execution (file hash known to EDR).
- Remote WMI/RPC calls (Event ID 5145 for share access).
- Credential use in processes (LSASS dumps if failed).

## Related

- [[procedures/windows-privilege-escalation-using-powerup-privesccheck-and-wes-ng]]
- [[tools/SeatBelt]]
