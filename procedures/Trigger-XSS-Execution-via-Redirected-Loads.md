---
tags:
  - xss-execution
  - js-injection
  - csp-bypass
type: procedure
tools:
  - '[[tools/DevTools]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/host-alert-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:19.814Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: ecb95593-8f98-4a14-a6e5-c8c9b34e619d
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Execution-via-Redirected-Loads

## Summary

This procedure triggers the stored XSS by reloading the affected GitLab page, causing the <base> tag to redirect script loads to the attacker server, resulting in arbitrary JavaScript execution within the GitLab domain context.

## Description

Once the payload is stored and the server is set up, page reload executes the redirected JS, bypassing CSP as the loads appear as relative but resolve externally. This leads to alerts, token creation, or takeover. Affects all users viewing the issue/wiki.

## Requirements

1. Injected payload saved and visible
2. Attacker server hosting payloads
3. Victim browser on the affected page

## Defense

Defensive measures and detection strategies:

- Post-load DOM scanning for <base> tags
- Enforce CSP nonce or hash for scripts
- Alert on JS execution from unexpected origins

## Objectives

1. Execute JS in victim context
2. Demonstrate domain alert for proof
3. Enable further exploitation like API calls

## Instructions

### Step 1: Reload the Injected Page

**Context**: Force resource reload to trigger redirection.

**Command** ([[commands/trigger-xss-reload]]):

Navigate to the issue URL and press Ctrl+R.

> Watch for network requests to attacker domain. Expected: JS loads and executes.

### Step 2: Verify Execution

**Context**: Confirm with simple payload.

**Command** ([[commands/host-alert-payload]]):

Server serves:

```javascript
alert(document.domain)
```

> Expected: Alert shows 'gitlab.com', proving context.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/host-alert-payload]]

## Tools Used

- [[tools/DevTools]]

## Tags

- execution
- verification
