---
id: proc-escape-via-x11
tags:
  - container-escape
  - x11-exploit
type: procedure
tools:
  - '[[tools/snap]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Linux
  - Ubuntu
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Escape to Host]]'
updated_at: '2025-12-14T17:23:23.834Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Escape to Host]]'
---
# Escape-Snap-Container-via-X11

## Summary

Exploit the X11 plug permissions in the snap to escape the container boundaries, pivoting the RCE payload to the host system and achieving full access as the current user.

## Description

Snaps with the 'x11' interface allow access to the DISPLAY and XAUTHORITY for GUI apps. The malicious payload, post-RCE, leverages this to connect to the host's X server, bypassing AppArmor confinement and executing in the host context. This grants access to dotfiles and system resources previously denied.

## Requirements

1. Snap app with X11 plug (e.g., Chromium)
2. X11 server running on host
3. RCE payload capable of X11 interaction

## Defense

Defensive measures and detection strategies:

- Disable unnecessary plugs like x11 in snap declarations
- Use wayland instead of X11 to reduce attack surface
- Monitor X11 connections from snap processes

## Objectives

1. Break out of snap confinement
2. Gain host-level execution
3. Enable full user compromise

## Instructions

### Step 1: Trigger X11 Pivot

**Context**: Use payload to exploit X11 permissions for escape. No direct command; integrated into RCE payload execution from prior step.

**Command** ():
```bash
# Payload handles escape via X11 socket access
```

> Automatically pivots after RCE trigger. Expected: No visible output, but subsequent host access succeeds.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Escape to Host]] Escape to Host

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/snap]]

## Tags

- container-escape
- x11-exploit
