---
id: ac-otp-bypass-ato-mtn
tags:
  - authentication-bypass
  - account-takeover
  - idor
  - otp-bypass
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Caido]]'
tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Register-Account-and-Add-Uncontrolled-MSISDN]]'
  - '[[procedures/Bypass-OTP-Verification-via-Response-Manipulation]]'
  - '[[procedures/Achieve-Account-Takeover-and-Access-Features]]'
  - '[[procedures/Exploit-IDOR-for-Transaction-History]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:33:24.563Z'
description: >-
  Multi-stage attack exploiting OTP verification bypass and IDOR on shop.mtn.ng
  to add uncontrolled mobile numbers, achieve account takeover, and access
  transaction history.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
---
# OTP Verification Bypass Leading to Account Takeover on MTN Shop

Multi-stage attack chain demonstrating a complete workflow to bypass OTP verification on the MTN Shop platform (shop.mtn.ng), add an uncontrolled mobile number (MSISDN) to the attacker's account, achieve full account takeover (ATO), and exploit an Insecure Direct Object Reference (IDOR) to view the victim's transaction history. This vulnerability stems from a lack of server-side validation on OTP responses, allowing attackers to manipulate HTTP responses and gain unauthorized access to personal data, account settings, and financial transactions.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Account Setup and MSISDN Addition] --> B[OTP Bypass via Response Manipulation]
    B --> C[Account Takeover and Access]
    C --> D[IDOR Exploitation for Data Exfiltration]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- [[tools/Caido]]

### Target Environment

- Web platform: shop.mtn.ng
- Required services/ports: HTTPS (443)
- Network access requirements: Direct internet access to the target site

### Initial Access Requirements

- No prior credentials needed; attacker creates a new account
- Valid Nigerian MSISDN (obtain from numverify.com or similar)
- Proxy tool configured to intercept traffic

## Detailed Attack Procedures

### Step 1: Account Setup and MSISDN Addition
procedure: [[procedures/Register-Account-and-Add-Uncontrolled-MSISDN]]

**Objective**: Create an attacker account and add a victim's uncontrolled mobile number to enable linking.

**Instructions**: Navigate to shop.mtn.ng, access the account section, and input details including a bogus MSISDN.

**Expected Output**: MSISDN added to account profile, prompting for OTP verification.

**Success Indicators**:
- Account created successfully
- MSISDN field populated and save button clickable
- OTP request triggered

### Step 2: OTP Bypass via Response Manipulation
procedure: [[procedures/Bypass-OTP-Verification-via-Response-Manipulation]]

**Objective**: Intercept the OTP verification request and modify the response to simulate success with an invalid OTP.

**Instructions**: Use a proxy like [[tools/Burp-Suite]] to capture the POST request to /mtn_otp/index/verification/, enter invalid OTP, and alter the JSON response from failure to success.

**Expected Output**: Client-side verification passes, linking the MSISDN without actual OTP.

**Success Indicators**:
- Modified response forwarded with {"status":200,"msisdn":"[redacted]","success":true}
- No error message; account updates reflect the new MSISDN

### Step 3: Account Takeover and Access Features
procedure: [[procedures/Achieve-Account-Takeover-and-Access-Features]]

**Objective**: Leverage the bypassed verification to gain full control over the victim's account.

**Instructions**: Post-bypass, access account management to view/modify personal info, settings, and initiate transactions.

**Expected Output**: Full access to victim's data and functions as if authenticated.

**Success Indicators**:
- Personal details (names, email) visible and editable
- Transaction initiation possible without further auth

### Step 4: IDOR Exploitation for Transaction History
procedure: [[procedures/Exploit-IDOR-for-Transaction-History]]

**Objective**: View sensitive transaction details of the linked MSISDN due to improper access controls.

**Instructions**: Navigate to Manage Account > Transaction History to retrieve data tied to the foreign MSISDN.

**Expected Output**: List of victim's transactions exposed.

**Success Indicators**:
- Transaction history loads without ownership checks
- Financial details (dates, amounts, types) visible

## Attack Chain Summary

### Key Achievements

1. Bypassed OTP verification to link uncontrolled MSISDN
2. Achieved full account takeover with access to personal and financial functions
3. Exploited IDOR to exfiltrate transaction history

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Valid Accounts]]
- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Lateral Movement]]
- [[Discovery]]

---

*Last updated: 2023-10-01T00:00:00Z*
