---
id: proc-uuid-1
tags:
  - csrf
  - recon
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/test-csrf-endpoint-curl]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:50.206Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-Instacart-CSRF-Vulnerable-Endpoint

## Summary

This procedure involves testing the Instacart admin API endpoint for CSRF protection to confirm it accepts POST requests without token validation, enabling forged zone updates.

## Description

In a web application like Instacart, CSRF vulnerabilities occur when state-changing endpoints do not validate request origins. Here, the /api/v2/zones endpoint updates user zones using 'zip' and 'override' parameters via POST. By inspecting legitimate requests and testing without tokens, attackers confirm exploitability. This targets authenticated users, potentially disrupting delivery services by changing zones to unavailable areas.

## Requirements

1. Access to an authenticated Instacart session (browser or cookie)
2. Web browser with developer tools or curl for testing
3. Knowledge of target endpoint URL

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all POST forms and validate on server
- Use SameSite=Strict cookies to prevent cross-site requests
- Monitor API logs for anomalous zone changes from unexpected referers

## Objectives

1. Confirm absence of CSRF protection on zone update endpoint
2. Identify required parameters for exploitation
3. Validate impact of unauthorized zone changes

## Instructions

### Step 1: Inspect Legitimate Request

**Context**: Perform a real zone update in the Instacart admin interface to capture the request details.

Open browser developer tools (Network tab), change a zone, and note the POST to https://admin.instacart.com/api/v2/zones with parameters zip and override.

**Expected Output**: Request details showing no CSRF token in headers or body.

### Step 2: Test Forged Request

**Context**: Use [[commands/test-csrf-endpoint-curl]] to simulate a cross-site POST without token.

Execute [[commands/test-csrf-endpoint-curl]] to verify the endpoint accepts the request:

```bash
curl -X POST https://admin.instacart.com/api/v2/zones -d "zip=10001&override=true" -b "session_cookie_value"
```

> This command sends a forged POST; replace session_cookie_value with a valid one. Expected output is a success response (e.g., 200 OK) if vulnerable.

### Step 3: Confirm Vulnerability

**Context**: Check if the zone updated without user intent.

Log into the account and verify the zone changed to the test zip code.

**Expected Output**: Zone settings altered to 10001.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/test-csrf-endpoint-curl]]

## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[api]]
