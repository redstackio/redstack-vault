---
id: proc-uuid-002
name: Create-and-Execute-CSRF-PoC-to-Trigger-XSS
tags:
  - csrf
  - poc
  - xss-injection
type: procedure
tools:
  - '[[tools/Burp-Suite-Professional]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:03.339Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-and-Execute-CSRF-PoC-to-Trigger-XSS

## Summary

This procedure creates a proof-of-concept HTML page using Burp Suite to exploit CSRF and inject XSS into Zomato's contact form.

## Description

A malicious HTML page with a hidden auto-submitting form targets https://www.zomato.com/contact. It includes XSS payloads in name and email fields, along with a static csrf_token. When loaded by a victim, it submits the form cross-origin, injecting scripts that execute on Zomato's page.

## Requirements

1. Burp Suite Professional for PoC generation
2. Web server to host the HTML page
3. Victim's browser session on Zomato

## Defense

Defensive measures and detection strategies:

- Enforce same-site cookies and strict referer checks
- Validate CSRF tokens server-side
- Use Content Security Policy to block inline scripts

## Objectives

1. Force unauthorized form submission
2. Deliver XSS payload to victim's browser
3. Enable client-side JavaScript execution

## Instructions

### Step 1: Generate PoC with Burp Suite

**Context**: Use Burp's CSRF PoC generator to create the HTML.

Capture a legitimate form submission in Burp Repeater, then generate PoC from the request.

> Modify to include payloads: name='<script>alert(1)</script>', email='"<script>alert(document.cookie)</script>', csrf_token='fa53b2d4ea3ae0113d903ed5b0200fcb'.

### Step 2: Host and Execute PoC

**Context**: Serve the HTML and trick victim into loading it.

Host the file on a server (e.g., via Python http.server) and open in victim's browser.

> Expected: Form auto-submits, injecting payloads into Zomato.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Professional]]

## Tags

- [[csrf]]
- [[xss]]
