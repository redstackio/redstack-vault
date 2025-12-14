---
tags:
  - bruteforce
  - password-reset
  - account-takeover
  - api-vulnerability
  - logic-flaw
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
commands:
  - '[[commands/post-initiate-password-reset]]'
  - '[[commands/get-post-verify-token]]'
  - '[[commands/post-reset-password]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Initiate-Password-Reset-Flow]]'
  - '[[procedures/Bruteforce-SMS-Token-with-Burp-Intruder]]'
  - '[[procedures/Complete-Password-Reset]]'
  - '[[procedures/Bypass-Error-Responses-with-Burp-Suite]]'
step_count: 4
techniques:
  - '[[Brute Force]]'
  - '[[Account Manipulation]]'
  - '[[Exploit Public-Facing Application]]'
description: >-
  Multi-stage attack exploiting weak rate limiting and modifiable responses in
  the password reset flow to bruteforce SMS tokens and takeover staff accounts
  on helpdesk.bistudio.com.
skill_level: intermediate
impact_level: high
id: 18dc10df-7195-4518-8d9b-bcff23092e81
created_at: '2025-12-14T17:33:12.403Z'
updated_at: '2025-12-14T17:33:12.403Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Brute Force]]'
  - '[[Account Manipulation]]'
  - '[[Exploit Public-Facing Application]]'
---
# Staff Account Takeover via Password Reset Token Bruteforce and Response Manipulation

## Overview

This attack chain exploits a logic flaw in the password reset mechanism of helpdesk.bistudio.com, where the API endpoints for verifying 6-digit SMS tokens lack rate limiting, enabling bruteforce attacks. Additionally, HTTP responses can be intercepted and modified to bypass frontend error checks, such as changing 400 Bad Request to 200 OK. Discovered through black-box testing with Burp Suite, this allows an adversary to initiate a reset for a target staff account, bruteforce the token during off-hours, and set a new password, leading to full account takeover. A similar issue exists in the out-of-office email response flow but is less critical.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~30-60 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initiate Reset] --> B[Bruteforce Token]
    B --> C[Bypass Errors]
    C --> D[Reset Password]
    D --> E[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform (helpdesk.bistudio.com)
- AngularJS frontend
- API endpoints accessible via HTTPS
- No specific ports beyond standard 443

### Initial Access Requirements

- Network access to the target domain
- No prior credentials needed
- Ability to intercept traffic (e.g., via proxy)

## Detailed Attack Procedures

### Step 1: Initiate Password Reset
procedure: [[procedures/Initiate-Password-Reset-Flow]]

**Objective**: Trigger the backend to generate and send a 6-digit SMS token to the target's phone.

**Instructions**: Use [[commands/post-initiate-password-reset]] to send a POST request to the verification endpoint with the target username:

```bash
curl -X POST https://helpdesk.bistudio.com/api/system/verification-codes -H "Content-Type: application/json" -d '{"username":"admin"}'
```

**Expected Output**: The backend processes the request and sends an SMS token to the victim's phone; response indicates initiation (may need modification if error).

**Success Indicators**:
- SMS sent to target (confirm via social engineering or timing)
- API response received without blocking

### Step 2: Bruteforce SMS Token
procedure: [[procedures/Bruteforce-SMS-Token-with-Burp-Intruder]]

**Objective**: Enumerate all possible 6-digit tokens to find the valid one before the victim intervenes.

**Instructions**: Configure Burp Suite Intruder to automate requests using [[commands/get-post-verify-token]] for combinations 000000-999999:

```bash
# Example single check (automate in Burp)
curl -X GET https://helpdesk.bistudio.com/api/system/verification-codes/123456
# Or POST if required: curl -X POST https://helpdesk.bistudio.com/api/system/verification-codes/123456 -H "Content-Type: application/json" -d '{}'
```

**Expected Output**: Valid token returns success status; invalid ones may return errors (bypassable in next step).

**Success Indicators**:
- Valid token identified (e.g., 200 OK with success body)
- No rate limiting observed during ~1 million requests

### Step 3: Complete Password Reset
procedure: [[procedures/Complete-Password-Reset]]

**Objective**: Use the bruteforced token to set a new password and takeover the account.

**Instructions**: Send a POST request with the new password and tokens using [[commands/post-reset-password]]:

```bash
curl -X POST https://helpdesk.bistudio.com/api/system/email-account/password -H "Content-Type: application/json" -d '{"password":"NewSecurePass123","code":"BRUTEFORCED_SMS_TOKEN","securityCode":"RETRIEVED_SECURITY_CODE"}'
```

**Expected Output**: Password updated successfully if tokens match; account now controllable.

**Success Indicators**:
- 200 OK response confirming password change
- Login with new password succeeds

### Step 4: Bypass Error Responses
procedure: [[procedures/Bypass-Error-Responses-with-Burp-Suite]]

**Objective**: Manipulate API responses to trick the AngularJS frontend into proceeding despite errors.

**Instructions**: Intercept responses in Burp Suite and modify them during any step, e.g., change status from 400 to 200 and body from {"status":"error"} to {"status":"ok"}. No specific command, but applies to prior curl requests.

**Expected Output**: Frontend accepts the modified response and advances the flow.

**Success Indicators**:
- Flow proceeds without client-side blocks
- ReCAPTCHA or other checks bypassed (not enforced)

## Attack Chain Summary

### Key Achievements

1. Initiated reset without authentication
2. Bruteforced 6-digit token due to no rate limits
3. Bypassed error handling via response tampering
4. Achieved staff account takeover

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Brute Force]] Brute Force
- [[Account Manipulation]] Account Manipulation
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Persistence]] Persistence

---
*Last updated: 2023-10-01*
