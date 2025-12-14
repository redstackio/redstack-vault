---
tags:
  - xss
  - dom-xss
  - postmessage
  - poc
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 73a38770-bf61-459b-97dd-c19d2b8b7ef3
created_at: '2025-12-13T23:56:20.053Z'
updated_at: '2025-12-13T23:56:20.053Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Develop PoC for PostMessage XSS

## Summary

This procedure develops a proof-of-concept script to send timed postMessage payloads after form submission, ensuring exploitation before legitimate responses, and bypasses CSP for testing.

## Description

Using SetInterval, the PoC sends payloads repeatedly to the target window. Burp Suite modifies responses to disable CSP, allowing XSS testing in browsers that would otherwise block it.

## Requirements

1. Access to the target form
2. Attacker-controlled site to host the PoC
3. Burp Suite for CSP manipulation

## Defense

Defensive measures and detection strategies:

- Enforce CSP with strict policies
- Rate-limit or validate post-submission messages
- Monitor for rapid postMessage events

## Objectives

1. Create reliable exploitation timing
2. Bypass CSP for PoC
3. Confirm XSS execution

## Instructions

### Step 1: Implement Timed Payload Sender

**Context**: Set up JavaScript to send payloads at intervals.

Use SetInterval to post the crafted message every 250ms to the target window.

```javascript
setInterval(() => {
  targetWindow.postMessage(payload, '*');
}, 250);
```

> Ensures payload arrives before legitimate Marketo response.

### Step 2: Disable CSP with Burp Suite

**Context**: Modify responses to remove CSP headers for testing.

Configure [[tools/Burp-Suite]] with a match and replace rule to remove ^Content-Security-Policy: .*$ from responses.

> Allows javascript: URI execution in the PoC.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[poc]]
- [[xss]]
