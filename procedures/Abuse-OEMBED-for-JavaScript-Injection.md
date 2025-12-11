---
tags:
  - oembed
  - injection
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
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 4fb78a8c-15d3-4ef6-8093-00fe0a4d45a4
created_at: '2025-12-11T06:10:22.138Z'
updated_at: '2025-12-11T06:10:22.138Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Abuse OEMBED for JavaScript Injection

## Summary

This procedure uses whitelisted OEMBED services like codepen.io to inject JavaScript in iframes and attempt access to privileged APIs.

## Description

OEMBED iframes in Steam's CEF context may not be properly sandboxed, allowing postMessage or open() to execute steam:// URIs.

## Requirements

1. Ability to embed OEMBED links in chat
2. Remote debugging setup

## Defense

Defensive measures and detection strategies:

- Sandbox OEMBED iframes strictly
- Block postMessage to privileged contexts

## Objectives

1. Inject JS in iframe
2. Communicate with parent window
3. Execute steam:// from iframe

## Instructions

### Step 1: Embed Malicious OEMBED

**Context**: Send codepen.io link with injected JS.

Send OEMBED URL in chat.

> Expected: Iframe renders with custom JS.

### Step 2: Execute Injected Code

**Context**: Test privileged access.

In [[tools/Remote-Chrome-Console]], run [[commands/window-top-postmessage]]:

```javascript
window.top.postMessage()
```

Run [[commands/open-steam-uri]]:

```javascript
open("steam://xxx")
```

Run [[commands/object-keys-window]]:

```javascript
Object.keys(window)
```

> Expected: Potential execution of Steam actions.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/window-top-postmessage]]
- [[commands/open-steam-uri]]
- [[commands/object-keys-window]]

## Tools Used

- [[tools/Remote-Chrome-Console]]

## Tags

- [[oembed]]
- [[injection]]
