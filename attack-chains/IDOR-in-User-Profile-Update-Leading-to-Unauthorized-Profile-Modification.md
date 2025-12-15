---
tags:
  - idor
  - web
  - authorization-bypass
  - profile-modification
  - account-takeover
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Mozilla-Firefox]]'
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Create-Test-Accounts-for-IDOR-Testing]]'
  - '[[procedures/Capture-Attacker-Profile-Update-Request]]'
  - '[[procedures/Record-Attacker-Identifiers-and-Logout]]'
  - '[[procedures/Capture-Victim-Profile-Update-Request]]'
  - '[[procedures/Exploit-IDOR-by-Modifying-Victims-Profile]]'
  - '[[procedures/Verify-Unauthorized-Profile-Modification]]'
step_count: 6
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Multi-stage attack exploiting an Insecure Direct Object Reference (IDOR)
  vulnerability in the MTN Group application's user profile update endpoint,
  allowing authenticated users to modify any other user's profile details.
skill_level: intermediate
impact_level: high
id: 4f0bcf1b-7c7d-4416-9954-e503fa38b0bc
created_at: '2025-12-14T17:25:47.577Z'
updated_at: '2025-12-14T17:25:47.577Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# IDOR in User Profile Update Leading to Unauthorized Profile Modification

Multi-stage attack chain demonstrating exploitation of an Insecure Direct Object Reference (IDOR) in the MTN Group application's POST /app/updateUser endpoint, enabling unauthorized modification of user profiles for impersonation or account takeover.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Test Accounts] --> B[Capture Attacker Request]
    B --> C[Record Identifiers]
    C --> D[Capture Victim Request]
    D --> E[Modify and Forward Request]
    E --> F[Verify Modification]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#f39c12
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- [[tools/Mozilla-Firefox]]
- [[tools/Google-Chrome]]

### Target Environment

- Web application at https://mtnmobad.mtnbusiness.com.ng
- Authenticated access to the application
- No specific ports or services beyond standard HTTPS (443)

### Initial Access Requirements

- Valid attacker credentials for the MTN Group app
- Valid victim credentials for verification (test accounts recommended)
- Network access to the target URL
- Burp Suite configured as a proxy for both browsers

## Detailed Attack Procedures

### Step 1: Setup Test Accounts
procedure: [[procedures/Create-Test-Accounts-for-IDOR-Testing]]

**Objective**: Establish attacker and victim test accounts to simulate the IDOR exploitation scenario.

**Instructions**: Use [[tools/Mozilla-Firefox]] to access the login page and create accounts.

**Expected Output**: Successful authentication for the attacker account.

**Success Indicators**:
- Attacker logged in successfully
- Victim account created for later use

### Step 2: Capture Attacker Profile Update Request
procedure: [[procedures/Capture-Attacker-Profile-Update-Request]]

**Objective**: Intercept the profile update request from the attacker's session to understand the payload structure.

**Instructions**: Navigate to the profile page in Firefox with Burp proxy enabled to capture the POST request.

**Expected Output**: Captured JSON payload containing 'id' and 'email' fields.

**Success Indicators**:
- POST /app/updateUser request intercepted
- Payload includes predictable user identifiers

### Step 3: Record Attacker Identifiers and Logout
procedure: [[procedures/Record-Attacker-Identifiers-and-Logout]]

**Objective**: Extract the attacker's user 'id' and 'email' for comparison and log out to prepare for victim session.

**Instructions**: Note the values from the captured JSON in Burp Suite, then log out of the attacker session.

**Expected Output**: Recorded identifiers like 'id': '/###', 'email': 'redacted+attacker@wearehackerone.com'.

**Success Indicators**:
- Identifiers documented
- Session logged out cleanly

### Step 4: Capture Victim Profile Update Request
procedure: [[procedures/Capture-Victim-Profile-Update-Request]]

**Objective**: Obtain the victim's user 'id' and 'email' by repeating the capture process in a separate browser.

**Instructions**: Use [[tools/Google-Chrome]] with Burp proxy to log in as victim, visit profile, and capture the request.

**Expected Output**: Victim's JSON payload with 'id': '/redacted', 'email': 'redacted+victim@wearehackerone.com'.

**Success Indicators**:
- Victim identifiers recorded
- Logout from victim session

### Step 5: Exploit IDOR by Modifying Victim's Profile
procedure: [[procedures/Exploit-IDOR-by-Modifying-Victims-Profile]]

**Objective**: From the attacker's authenticated session, alter the update request to target the victim's profile.

**Instructions**: In Firefox (attacker session), intercept the request in Burp, replace 'id' and 'email' with victim's values, and forward.

**Expected Output**: Modified request sent successfully without errors.

**Success Indicators**:
- Request forwarded with victim's identifiers
- No authorization denial from the server

### Step 6: Verify Unauthorized Profile Modification
procedure: [[procedures/Verify-Unauthorized-Profile-Modification]]

**Objective**: Confirm the profile changes in the victim's session to validate the IDOR exploitation.

**Instructions**: In Chrome (victim session), refresh the profile page to observe updates.

**Expected Output**: Victim's profile shows changes like updated username, address, mobile number.

**Success Indicators**:
- Unauthorized modifications visible
- Potential for impersonation confirmed

## Attack Chain Summary

### Key Achievements

1. Successful IDOR exploitation allowing cross-user profile updates
2. No server-side authorization checks bypassed
3. Demonstrated risk of account takeover via profile manipulation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---

*Last updated: 2023-10-01*
