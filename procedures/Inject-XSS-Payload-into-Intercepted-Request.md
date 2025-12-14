---
id: proc-inject-xss-payload-001
tags:
  - xss
  - self-xss
  - payload-injection
  - javascript
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:37.256Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload into Intercepted Request

## Summary

This procedure modifies the intercepted HTTP request by appending a crafted JavaScript payload to the URL, exploiting the reflection in the Nextcloud about page's HTML output.

## Description

The payload `</title>"><script>alert(205)</script>'"><marquee><h1>nextcloud.com</h1></marquee>'` breaks out of HTML contexts like the title tag and injects executable JavaScript. Due to improper sanitization, it reflects directly into the page, leading to self-XSS execution in the attacker's browser.

## Requirements

1. Intercepted request visible in Burp Suite
2. Knowledge of the vulnerable reflection point (URL parameters)
3. Basic understanding of HTML/JS context breaking

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs from URLs in HTML output
- Deploy WAF rules to block common XSS payloads
- Monitor for alert() or unusual script tags in logs

## Objectives

1. Craft and insert the payload without breaking the request
2. Target the unsanitized URL reflection
3. Prepare for execution in the browser context

## Instructions

### Step 1: Edit Request URL

**Context**: Locate the URL in the intercepted GET request and append the payload.

No specific command; in Burp's Raw or Inspector view, modify the path to include `/about/')</title>"><script>alert(205)</script>'"><marquee><h1>nextcloud.com</h1></marquee>'`.

> Expected output: Updated request shows the payload in the URL field.

### Step 2: Validate Payload Syntax

**Context**: Ensure the payload doesn't cause parsing errors.

No specific command; preview the request in Burp.

> Expected output: No HTTP errors; payload intact.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[self-xss]]
- [[payload-injection]]
- [[JavaScript]]
