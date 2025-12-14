---
tags:
  - xss-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:33:24.257Z'
skill_level: low
impact_level: high
detection_risk: medium
sub_techniques: []
id: 3b4e96b9-2304-483d-bf96-8e89b825319e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-on-Message-View

## Summary

This procedure relies on victim interaction to render the stored malicious message, triggering the XSS by exploiting the client-side parsing chain that injects and executes JavaScript attributes during HTML rendering.

## Description

Once the payload is stored server-side, viewing the message in the Rocket.Chat web client causes the Markdown parser to tokenize the content (inline-code and URL), followed by AutoLinker wrapping it in an <a> tag. The malformed payload breaks out of the href, injecting style (for animation) and onanimationiteration (for JS execution via eval override). This runs in the victim's browser context, with no server-side execution. Expected outcomes include arbitrary JS like alerts or script loads. Prerequisites: Payload already sent; victim must load the chat view.

## Requirements

1. Victim access to the same Rocket.Chat channel
2. Victim's browser rendering the message (e.g., refresh or new load)
3. No CSP blocking animations or eval

## Defense

Defensive measures and detection strategies:

- Enforce CSP to restrict script sources and eval
- Client-side monitoring for animation events triggering JS
- Log unusual attribute injections in rendering logs
- Educate users on suspicious links in chats

## Objectives

1. Execute injected JS in victim context
2. Confirm payload activation
3. Prepare for data exfiltration

## Instructions

### Step 1: Direct Victim to Channel

**Context**: Ensure the victim views the message to initiate rendering.

No command; social engineering or shared channel access.

> Expected: Victim loads the chat page.

### Step 2: Monitor Execution

**Context**: Observe JS execution via network requests or alerts.

Use browser dev tools on a test victim account to verify:

```javascript
// In console, check for alert or script load after render
console.log('XSS triggered if this runs');
```

> Expected: Animation starts, onanimationiteration fires, eval executes payload.

### Step 3: Validate Breakout

**Context**: Inspect rendered HTML to confirm attribute injection.

In dev tools, inspect the <a> element:

```javascript
// Expected malformed: <a href="https:// style=... onanimationiteration=...">
```

> Success if attributes like onanimationiteration are present and executable.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-execution
