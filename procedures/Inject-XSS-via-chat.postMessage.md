---
tags:
  - xss
  - stored-xss
  - injection
  - rocket-chat
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-rocket-chat-post-message-xss]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e61995f7-faae-4562-a2c5-39b4c26e53c3
created_at: '2025-12-13T23:55:06.265Z'
updated_at: '2025-12-13T23:55:06.265Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Inject-XSS-via-chat.postMessage

## Summary

This procedure exploits a stored XSS vulnerability in Rocket.Chat by posting a message with an attachment containing unencoded HTML/JavaScript in the fields value, leading to execution when viewed by victims.

## Description

The /api/v1/chat.postMessage endpoint fails to encode user-supplied input in attachment fields when an image_url is present, allowing injection of HTML tags like <img> with onload events. The payload is stored and rendered in victims' clients (browsers or apps), executing JS in their context for potential session hijacking or data theft. Requires prior authentication.

## Requirements

1. AuthToken and UserId from successful login
2. Target channel name or RoomId
3. Network access to Rocket.Chat server
4. curl tool

## Defense

Defensive measures and detection strategies:

- Sanitize and HTML-encode all user inputs in attachments (e.g., use libraries like DOMPurify)
- Implement Content Security Policy (CSP) to restrict inline scripts
- Monitor for suspicious message content with JS patterns (e.g., onload, alert)
- Audit attachment rendering in clients

## Objectives

1. Inject and store malicious JavaScript payload
2. Trigger execution upon message view
3. Achieve arbitrary code execution in victim context

## Instructions

### Step 1: Craft and Post Malicious Message

**Context**: Use authenticated headers to post a message with an attachment exploiting the encoding flaw in fields[0].value.

**Command** ([[commands/curl-rocket-chat-post-message-xss]]):
```bash
curl -H "X-Auth-Token: <USER_TOKEN>" -H "X-User-Id: <USER_ID>" http://127.0.0.1:3000/api/v1/chat.postMessage -d "channel=<CHANNEL_NAME>&attachments[0][image_url]=/assets/logo&attachments[0][fields][0][title]=&attachments[0][fields][0][value]=<img src=/assets/logo width=1 height=1 onload=alert('XSS4') />You're Pwned!"
```

> Replace <USER_TOKEN>, <USER_ID>, and <CHANNEL_NAME> with actual values. The payload injects an <img> tag that loads a benign image but executes alert() on onload. Expected output: {"success": true, "message": {...}}. Test by viewing the message in a browser; the alert should fire if vulnerable.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-rocket-chat-post-message-xss]]

## Tools Used

- [[tools/curl]]

## Tags

- xss
- stored-xss
- injection
