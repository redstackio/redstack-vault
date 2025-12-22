---
tags:
  - otp-leak
  - information-disclosure
  - account-takeover
  - api-vulnerability
  - mtn-group
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Initiate-Insurance-Quote-Authentication]]'
  - '[[procedures/Intercept-OTP-Request-Traffic]]'
  - '[[procedures/Extract-OTP-from-API-Response]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Sniffing]]'
updated_at: '2025-12-14T17:32:48.222Z'
description: >-
  Multi-stage attack exploiting OTP leakage in the MTN Group device insurance
  quote API, allowing interception of one-time passwords for unauthorized
  account access.
skill_level: intermediate
impact_level: high
id: 5ff75b8b-d73e-4152-add9-459601451866
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Sniffing]]'
---
# OTP Code Leakage in MTN Group API Response Enabling Account Takeover

Multi-stage attack chain demonstrating the exploitation of an information disclosure vulnerability in the MTN Group mobile application's device insurance quote process, where OTP codes are leaked in API responses, allowing attackers to bypass authentication and achieve account takeover without physical access to the victim's device.

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
    A[Initiate Quote Process] --> B[Intercept Traffic]
    B --> C[Extract OTP]
    C --> D[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform (MTN Group customer insurance portal at https://corporate.admyntec.co.za/customerInsurance)
- Required services/ports: HTTPS (443)
- Network access requirements: Ability to access the public-facing web application and intercept HTTP traffic

### Initial Access Requirements

- No prior credentials needed
- Attacker must be able to submit arbitrary valid MTN phone numbers
- Proxy setup for traffic interception

## Detailed Attack Procedures

### Step 1: Initiate Quote Process
procedure: [[procedures/Initiate-Insurance-Quote-Authentication]]

**Objective**: Trigger the OTP authentication flow by starting the device insurance quote process with a target phone number.

**Instructions**: Navigate to the customer insurance page and begin the quote request by entering a valid MTN phone number. This initiates the API call for OTP generation.

**Expected Output**: The application prompts for OTP verification after submitting the phone number.

**Success Indicators**:
- Phone number submission accepted
- OTP sent to the target device (though not received by attacker yet)

### Step 2: Intercept Traffic
procedure: [[procedures/Intercept-OTP-Request-Traffic]]

**Objective**: Set up traffic interception to capture the API response containing the leaked OTP.

**Instructions**: Configure a proxy tool to intercept all HTTP/HTTPS traffic from the browser or application. Submit the phone number and monitor the outgoing request to the authentication endpoint.

**Expected Output**: Captured request and response packets, including the API call for OTP.

**Success Indicators**:
- Traffic successfully intercepted
- API request to phone number submission endpoint visible

### Step 3: Extract OTP
procedure: [[procedures/Extract-OTP-from-API-Response]]

**Objective**: Analyze the intercepted API response to obtain the OTP code and use it for unauthorized authentication.

**Instructions**: Inspect the response body of the OTP request API call to locate the leaked OTP value. Use the OTP to complete sign-up or login on the target account.

**Expected Output**: OTP code visible in the JSON response body, enabling immediate use for authentication.

**Success Indicators**:
- OTP code extracted without errors
- Successful account login or sign-up using the intercepted OTP

## Attack Chain Summary

### Key Achievements

1. Bypassed two-factor authentication via API leakage
2. Enabled unauthorized access to any MTN user's account using only their phone number
3. Demonstrated potential for mass account takeover without physical device access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Network Sniffing]] Network Sniffing

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Credential Access]] Credential Access
- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
