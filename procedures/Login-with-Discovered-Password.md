---
id: proc-login-discovered-pw
tags:
  - authentication
  - account-takeover
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:52.776Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-with-Discovered-Password

## Summary

This procedure uses the brute-forced password to authenticate to the target account, confirming unauthorized access without additional verification.

## Description

With the discovered password 'Geniaal2!!', perform a standard login to the /sessions endpoint. In the HackerOne case, this granted full access to the test account, exposing confidential bug reports, as no post-auth checks were in place.

## Requirements

1. Discovered password
2. Target username
3. Access to login endpoint

## Defense

Defensive measures and detection strategies:

- Require 2FA or email verification on login
- Alert on logins from new IPs/locations
- Log all successful logins with failed attempt history

## Objectives

1. Authenticate using compromised credentials
2. Verify full account access
3. Access sensitive data (e.g., bug reports)

## Instructions

### Step 1: Perform Login

**Context**: Send POST with username and password.

No specific command; use browser or curl:

```bash
curl -X POST https://hackerone.com/sessions -d 'login=██████████&password=Geniaal2!!' -c cookies.txt
```

> Expected: Successful response with session cookie, no blocks.

### Step 2: Validate Access

**Context**: Navigate to protected areas.

Use session to access account dashboard.

> Expected: View confidential reports, confirming compromise.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authentication]]
- [[account-takeover]]
