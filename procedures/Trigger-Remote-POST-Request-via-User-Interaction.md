---
id: uuid-proc-2
tags:
  - user-execution
  - cors
  - post-request
  - csrf
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[User Execution]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:15.680Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[User Execution]]'
  - '[[JavaScript]]'
---
# Trigger-Remote-POST-Request-via-User-Interaction

## Summary

This procedure relies on user interaction with injected HTML to trigger a remote POST request, exploiting jQuery-UJS to include the CSRF token due to malformed URL parsing, effectively bypassing origin checks.

## Description

Once HTML is injected, the user (e.g., victim) clicks the malicious link, initiating an AJAX POST via jQuery-UJS. The space-prefixed URL causes the weak regex in jQuery (and Zepto) to misclassify it as same-origin, attaching the CSRF token. A preflight OPTIONS request is sent first; if the attacker's server responds with permissive CORS, the POST follows with the token in headers. This works in CSP-strict environments as it uses the app's bundled JS.

## Requirements

1. Injected HTML from prior step visible and clickable
2. Attacker server configured for CORS (e.g., Access-Control-Allow-Origin: *)
3. Browser supporting CORS preflights (modern browsers)
4. Active user session with CSRF token

## Defense

Defensive measures and detection strategies:

- Patch jQuery-UJS to version fixing URL parsing (1.1.0+)
- Enforce strict CORS policies on external domains
- Log and alert on unexpected OPTIONS requests from internal users
- Use Content-Security-Policy with report-uri to monitor violations

## Objectives

1. Leverage user click to initiate cross-origin request
2. Ensure token inclusion via framework misparse
3. Complete the request chain without browser blocks

## Instructions

### Step 1: Prepare Attacker Server

**Context**: Set up endpoint to handle OPTIONS and POST, returning CORS headers.

Configure server (e.g., Node.js/Express) to respond to OPTIONS with:

```http
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: POST, OPTIONS
Access-Control-Allow-Headers: X-CSRF-Token
```

For POST, log the `X-CSRF-Token` header.

### Step 2: Induce User Interaction

**Context**: Socially engineer or wait for the victim to interact with the injected element.

The click event triggers jQuery's remote handler: it parses the href, fails to detect cross-origin due to space, and sends POST with token.

### Step 3: Monitor Network Traffic

**Context**: Verify the request sequence in browser dev tools.

Look for OPTIONS to attacker.com (200 OK), followed by POST with token in headers. No errors in console indicate success.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[User Execution]] User Execution
- [[JavaScript]] JavaScript

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[user-execution]]
- [[cors]]
- [[post-request]]
- [[csrf]]
