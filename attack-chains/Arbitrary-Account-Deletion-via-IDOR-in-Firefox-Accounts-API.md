---
tags:
  - idor
  - account-deletion
  - sso
  - firefox-accounts
  - api-exploitation
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-SSO-Accounts-for-IDOR-Exploitation]]'
  - '[[procedures/Intercept-and-Modify-Deletion-Request-with-Burp-Suite]]'
  - '[[procedures/Execute-Modified-Account-Deletion]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:48.199Z'
description: >-
  An authenticated attacker exploits an IDOR vulnerability in the Firefox
  Accounts API to delete any other user's account by modifying the email in a
  deletion request payload, targeting SSO accounts without custom passwords.
skill_level: intermediate
impact_level: high
id: 0d5cbebe-3043-4e73-bbd1-115ddb15426d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Arbitrary Account Deletion via IDOR in Firefox Accounts API

Multi-stage attack chain demonstrating exploitation of an Insecure Direct Object Reference (IDOR) vulnerability in the Firefox Accounts API, allowing an authenticated attacker to delete arbitrary user accounts using only the victim's email address.

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
    A[Setup SSO Accounts] --> B[Authenticate Attacker]
    B --> C[Intercept Legitimate Request]
    C --> D[Modify Payload for Victim]
    D --> E[Execute Deletion]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#f39c12
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform with Firefox Accounts API
- SSO services (e.g., Google login)
- No custom password set on accounts

### Initial Access Requirements

- Attacker must have a valid SSO account (e.g., Google-linked Firefox account without password)
- Knowledge of victim's email address
- Network access to https://api.accounts.firefox.com

## Detailed Attack Procedures

### Step 1: Prepare Attacker and Victim Accounts
procedure: [[procedures/Setup-SSO-Accounts-for-IDOR-Exploitation]]

**Objective**: Create or use existing SSO accounts without custom passwords to enable exploitation without authPW validation.

**Instructions**: Register both attacker and victim accounts using Google SSO during Firefox Accounts signup, ensuring no custom password is set. This leaves the authPW field empty or default, which the API does not enforce for deletion requests.

**Expected Output**: Two active SSO accounts linked to Firefox services, verifiable via login.

**Success Indicators**:
- Successful SSO login without password prompt
- Account details confirm no custom password configured

### Step 2: Authenticate Attacker Session
procedure: [[procedures/Setup-SSO-Accounts-for-IDOR-Exploitation]]

**Objective**: Establish an authenticated session for the attacker to issue API requests.

**Instructions**: Log in to the Firefox Accounts system using the attacker's Google SSO credentials. This generates session cookies or tokens required for authenticated API calls.

**Expected Output**: Active session with access to account management features.

**Success Indicators**:
- Dashboard or account settings accessible post-login
- Session cookies present in browser (e.g., via developer tools)

### Step 3: Intercept Legitimate Account Deletion Request
procedure: [[procedures/Intercept-and-Modify-Deletion-Request-with-Burp-Suite]]

**Objective**: Capture a sample deletion request to understand the payload structure.

**Instructions**: Configure Burp Suite as a proxy, initiate account deletion in the Firefox UI to trigger a POST to /v1/account/destroy, intercept it, forward to Repeater, and cancel the original to avoid self-deletion.

**Expected Output**: Intercepted request in Burp Repeater showing JSON payload with 'email' field.

**Success Indicators**:
- Request body visible: {"email": "attacker@example.com"}
- No authPW required in payload for SSO accounts

### Step 4: Modify JSON Payload for Victim
procedure: [[procedures/Intercept-and-Modify-Deletion-Request-with-Burp-Suite]]

**Objective**: Alter the request to target the victim's account by substituting their email.

**Instructions**: In Burp Repeater, edit the request body to replace the 'email' value with the victim's email (e.g., "victims344@gmail.com"). Ensure session cookies from the attacker login are included in headers.

**Expected Output**: Modified POST request ready for submission.

**Success Indicators**:
- Payload updated: {"email": "victims344@gmail.com"}
- Request headers include valid attacker session tokens

### Step 5: Send Modified Request to Delete Victim's Account
procedure: [[procedures/Execute-Modified-Account-Deletion]]

**Objective**: Submit the tampered request to permanently delete the victim's account.

**Instructions**: From Burp Repeater, send the modified POST request to https://api.accounts.firefox.com/v1/account/destroy. The server processes it without verifying session ownership of the targeted email.

**Expected Output**: HTTP 200 or success response indicating deletion; victim's account inaccessible upon verification.

**Success Indicators**:
- API response confirms deletion (e.g., no error on email)
- Victim's login fails or account is reported as deleted in Mozilla services

## Attack Chain Summary

### Key Achievements

1. Bypassed account ownership verification in the API
2. Achieved permanent deletion of arbitrary SSO accounts using only email
3. Demonstrated high-impact disruption to Mozilla services without victim credentials

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Impact]]

---
*Last updated: 2023-10-01T00:00:00Z*
