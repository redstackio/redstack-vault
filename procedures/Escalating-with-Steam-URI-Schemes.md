---
tags:
  - uri-abuse
  - escalation
  - steam
type: procedure
tools:
  - '[[tools/Remote-Chrome-Console]]'
  - '[[tools/Binary-Grep]]'
  - '[[tools/Vim]]'
tactics:
  - '[[Lateral Movement]]'
commands:
  - '[[commands/open-steam-uri]]'
  - '[[commands/object-keys-window]]'
  - '[[commands/window-top-postmessage]]'
  - '[[commands/txt-hello-protocol]]'
platforms:
  - Windows
techniques:
  - '[[Command-Line Interface]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 79f043b6-ef3a-49f9-8d46-03adc4f7377e
created_at: '2025-12-14T00:11:25.293Z'
updated_at: '2025-12-14T00:11:25.293Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Escalating with Steam URI Schemes

## Summary

This procedure escalates XSS to privileged actions using steam:// URIs and OEMBED injections.

## Description

Abuse steam:// schemes to execute actions without confirmation, and use embeds like codepen.io for further exploration.

## Requirements

1. Active XSS in chat
2. Access to remote console
3. Steam binaries for reverse engineering

## Defense

Defensive measures and detection strategies:

- Require user confirmation for steam:// URIs
- Whitelist allowed URI schemes

## Objectives

1. Execute privileged steam:// actions
2. Inspect window properties
3. Discover undocumented protocols

## Instructions

### Step 1: Test Steam URIs

**Context**: Use remote console to open URIs.

Execute [[commands/open-steam-uri]]:

```javascript
open("steam://xxx")
```

> Expected: Privileged action executes.

### Step 2: Embed and Inspect

**Context**: Use OEMBED for JS injection.

Run [[commands/object-keys-window]]:

```javascript
Object.keys(window)
```

And [[commands/window-top-postmessage]]:

```javascript
window.top.postMessage()
```

> Expected: Window properties dumped.

### Step 3: Reverse Engineer Binaries

**Context**: Search for URIs.

Use [[tools/Binary-Grep]] and [[tools/Vim]] to find steam://openexternalforpid.

> Expected: Undocumented URIs identified.

### Step 4: Test Custom Protocols

**Context**: Explore Windows protocols.

Run [[commands/txt-hello-protocol]]:

```bash
.txt:hello
```

> Expected: Notepad opens.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/open-steam-uri]]
- [[commands/object-keys-window]]
- [[commands/window-top-postmessage]]
- [[commands/txt-hello-protocol]]

## Tools Used

- [[tools/Remote-Chrome-Console]]
- [[tools/Binary-Grep]]
- [[tools/Vim]]

## Tags

- uri-abuse
- escalation
- steam
