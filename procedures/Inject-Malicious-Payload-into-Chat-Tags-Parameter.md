---
tags:
  - xss
  - payload-injection
  - url-manipulation
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:31.960Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: c460dcd0-e778-4dad-ad8f-642d8eaaab91
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject Malicious Payload into Chat Tags Parameter

## Summary

This procedure involves crafting a chat initiation URL for Shopify's live chat with a malicious JavaScript payload embedded in the chat[tags] parameter, exploiting lack of input sanitization to set up a reflected XSS attack.

## Description

The chat[tags] parameter in the URL https://livechat.shopify.com/customer/chats/new is reflected into the page without proper escaping, allowing attackers to inject JavaScript that breaks out of string or array contexts. This is typically used in phishing campaigns where victims are tricked into loading the URL. The payload executes only upon user interaction, such as clicking 'Start chat', in the victim's browser session, enabling theft of cookies, session tokens, or phishing attacks. Prerequisites include public access to the live chat endpoint; no authentication is required.

## Requirements

1. Web browser with developer tools for inspection
2. Knowledge of JavaScript payloads for context-breaking (e.g., closing quotes and semicolons)
3. Valid email and name values for other parameters to mimic legitimate requests

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization for all URL parameters, especially tags
- Use output encoding (e.g., HTML entity encoding) when reflecting parameters into the DOM
- Deploy Content Security Policy (CSP) to restrict inline JavaScript execution
- Monitor for anomalous URL parameters in access logs and block suspicious patterns

## Objectives

1. Embed a JavaScript payload in the chat[tags] parameter without triggering errors
2. Load the page to confirm payload reflection in the source
3. Prepare the environment for payload execution in a subsequent step

## Instructions

### Step 1: Construct the Malicious URL

**Context**: Build a URL that includes legitimate parameters alongside the malicious chat[tags] to evade basic filters and ensure page load.

Use the following URL structure, replacing alert(1) with desired payload:

```url
https://livechat.shopify.com/customer/chats/new?chat%5Bemail%5D=mymail%40mail.com&chat%5Bname%5D=My+Name&utm_source=partner&chat%5Btags%5D=123%27%5D%29;alert%281%29;//&chat%5Bmetadata%5D%5Bshop_id%5D=90909090
```

> The payload "123'"]);alert(1);//" appends to the tags array, closes the string with ', escapes potential quotes with ", closes parentheses and brackets, executes alert(1), and comments out the rest with // to avoid syntax errors.

Copy-paste this into the browser address bar and press Enter.

### Step 2: Verify Payload Reflection

**Context**: Inspect the loaded page to ensure the payload is present and unsanitized.

Open browser developer tools (F12), navigate to the Elements tab, and search for the payload string (e.g., "alert(1)").

> Expected: The payload appears in the HTML source or JavaScript context without encoding, confirming vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[shopify]]
