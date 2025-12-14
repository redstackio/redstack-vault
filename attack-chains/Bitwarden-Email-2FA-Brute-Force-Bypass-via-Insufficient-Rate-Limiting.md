---
tags:
  - brute-force
  - 2fa-bypass
  - rate-limiting
  - authentication
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Bitwarden-Account]]'
  - '[[procedures/Enable-Email-2FA-on-Bitwarden]]'
  - '[[procedures/Initiate-Login-and-Intercept-2FA-Request]]'
  - '[[procedures/Brute-Force-2FA-Code-with-Burp-Intruder]]'
step_count: 4
techniques:
  - '[[Brute Force]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:47.551Z'
description: >-
  Multi-stage attack exploiting weak rate limiting on Bitwarden's email-based
  2FA verification endpoint to brute-force the 6-digit code and achieve account
  takeover.
skill_level: intermediate
impact_level: high
id: e2ee56ce-77de-4a71-a415-92b028135bff
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
  - '[[Exploit Public-Facing Application]]'
---
# Bitwarden Email 2FA Brute-Force Bypass via Insufficient Rate Limiting

Multi-stage attack chain demonstrating a complete attack workflow to bypass email-based 2FA on Bitwarden through brute-forcing the 6-digit code due to insufficient rate limiting on the verification endpoint.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Account Creation] --> B[Enable 2FA]
    B --> C[Initiate Login]
    C --> D[Brute-Force 2FA Code]
    D --> E[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#e67e22
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform (vault.bitwarden.com)
- Required services/ports: HTTPS (443)
- Network access requirements: Direct internet access to Bitwarden

### Initial Access Requirements

- No prior credentials needed; attacker creates a test account
- Email address for 2FA delivery
- Knowledge of target's email and password for real attack

## Detailed Attack Procedures

### Step 1: Account Creation
procedure: [[procedures/Create-Bitwarden-Account]]

**Objective**: Establish a test account to simulate the target environment and enable 2FA setup.

**Instructions**: Navigate to vault.bitwarden.com and register a new account using a controlled email address.

**Expected Output**: Successful account creation with login credentials.

**Success Indicators**:
- Account registered and accessible via email/password
- Confirmation email received

### Step 2: Enable Email 2FA
procedure: [[procedures/Enable-Email-2FA-on-Bitwarden]]

**Objective**: Configure email-based two-factor authentication to expose the vulnerable verification endpoint.

**Instructions**: Log in to the account, navigate to account settings, and enable 2FA with email as the delivery method. A 6-digit code will be sent to the email for initial verification.

**Expected Output**: 2FA enabled; subsequent logins require email code.

**Success Indicators**:
- 2FA status shows as active in settings
- Test login prompts for email code

### Step 3: Initiate Login and Intercept Request
procedure: [[procedures/Initiate-Login-and-Intercept-2FA-Request]]

**Objective**: Trigger the 2FA verification process to capture the request for brute-forcing.

**Instructions**: Log out, then attempt to log in with valid email/password but enter a random invalid 6-digit code to send the verification POST request.

**Expected Output**: 400 Bad Request response for invalid code; request intercepted in proxy tool.

**Success Indicators**:
- Login flow reaches 2FA step
- POST request to verification endpoint captured

### Step 4: Brute-Force 2FA Code
procedure: [[procedures/Brute-Force-2FA-Code-with-Burp-Intruder]]

**Objective**: Exploit weak rate limiting to guess the static 6-digit code within feasible attempts.

**Instructions**: Forward the intercepted request to Burp Intruder, mark the 2FA code parameter, set payload as numeric range 000000-999999, and launch attack. Ignore initial 429 responses; continue until a 200 OK is received indicating valid code.

**Expected Output**: 200 response on correct code; login proceeds to vault access.

**Success Indicators**:
- Valid code guessed within ~1000 attempts
- Full account access granted, compromising vault data

## Attack Chain Summary

### Key Achievements

1. Bypassed email 2FA without legitimate code access
2. Demonstrated account takeover potential for any user with known email/password
3. Highlighted rate limiting flaw allowing ~1000 attempts before success

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Brute Force]] Brute Force
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
