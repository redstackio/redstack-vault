---
tags:
  - xss
  - reflection
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite-Professional]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:57.665Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: ee6033ed-d233-45f5-89d6-2792187e7581
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-for-Reflected-XSS-in-HTML-Endpoints

## Summary

This procedure tests for reflected XSS vulnerabilities by sending POST requests to non-existent .html endpoints on echo.urbandictionary.biz, where the server echoes the request body as unsanitized HTML content.

## Description

In the attack scenario, the target is a web service like echo.urbandictionary.biz that handles POST requests to paths ending in .html by reflecting the body in the response with Content-Type: text/html. This allows injection of HTML/JS payloads without sanitization. Prerequisites include network access to the target and a tool like Burp Suite for request manipulation. Expected outcome is confirmation of reflection, setting up for XSS exploitation.

## Requirements

1. Network access to echo.urbandictionary.biz
2. Burp Suite or similar proxy for HTTP testing
3. Basic knowledge of HTTP requests and payloads

## Defense

Defensive measures and detection strategies:

- Implement Content-Type validation and body sanitization on reflected responses
- Use CSP headers to block inline scripts
- Monitor for anomalous POST requests to unusual endpoints

## Objectives

1. Verify server reflection of POST bodies as HTML
2. Identify injectable points for XSS payloads
3. Confirm Content-Type spoofing from text/plain to text/html

## Instructions

### Step 1: Configure Proxy and Intercept Request

**Context**: Set up Burp Suite to intercept traffic and prepare a test POST request to a fabricated .html endpoint.

Launch Burp Suite and configure your browser proxy. Navigate to echo.urbandictionary.biz or directly craft the request in Repeater.

### Step 2: Send Test POST Request

**Context**: Craft and send a POST with a benign payload to observe reflection.

Use Burp Repeater to send:

```http
POST /xsxsxs.html HTTP/1.1
Host: echo.urbandictionary.biz
Content-Type: text/plain
Content-Length: 20

test<payload>here</payload>
```

> The server will respond with 200 OK, Content-Type: text/html, and echo the body, parsing the tags.

### Step 3: Validate Reflection

**Context**: Inspect the response to confirm unsanitized output.

Check if the response body matches the input verbatim and HTML is rendered.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Professional]]

## Tags

- xss
- reflection
- testing
