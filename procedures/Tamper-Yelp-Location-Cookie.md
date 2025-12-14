---
id: proc-tamper-yelp-cookie-001
tags:
  - xss
  - cookie-tampering
  - injection
type: procedure
tools:
  - '[[tools/Chrome-Developer-Tools]]'
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
updated_at: '2025-12-14T03:16:30.975Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Tamper-Yelp-Location-Cookie

## Summary

This procedure modifies the 'city' field in Yelp's URL-encoded JSON location cookie to inject a malicious script payload, such as '<script>debugger</script>', enabling self-XSS when the cookie is later reflected in API responses.

## Description

Yelp's location cookie is client-modifiable and contains JSON with fields like 'city'. By editing this field via developer tools and re-encoding, an attacker can inject HTML/JS payloads. The tampered cookie remains valid for the session, allowing reflection in endpoints like /location_suggest/json without server sanitization. Prerequisites include an active session; outcomes include payload persistence until cookie expiry.

## Requirements

1. Inspected original cookie structure
2. Knowledge of URL encoding for JSON
3. Active Yelp authentication

## Defense

Defensive measures and detection strategies:

- Enforce HttpOnly and Secure flags on sensitive cookies
- Validate and sanitize all cookie-derived inputs server-side
- Use Content Security Policy (CSP) to block inline scripts

## Objectives

1. Inject script into 'city' field
2. Maintain valid JSON structure post-tampering
3. Enable payload reflection in UI interactions

## Instructions

### Step 1: Edit Cookie Value

**Context**: Access and modify the cookie directly in the browser.

In [[tools/Chrome-Developer-Tools]], go to Application > Cookies > yelp.com, select 'location', and edit the value by replacing the 'city' string with '<script>debugger</script>' within the JSON.

### Step 2: Re-encode JSON

**Context**: Ensure the modified JSON is URL-encoded to match the original format.

Update the full JSON to {"city":"<script>debugger</script>","zip":"","country":"US","address2":"","address3":"","state":"CA","address1":"","unformatted":"SanFrancisco,CA"}, then URL-encode it (e.g., %7B%22city%22%3A%22%3Cscript%3Edebugger%3C/script%3E%22%2C...%7D) and save.

**Expected Output**: Cookie updated without session disruption; verify by re-decoding.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome-Developer-Tools]]

## Tags

- xss
- cookie-tampering
- injection
