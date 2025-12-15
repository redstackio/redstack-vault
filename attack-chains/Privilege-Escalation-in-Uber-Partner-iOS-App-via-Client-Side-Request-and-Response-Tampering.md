---
tags:
  - privilege-escalation
  - auth-bypass
  - api-tampering
  - mobile-security
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Persistence]]'
verified: false
platforms:
  - iOS
  - Mobile
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Bypass-Uber-Partner-App-Activation-Using-Burp-Suite]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
  - '[[Modify Authentication Process]]'
updated_at: '2025-12-14T17:28:36.544Z'
description: >-
  A multi-step privilege escalation attack that allows non-activated users to
  bypass activation checks in the Uber Partner iOS app by intercepting and
  modifying API requests and responses using Burp Suite.
skill_level: intermediate
impact_level: medium
id: f232ae60-4f1b-42c2-aff8-126d32d6c3bb
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Modify Authentication Process]]'
---
# Privilege Escalation in Uber Partner iOS App via Client-Side Request and Response Tampering

Multi-stage attack chain demonstrating a privilege escalation vulnerability in the Uber Partner iOS app, where non-activated users can bypass activation checks through client-side tampering of API requests and responses.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Download and Install App] --> B[Intercept and Modify Login Request]
    B --> C[Set Up Automated Response Tampering Rule]
    C --> D[Complete Login as Non-Activated User]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- iOS platform with Uber Partner app installed
- Access to the app's backend API services
- Network access to intercept mobile traffic (e.g., via proxy on a connected device)

### Initial Access Requirements

- A non-activated Uber Partner account
- Physical access to an iOS device
- No prior elevated privileges needed, but proxy setup on the device is required

## Detailed Attack Procedures

### Step 1: Download and Install Uber Partner iOS App
procedure: [[procedures/Bypass-Uber-Partner-App-Activation-Using-Burp-Suite]]

**Objective**: Obtain the target application to begin the attack setup.

**Instructions**: Download the official Uber Partner app from the Apple App Store and install it on an iOS device configured to route traffic through a proxy like Burp Suite.

**Expected Output**: App installed and ready for login attempts.

**Success Indicators**:
- App launches successfully without errors
- Proxy interception is confirmed for app traffic

### Step 2: Intercept and Modify Initial Login Request
procedure: [[procedures/Bypass-Uber-Partner-App-Activation-Using-Burp-Suite]]

**Objective**: Tamper with client-side parameters to attempt bypassing activation during login.

**Instructions**: Launch the app, initiate a login with a non-activated account, and use Burp Suite to intercept the login API request. Modify the JSON payload by changing the 'allowNotActivated' parameter from false to true before forwarding the request.

**Expected Output**: Server responds with 'isActivated': false, causing the login to fail initially.

**Success Indicators**:
- Request intercepted and modified successfully
- Server response indicates activation check failure

### Step 3: Configure Match and Replace Rule for Response Tampering
procedure: [[procedures/Bypass-Uber-Partner-App-Activation-Using-Burp-Suite]]

**Objective**: Automate the alteration of server responses to fake activation status.

**Instructions**: In Burp Suite, navigate to the Proxy > Options tab, access the Match and Replace section, and add a new rule for the response body. Set Type to Response body, Match to 'false', and Replace to 'true' to automatically change boolean values in API responses.

**Expected Output**: Rule applied and active for subsequent traffic.

**Success Indicators**:
- Rule saves without errors
- Test interception confirms automatic replacement

### Step 4: Retry Login with Tampered Request and Automated Response Modification
procedure: [[procedures/Bypass-Uber-Partner-App-Activation-Using-Burp-Suite]]

**Objective**: Achieve successful login by combining request modification and response tampering.

**Instructions**: Repeat the login process: intercept the request, set 'allowNotActivated' to true, forward it, and let the match-and-replace rule change the server's 'isActivated': false response to true.

**Expected Output**: App accepts the login, granting access to the interface for non-activated users.

**Success Indicators**:
- Login succeeds without activation prompt
- Access to app features (e.g., dashboard) is granted, though server-side actions like going online remain blocked

## Attack Chain Summary

### Key Achievements

1. Successful bypass of client-side activation checks via parameter tampering
2. Automated response modification to evade server validation
3. Gained unauthorized access to the app interface for non-activated accounts

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Modify Authentication Process]] Modify Authentication Process

### MITRE ATT&CK Tactics

- [[Persistence]] Privilege Escalation

---

*Last updated: 2023-10-01T00:00:00Z*
