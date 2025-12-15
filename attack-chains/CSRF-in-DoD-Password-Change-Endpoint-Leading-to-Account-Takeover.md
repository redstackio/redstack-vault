---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: CSRF in DoD Password Change Endpoint Leading to Account Takeover
tags:
  - csrf
  - account-takeover
  - web-vulnerability
  - dod
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
verified: false
platforms:
  - Web
  - IIS
submitted: true
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Authenticate-to-DoD-Website]]'
  - '[[procedures/Access-Password-Change-Feature]]'
  - '[[procedures/Intercept-Password-Change-Request-with-Burp-Suite]]'
  - '[[procedures/Craft-and-Deliver-CSRF-Proof-of-Concept]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:11.973Z'
description: >-
  A multi-step attack exploiting a CSRF vulnerability in the U.S. Department of
  Defense website's password change functionality, enabling unauthorized account
  takeover by forging password reset requests.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# CSRF in DoD Password Change Endpoint Leading to Account Takeover

Multi-stage attack chain demonstrating a complete attack workflow exploiting CSRF in a government web application for account takeover.

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
    A[Initial Access: Authenticate] --> B[Discovery: Intercept Request]
    B --> C[Execution: Craft CSRF PoC]
    C --> D[Impact: Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform hosted on IIS
- Access to https://███.mil/
- Valid credentials for initial authentication

### Initial Access Requirements

- Attacker must have valid DoD credentials to observe legitimate flow
- Victim must be authenticated to the target site
- Network access to the target domain

## Detailed Attack Procedures

### Step 1: Authenticate to Target Website
procedure: [[procedures/Authenticate-to-DoD-Website]]

**Objective**: Gain an authenticated session to the DoD website to prepare for request interception.

**Instructions**: Access the target URL and log in using valid credentials.

**Expected Output**: Successful login redirect to the authenticated dashboard.

**Success Indicators**:
- Authentication token in session cookies
- Access to user-specific features

### Step 2: Access Password Change Feature
procedure: [[procedures/Access-Password-Change-Feature]]

**Objective**: Navigate to the password change interface to trigger the vulnerable request.

**Instructions**: Within the authenticated session, locate and select the password change option.

**Expected Output**: Password change form loads with input fields for new credentials.

**Success Indicators**:
- Form visible and editable
- No immediate errors on navigation

### Step 3: Intercept Password Change Request with Burp Suite
procedure: [[procedures/Intercept-Password-Change-Request-with-Burp-Suite]]

**Objective**: Capture the legitimate POST request parameters for replication in the CSRF attack.

**Instructions**: Configure Burp Suite to intercept traffic, submit a test password change, and analyze the captured request.

**Expected Output**: Detailed POST request including parameters like GETPW2, Y, p (password), q (email), X.

**Success Indicators**:
- Request intercepted successfully
- All form parameters visible and modifiable

### Step 4: Craft and Deliver CSRF Proof of Concept
procedure: [[procedures/Craft-and-Deliver-CSRF-Proof-of-Concept]]

**Objective**: Create a malicious HTML form that forges the password change and deliver it to the victim.

**Instructions**: Build an HTML page with a hidden form auto-submitting to the endpoint, then host and link it to the victim.

**Expected Output**: Victim's password changed to attacker-controlled value upon link visit while authenticated.

**Success Indicators**:
- Form submission alters victim account
- Attacker gains access with new credentials

## Attack Chain Summary

### Key Achievements

1. Identified missing CSRF tokens in password reset endpoint
2. Captured and replicated legitimate request parameters
3. Demonstrated full account takeover via social engineering
4. Highlighted critical impact on government systems

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Persistence]]

---

*Last updated: 2023-10-01T12:00:00Z*
