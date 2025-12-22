---
id: ac-idor-ato-001
tags:
  - idor
  - account-takeover
  - web-vulnerability
  - ato
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Foxy-Proxy]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-Attacker-and-Victim-Accounts]]'
  - '[[procedures/Intercept-and-Analyze-Profile-Update-Request]]'
  - '[[procedures/Enumerate-Victims-User-ID]]'
  - '[[procedures/Exploit-IDOR-to-Modify-Victim-Profile]]'
  - '[[procedures/Perform-Account-Takeover-via-Login]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:33:06.661Z'
description: >-
  Multi-stage attack exploiting an Insecure Direct Object Reference (IDOR)
  vulnerability in the user profile editing endpoint to perform unauthorized
  email changes, enabling full account takeover without user interaction.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
---
# IDOR in User Profile Editing Leading to Full Account Takeover

Multi-stage attack chain demonstrating exploitation of an IDOR vulnerability in the /EditUserProfile/Save endpoint of an ASP.NET Core web application, allowing unauthorized modification of other users' profiles to change emails and achieve full account takeover.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Account Setup] --> B[Request Interception]
    B --> C[User ID Enumeration]
    C --> D[Profile Modification]
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
- [[tools/Foxy-Proxy]]

### Target Environment

- Web application built on ASP.NET Core
- Accessible login and profile editing pages
- No specific ports required beyond standard HTTPS (443)

### Initial Access Requirements

- Ability to register new accounts
- Valid network access to the target URL (e.g., https://target.com)
- Attacker credentials for authentication

## Detailed Attack Procedures

### Step 1: Account Setup
procedure: [[procedures/Setup-Attacker-and-Victim-Accounts]]

**Objective**: Create attacker and victim accounts to establish baseline for exploitation.

**Instructions**: Navigate to the login/registration page and register two accounts: one for the attacker and one simulating the victim. Use distinct emails like attacker@gmail.com and victim@gmail.com.

**Expected Output**: Successful registration confirmations for both accounts.

**Success Indicators**:
- Attacker account created and login successful
- Victim account created with known email

### Step 2: Request Interception and Analysis
procedure: [[procedures/Intercept-and-Analyze-Profile-Update-Request]]

**Objective**: Login as attacker, update profile, and intercept the request to identify the static userId parameter.

**Instructions**: Login with attacker credentials, go to My Account, update email or other fields, enable Foxy Proxy to route through Burp Suite, and intercept the POST to /EditUserProfile/Save. Observe the userId parameter (e.g., userId=123464).

**Expected Output**: Intercepted request showing userId tied to attacker's account.

**Success Indicators**:
- Request captured with userId visible
- Parameter remains static when modifying fields

### Step 3: Enumerate Victim's User ID
procedure: [[procedures/Enumerate-Victims-User-ID]]

**Objective**: Login as victim/test account and intercept a profile update to obtain the victim's userId.

**Instructions**: Login with victim credentials, update profile, enable Foxy Proxy, intercept in Burp Suite to note userId (e.g., userId=123465).

**Expected Output**: Intercepted request revealing victim's userId.

**Success Indicators**:
- Victim's userId captured (e.g., 123465)
- Request structure matches attacker's for consistency

### Step 4: Exploit IDOR for Profile Modification
procedure: [[procedures/Exploit-IDOR-to-Modify-Victim-Profile]]

**Objective**: Modify the intercepted request to target victim's userId and change email to attacker's.

**Instructions**: In Burp Suite, alter the userId to victim's (123465), set Email=attacker@gmail.com, and forward the POST request.

**Expected Output**: Server response indicating successful profile update (e.g., 200 OK or redirect).

**Success Indicators**:
- No authorization error
- Victim's email updated to attacker's

### Step 5: Account Takeover
procedure: [[procedures/Perform-Account-Takeover-via-Login]]

**Objective**: Login to victim's account using attacker's email and credentials.

**Instructions**: Attempt login with victim's original email but attacker's password; since email is now attacker's, it authenticates successfully.

**Expected Output**: Access to victim's account dashboard.

**Success Indicators**:
- Login succeeds without victim's password
- Full access to victim's data and actions

## Attack Chain Summary

### Key Achievements

1. Unauthorized profile modification via IDOR
2. Email hijacking without interaction
3. Complete account takeover enabling data access and further abuse

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Valid Accounts]] Valid Accounts
- [[Account Discovery]] Account Discovery

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery

---
*Last updated: 2023-10-01T00:00:00Z*
