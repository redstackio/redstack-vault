---
id: ac-romit-pin-bruteforce-001
name: Brute-Force 4-Digit PIN to Access User PII via Operator Wallet in Romit App
type: attack_chain
description: >-
  Multi-stage attack exploiting lack of rate limiting on PIN verification in the
  Romit app to brute-force a 4-digit PIN and gain unauthorized access to victim
  PII added to the attacker's operator wallet.
verified: false
submitted: true
step_count: 4
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:56.244Z'
procedures:
  - '[[procedures/Set-Up-Attacker-Account-on-Romit-App]]'
  - '[[procedures/Initiate-Send-Money-to-Trigger-PIN-Verification]]'
  - '[[procedures/Brute-Force-PIN-Using-Client-Side-Signature-Generation]]'
  - '[[procedures/Access-Disclosed-User-Information-from-Operator-Wallet]]'
techniques:
  - '[[Brute Force]]'
  - '[[Valid Accounts]]'
  - '[[T1213.003]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
tags:
  - brute-force
  - pin-bruteforce
  - information-disclosure
  - pii
  - authentication-bypass
  - web-app
platforms:
  - Web
tools:
  - '[[tools/calSignature-js]]'
  - '[[tools/Burp-Suite]]'
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Brute Force]]'
  - '[[Valid Accounts]]'
  - '[[T1213.003]]'
---

# Brute-Force 4-Digit PIN to Access User PII via Operator Wallet in Romit App

Multi-stage attack chain demonstrating a complete attack workflow exploiting the Romit app's lack of rate limiting on 4-digit PIN verification during login, combined with premature addition of user data to the attacker's operator wallet without full authentication. An attacker with only the victim's phone number can brute-force the PIN client-side using API credentials, gaining access to sensitive PII such as verification documents, email, and DOB.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5-10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Set Up Attacker Account] --> B[Initiate Send Money with Victim Phone]
    B --> C[Brute-Force PIN via API]
    C --> D[Access Victim PII in Operator Wallet]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/calSignature-js]]
- [[tools/Burp-Suite]]

### Target Environment

- Web platform: app.romit.io and api.romit.io
- Required services/ports: HTTPS (443)
- Network access requirements: Internet access to Romit endpoints

### Initial Access Requirements

- No prior credentials needed beyond creating a free attacker account
- Victim's phone number only
- No network position restrictions; public-facing web app

## Detailed Attack Procedures

### Step 1: Set Up Attacker Account
procedure: [[procedures/Set-Up-Attacker-Account-on-Romit-App]]

**Objective**: Create an attacker-controlled account to obtain necessary API credentials for signature generation.

**Instructions**: Navigate to app.romit.io and register a new account using any valid email and phone number. Upon successful registration, note the obtained apiKey, apiSecret, and Location-ID from the account dashboard or browser storage.

**Expected Output**: Attacker account with API credentials (apiKey, apiSecret, Location-ID).

**Success Indicators**:
- Account creation confirmation
- API credentials visible in app or dev tools

### Step 2: Initiate Send Money to Trigger PIN Verification
procedure: [[procedures/Initiate-Send-Money-to-Trigger-PIN-Verification]]

**Objective**: Use the app's 'Send Money' feature to input the victim's phone number, initiating the login/PIN verification process and exposing the /v0/cash/auth/login endpoint.

**Instructions**: Log in to the attacker account, navigate to the 'Send Money' section, and enter the victim's phone number. This triggers a request to /v0/cash/auth/login on api.romit.io, prompting PIN entry without rate limits.

**Expected Output**: API response indicating PIN verification challenge for the victim.

**Success Indicators**:
- Victim phone number accepted
- Login endpoint invoked successfully

### Step 3: Brute-Force PIN Using Client-Side Signature Generation
procedure: [[procedures/Brute-Force-PIN-Using-Client-Side-Signature-Generation]]

**Objective**: Exploit the absence of rate limiting to guess the 4-digit PIN by generating signed requests client-side and sending them repeatedly to the login endpoint.

**Instructions**: Use [[tools/calSignature-js]] to generate authorization signatures for each PIN guess (0000-9999). Configure [[tools/Burp-Suite]] Intruder to automate requests to /v0/cash/auth/login with varying PIN payloads. Example signature generation: Load calSignature.js and call the signing function with apiKey, apiSecret, Location-ID, and guessed PIN. Send POST requests like:

```bash
curl -X POST https://api.romit.io/v0/cash/auth/login \
  -H "Authorization: Bearer <signed_token>" \
  -d '{"phone":"+1VICTIM_PHONE","pin":"GUESS_PIN"}'
```

**Expected Output**: Successful response (200 OK) on correct PIN, indicating authentication success.

**Success Indicators**:
- Rate limiting absent (unlimited requests)
- Valid signature accepted for correct PIN

### Step 4: Access Disclosed User Information from Operator Wallet
procedure: [[procedures/Access-Disclosed-User-Information-from-Operator-Wallet]]

**Objective**: Retrieve the victim's sensitive PII automatically added to the attacker's operator wallet post-PIN success, without additional SMS/GA verification.

**Instructions**: After successful PIN brute-force, refresh the operator wallet view in the app or query the relevant API endpoint to view added user profile. The data includes verification documents, email, DOB, and other PII.

**Expected Output**: Victim's profile details visible in attacker's wallet.

**Success Indicators**:
- User info added without further auth
- PII (docs, email, DOB) accessible

## Attack Chain Summary

### Key Achievements

1. Created attacker account to obtain API credentials for signature generation.
2. Triggered PIN verification via 'Send Money' without restrictions.
3. Brute-forced 4-digit PIN (up to 10,000 attempts) due to no rate limiting.
4. Gained full PII access via premature wallet addition.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Brute Force]] Brute Force
- [[Valid Accounts]] Valid Accounts
- [[T1213.003]] Data from Web Service

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery
- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
