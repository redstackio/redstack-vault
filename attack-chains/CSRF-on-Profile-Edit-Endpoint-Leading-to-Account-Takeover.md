---
id: ac-2712857-csrf-account-takeover
tags:
  - csrf
  - account-takeover
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Register-and-Authenticate-Account]]'
  - '[[procedures/Analyze-Profile-Edit-Endpoint-with-Burp-Suite]]'
  - '[[procedures/Exploit-CSRF-for-Account-Takeover]]'
step_count: 6
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:24.502Z'
description: >-
  A multi-stage attack exploiting a CSRF vulnerability in the account profile
  edit endpoint to achieve full account takeover by changing username, email,
  and password without user interaction.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# CSRF on Profile Edit Endpoint Leading to Account Takeover

Multi-stage attack chain demonstrating a complete attack workflow exploiting CSRF to takeover user accounts.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Account Registration and Login] --> B[Endpoint Analysis]
    B --> C[CSRF Identification]
    C --> D[POC Exploitation]
    D --> E[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web application with account management features
- Accessible registration and login endpoints
- No email verification enforced for login

### Initial Access Requirements

- Public access to the target domain
- Ability to register a test account
- Victim must be authenticated in the browser

## Detailed Attack Procedures

### Step 1: Register a New Account
procedure: [[procedures/Register-and-Authenticate-Account]]

**Objective**: Create a test account to simulate victim authentication and access profile features.

**Instructions**: Navigate to the registration endpoint and provide required details.

Access https://target.com/account/register in a browser and fill in username, password, and other fields, then submit the form.

**Expected Output**: Successful registration confirmation, account created without email verification.

**Success Indicators**:
- Account registration succeeds
- No immediate verification required

### Step 2: Log In to the Account
procedure: [[procedures/Register-and-Authenticate-Account]]

**Objective**: Authenticate as the test user to enable session-based interactions with protected endpoints.

**Instructions**: Use the registered credentials to log in directly.

Visit https://target.com/login, enter the username and password, and submit.

**Expected Output**: Successful login, session established.

**Success Indicators**:
- Dashboard or profile page loads
- Authentication cookie set

### Step 3: Navigate to Profile Edit and Attempt Modifications
procedure: [[procedures/Analyze-Profile-Edit-Endpoint-with-Burp-Suite]]

**Objective**: Interact with the profile edit form to prepare for request interception.

**Instructions**: Manually attempt to edit profile details.

Go to https://target.com/account/profile/edit, enter changes to first name, email, and password, then submit the form.

**Expected Output**: Profile updates if valid, or error if invalid.

**Success Indicators**:
- Form submission triggers a POST request
- Endpoint responds to modifications

### Step 4: Intercept and Observe Request with Burp Suite
procedure: [[procedures/Analyze-Profile-Edit-Endpoint-with-Burp-Suite]]

**Objective**: Capture the profile edit request to inspect its structure.

**Instructions**: Configure Burp Suite proxy and repeat the form submission.

Set browser proxy to Burp Suite (127.0.0.1:8080), resubmit the profile edit form, and check Burp's HTTP history for the POST to /account/profile/edit.

**Expected Output**: Intercepted request showing form parameters like username, email, password.

**Success Indicators**:
- Request visible in Burp history
- Parameters clearly visible

### Step 5: Identify Lack of CSRF Protection
procedure: [[procedures/Analyze-Profile-Edit-Endpoint-with-Burp-Suite]]

**Objective**: Confirm the vulnerability by checking for anti-CSRF measures.

**Instructions**: Analyze the intercepted request headers and body.

In Burp, examine the POST request for CSRF tokens, SameSite cookies, or Origin checks; note their absence.

**Expected Output**: No CSRF token field or header validation.

**Success Indicators**:
- Absence of _token or similar fields
- No custom headers enforcing origin

### Step 6: Execute CSRF Proof-of-Concept
procedure: [[procedures/Exploit-CSRF-for-Account-Takeover]]

**Objective**: Forge a request via a malicious page to takeover the account.

**Instructions**: Create and host a malicious HTML page, then lure victim to visit it while authenticated.

Craft HTML with a hidden form: <form action="https://target.com/account/profile/edit" method="POST"><input type="hidden" name="username" value="hacker"><input type="hidden" name="email" value="attacker@email.com"><input type="hidden" name="password" value="newpass"><input type="hidden" name="cpassword" value="newpass"><input type="submit" value="Save"></form>, add JavaScript to auto-submit and use history.pushState to hide navigation. Host on a server and send link to victim.

**Expected Output**: Victim's account details updated to attacker's values upon page load.

**Success Indicators**:
- Profile changes confirmed on target site
- Login with new credentials succeeds

## Attack Chain Summary

### Key Achievements

1. Successful registration and authentication without verification
2. Identification of unprotected CSRF endpoint using Burp Suite
3. Full account takeover via malicious HTML form submission

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
