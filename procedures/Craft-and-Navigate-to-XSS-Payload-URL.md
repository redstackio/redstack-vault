---
id: proc-craft-xss-url-ie
tags:
  - xss
  - payload-craft
  - url-injection
  - null-byte
type: procedure
tools:
  - '[[tools/Internet-Explorer]]'
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
updated_at: '2025-12-14T03:15:41.522Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-and-Navigate-to-XSS-Payload-URL

## Summary

This procedure involves crafting a malicious URL that exploits insufficient sanitization in the 'action' parameter, using HTML closing tags and null bytes to inject a script tag, then navigating to it in Internet Explorer to trigger JavaScript execution from the location hash.

## Description

The vulnerability in https://owncloud.com/wp-123.php allows reflected XSS only in IE due to its lenient parsing of null bytes in script tags. The payload breaks out of the expected HTML form/div/script context, injects a new script with %00%00 to evade filters, and redirects to execute JS from the #hash fragment, such as alerting the document domain.

## Requirements

1. Configured Internet Explorer instance.
2. Knowledge of the target endpoint (wp-123.php).
3. Ability to construct URLs with encoded payloads.

## Defense

Defensive measures and detection strategies:

- Sanitize and escape user input in URL parameters, rejecting null bytes.
- Use strict HTML encoding for output.
- Deploy Web Application Firewall (WAF) rules to block script injections and null bytes.

## Objectives

1. Deliver the XSS payload via reflected parameter.
2. Bypass any basic filters using IE-specific techniques.
3. Achieve JavaScript injection in the page context.

## Instructions

### Step 1: Construct the Payload

**Context**: Build the URL to close HTML tags and inject the script.

Create the full URL: https://owncloud.com/wp-123.php?action[][]=</form></div></script><script/%00%00v%00%00>document.location.href=location.hash.slice(1)</script>#javascript:alert(document.domain);

> Manual URL crafting. Expected output: Valid URL ready for navigation.

### Step 2: Navigate in IE

**Context**: Deliver the payload to trigger reflection.

Paste the URL into the IE address bar and press Enter.

> Expected output: Page loads, reflecting the 'action' parameter with injected script parsed due to IE's behavior.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Internet-Explorer]]

## Tags

- [[xss]]
- [[payload-craft]]
