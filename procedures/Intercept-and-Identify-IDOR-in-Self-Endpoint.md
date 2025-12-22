---
tags:
  - idor
  - web-vulnerability
  - recon
type: procedure
tools:
  - '[[tools/Firefox-Multi-Account-Containers]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-intercept-self]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:25:23.474Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: c9419e21-bc22-4533-a442-8f75ec163e28
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Intercept-and-Identify-IDOR-in-Self-Endpoint

## Summary

This procedure intercepts the 2FA authentication switch request to identify an IDOR vulnerability in the /self endpoint, allowing unauthorized access to user account parameters.

## Description

In a U.S. Department of Defense social network built on ASP.NET, toggling 2FA triggers a POST to /self with parameters like userName, originalEmail, Email, and RecoveryEmail. These lack proper authorization, enabling IDOR exploitation for account manipulation. This step focuses on discovery via interception, requiring a valid session and tools for traffic monitoring.

## Requirements

1. Authenticated session on the target site
2. Browser with proxy capabilities or extension for request interception
3. Firefox Multi-Account Containers for session isolation

## Defense

Defensive measures and detection strategies:

- Implement server-side ownership checks on user-modifying endpoints
- Log and monitor anomalous parameter values in requests to /self
- Use WAF rules to detect IDOR patterns in POST data

## Objectives

1. Capture and analyze the vulnerable request
2. Confirm lack of authorization on key parameters
3. Prepare for subsequent exploitation steps

## Instructions

### Step 1: Setup Session Isolation

**Context**: Isolate attacker and potential victim sessions to avoid interference during testing.

Use [[tools/Firefox-Multi-Account-Containers]] to create separate containers for different sessions.

### Step 2: Trigger and Intercept Request

**Context**: Perform the 2FA toggle to generate the vulnerable request, then intercept it.

Execute [[commands/curl-intercept-self]] equivalent via proxy or browser dev tools to capture the POST to /self:

```bash
curl -X POST https://target-site.com/self \
  -H "Cookie: session=valid_session" \
  -H "__RequestVerificationToken: token_value" \
  -d "userName=attacker&originalEmail=attacker@example.com&Email=attacker@example.com&RecoveryEmail=attacker@example.com" \
  -v
```

> This command simulates the request; inspect the response and parameters to confirm IDOR (no ownership check).

**Expected Output**: 200 OK response with no validation errors, revealing modifiable fields.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-intercept-self]]

## Tools Used

- [[tools/Firefox-Multi-Account-Containers]]

## Tags

- idor
- web-vulnerability
