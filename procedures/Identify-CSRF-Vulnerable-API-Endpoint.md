---
tags:
  - csrf
  - api-testing
  - vulnerability-identification
type: procedure
tools: []
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
updated_at: '2025-12-14T17:27:42.573Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: c5c1637c-5c6d-45c3-b10e-0dc2e85217f3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-CSRF-Vulnerable-API-Endpoint

## Summary

This procedure involves testing a web API endpoint to confirm the absence of CSRF protections and improper validation of authentication parameters, specifically session_id in POST requests.

## Description

In the context of the Unikrn raffle entry API, this step tests the POST endpoint at https://unikrn.com/apiv2/raffle/enter by sending requests with missing or empty session_id parameters. The endpoint relies solely on cookies for authentication, ignoring the session_id, which enables CSRF attacks. This is a reconnaissance step to validate the vulnerability before crafting exploits.

## Requirements

1. Access to a web browser or API client (e.g., curl, Postman)
2. Knowledge of the target endpoint URL and parameters (raffle ID, tickets count)
3. Optional: Authenticated session cookies for testing legitimacy

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing POST endpoints
- Enforce strict validation of session_id parameters alongside cookie auth
- Use Content-Security-Policy (CSP) headers to restrict cross-origin requests
- Monitor for anomalous POST requests from unexpected referers

## Objectives

1. Confirm lack of CSRF token requirement
2. Verify session_id is not enforced for authentication
3. Identify potential for cookie-based auth bypass

## Instructions

### Step 1: Prepare Test Request

**Context**: Set up a POST request to the endpoint with standard parameters but omit session_id.

Use a tool like curl to simulate the request:

```bash
curl -X POST https://unikrn.com/apiv2/raffle/enter \
     -H "Cookie: session=your_session_cookie" \
     -d "raffle=4775" \
     -d "tickets=1"
```

> This command sends the request without session_id. Expected output: Success response indicating raffle entry, confirming vulnerability.

### Step 2: Test with Empty session_id

**Context**: Explicitly include an empty session_id to check if it's ignored.

```bash
curl -X POST https://unikrn.com/apiv2/raffle/enter \
     -H "Cookie: session=your_session_cookie" \
     -d "raffle=4775" \
     -d "tickets=1" \
     -d "session_id="
```

> Expected output: Same success as before, proving no validation occurs.

### Step 3: Verify No CSRF Token Needed

**Context**: Attempt the request without any anti-CSRF measures.

Repeat the curl command without additional tokens. If it succeeds repeatedly, the endpoint is vulnerable.

> Success: No error for missing tokens; request processes normally.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[api-endpoint]]
- [[vulnerability-scan]]
