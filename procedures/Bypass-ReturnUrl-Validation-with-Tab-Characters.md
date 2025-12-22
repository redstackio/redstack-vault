---
tags:
  - xss
  - bypass
  - tab-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: e85d625b-7fcb-460c-9785-e0c4959be442
created_at: '2025-12-13T23:52:21.125Z'
updated_at: '2025-12-13T23:52:21.125Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Bypass-ReturnUrl-Validation-with-Tab-Characters

## Summary

This procedure crafts a malicious URL for the Starbucks sign-in page by encoding a JavaScript payload with tab characters (%09) to bypass validation filters on the ReturnUrl parameter, embedding the payload without triggering immediate detection.

## Description

The ReturnUrl parameter on https://app.starbucks.com/account/signin is vulnerable to DOM-based XSS due to inadequate sanitization of control characters (hex 00-1F). By inserting tab characters, attackers split keywords like 'javascript' to evade blacklists, allowing injection of payloads like 'javascript:alert(document.domain)'. This sets up execution upon DOM processing during sign-in. Prerequisites include a web browser and knowledge of URL encoding; no special access is needed beyond tricking a victim to visit the link.

## Requirements

1. Web browser for URL construction and navigation
2. Victim interaction (e.g., phishing link delivery)
3. Basic URL encoding knowledge (e.g., %09 for tab)

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation and sanitization, rejecting control characters
- Use Content Security Policy (CSP) to block inline JavaScript execution
- Monitor for unusual ReturnUrl patterns in logs, such as encoded tabs

## Objectives

1. Embed JavaScript payload in the sign-in page DOM without validation blocks
2. Prepare for payload execution on user interaction
3. Enable subsequent cookie theft

## Instructions

### Step 1: Construct Malicious URL

**Context**: Build the URL by inserting tab characters (%09) around sensitive keywords to bypass filters.

No command required; manually construct in browser address bar or via URL shortener.

Example URL:

```url
https://app.starbucks.com/account/signin?ReturnUrl=%09Jav%09ascript:alert(document.domain)
```

> This encodes 'Jav	ascript:alert(document.domain)' where \t is the tab, splitting 'javascript' to evade detection. Visit the URL to load the page.

### Step 2: Verify Payload Embedding

**Context**: Inspect the page to confirm the payload is in the DOM but not executed yet.

Open browser developer tools (F12), navigate to the sign-in page, and search for the ReturnUrl value in the source.

**Expected Output**: Payload visible in URL parameters or DOM elements handling redirects, without errors.

> Success confirms bypass; if blocked, try other control characters like %00 or %0A.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[bypass]]
- [[injection]]
