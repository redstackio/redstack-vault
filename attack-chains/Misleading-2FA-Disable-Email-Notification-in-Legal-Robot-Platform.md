---
tags:
  - business-logic
  - 2fa
  - email-notification
  - user-confusion
  - legal-robot
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
complexity: low
procedures:
  - '[[procedures/Create-New-Account-on-Legal-Robot]]'
  - '[[procedures/Enable-2FA-with-Authenticator-App]]'
  - '[[procedures/Skip-U2F-Security-Key-Registration]]'
  - '[[procedures/Disable-2FA-Authenticator-App]]'
  - '[[procedures/Receive-2FA-Disable-Email-Notification]]'
  - '[[procedures/Observe-Incorrect-2FA-Status-in-Email]]'
step_count: 6
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  A business logic vulnerability where disabling 2FA via authenticator app
  triggers an email falsely claiming 2FA remains enabled due to a non-existent
  security key, leading to user confusion and trust erosion.
skill_level: low
impact_level: low
id: 72b32d6c-feed-45b2-b0c4-8042d66a677e
created_at: '2025-12-14T17:24:45.481Z'
updated_at: '2025-12-14T17:24:45.481Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Misleading 2FA Disable Email Notification in Legal Robot Platform

Multi-stage reproduction chain demonstrating a business logic error in the Legal Robot platform's 2FA notification system. By setting up an account with only authenticator app-based 2FA and then disabling it without a U2F key, the system sends an email incorrectly stating that 2FA is still active due to a security key. This causes user confusion and undermines trust in security notifications, though it does not enable unauthorized access.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~5 minutes |
| Skill Level | Low |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Account] --> B[Enable 2FA App] --> C[Skip U2F Setup] --> D[Disable 2FA App] --> E[Receive Email] --> F[Observe Misleading Claim]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#9b59b6
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Legal Robot web platform
- Access to email inbox for notifications
- No special services or ports required beyond standard HTTPS (port 443)

### Initial Access Requirements

- Internet access
- Valid email address for account creation
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Create New Account
procedure: [[procedures/Create-New-Account-on-Legal-Robot]]

**Objective**: Establish a test account on the Legal Robot platform to begin 2FA setup.

**Instructions**: Navigate to the Legal Robot signup page at their official website. Fill in the registration form with a new email address, username, and password. Complete any CAPTCHA or verification steps if prompted. Submit the form to create the account. Upon success, you will be redirected to the login page or dashboard.

**Expected Output**: Confirmation email sent, and ability to log in with new credentials.

**Success Indicators**:
- Account creation successful
- Login possible with new credentials

### Step 2: Enable 2FA with Authenticator App
procedure: [[procedures/Enable-2FA-with-Authenticator-App]]

**Objective**: Activate 2FA using only the authenticator app method to set up the flawed scenario.

**Instructions**: Log in to the newly created account. Navigate to the account settings or security section. Locate the 2FA enablement option and select the authenticator app method. Scan the provided QR code with an authenticator app (e.g., Google Authenticator) on your mobile device. Enter the generated code to verify and enable 2FA. Ensure no other 2FA methods are activated.

**Expected Output**: 2FA enabled confirmation in the UI, requiring app codes for future logins.

**Success Indicators**:
- 2FA active status shown in settings
- Login now prompts for app code

### Step 3: Skip U2F Security Key Registration
procedure: [[procedures/Skip-U2F-Security-Key-Registration]]

**Objective**: Avoid registering any FIDO U2F security key to isolate the authenticator app as the sole 2FA method.

**Instructions**: In the 2FA settings, do not select or configure the U2F security key option. If prompted during setup, explicitly skip or ignore the U2F registration flow. Confirm that only the authenticator app is listed as enabled in the settings.

**Expected Output**: No U2F key registered; 2FA settings reflect only authenticator app.

**Success Indicators**:
- U2F option remains unconfigured
- No security key associated with account

### Step 4: Disable 2FA Authenticator App
procedure: [[procedures/Disable-2FA-Authenticator-App]]

**Objective**: Deactivate the authenticator app 2FA to trigger the notification system.

**Instructions**: Remain logged in and return to the account settings or security section. Locate the 2FA disable option for the authenticator app. Confirm the disable action, which may require entering the current app-generated code for verification. Submit to remove the authenticator app registration.

**Expected Output**: 2FA disabled confirmation in the UI; no 2FA methods active.

**Success Indicators**:
- Authenticator app removed from 2FA settings
- Login no longer requires 2FA code

### Step 5: Receive 2FA Disable Email Notification
procedure: [[procedures/Receive-2FA-Disable-Email-Notification]]

**Objective**: Capture the automated email sent upon 2FA disablement.

**Instructions**: After disabling, check the associated email inbox for the automatic notification from Legal Robot. The email should arrive within seconds to minutes, detailing the change.

**Expected Output**: Email with subject related to 2FA removal, body stating: 'The 2FA Authenticator App registration was just removed from your Legal Robot (TEST) account. 2-Factor Authentication is still enabled since you registered a security key.'

**Success Indicators**:
- Email received in inbox
- Notification references both app removal and security key

### Step 6: Observe Incorrect 2FA Status in Email
procedure: [[procedures/Observe-Incorrect-2FA-Status-in-Email]]

**Objective**: Identify the business logic error in the email content.

**Instructions**: Review the email body for the false claim about a registered security key enabling 2FA. Cross-verify against account settings to confirm no U2F key exists and 2FA is fully disabled.

**Expected Output**: Confirmation of misleading statement despite no security key registration.

**Success Indicators**:
- Email inaccurately reports 2FA as enabled
- Account settings show complete 2FA disablement

## Attack Chain Summary

### Key Achievements

1. Successful reproduction of the notification flaw
2. Demonstration of user-facing misinformation
3. Highlighted business logic gap in email templating

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01*
