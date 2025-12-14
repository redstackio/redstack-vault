---
tags:
  - account-takeover
  - password-reset
  - improper-validation
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
  - '[[procedures/Intercept-and-Modify-UPchieve-Password-Reset-Request]]'
  - '[[procedures/Use-Shared-Reset-Token-for-Account-Takeover]]'
step_count: 8
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:24.392Z'
description: >-
  Exploits a flaw in UPchieve's password reset endpoint by injecting an array of
  emails to receive the victim's reset token, enabling unauthorized account
  takeover.
skill_level: intermediate
impact_level: high
id: ffad03df-b8f4-4b01-89ed-5dc006fe23bf
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# UPchieve Full Account Takeover via Password Reset Email Array Injection

Multi-stage attack chain demonstrating a complete account takeover workflow by exploiting improper validation in the password reset functionality of UPchieve.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 8 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Reset Page] --> B[Submit Victim Email]
    B --> C[Intercept Request with Burp Suite]
    C --> D[Modify Email to Array]
    D --> E[Forward Modified Request]
    E --> F[Receive Shared Reset Token]
    F --> G[Access Reset Link]
    G --> H[Reset Password and Takeover]

    style A fill:#e74c3c
    style B fill:#e74c3c
    style C fill:#f39c12
    style D fill:#f39c12
    style E fill:#f39c12
    style F fill:#3498db
    style G fill:#3498db
    style H fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform
- Access to UPchieve application at https://app.upchieve.org
- Email accounts for victim and attacker
- Network access to intercept HTTP traffic

### Initial Access Requirements

- No prior credentials needed
- Attacker must know victim's email address
- Proxy setup for traffic interception

## Detailed Attack Procedures

### Step 1: Navigate to Password Reset Page
procedure: [[procedures/Intercept-and-Modify-UPchieve-Password-Reset-Request]]

**Objective**: Access the target application's password reset functionality to initiate the exploit process.

**Instructions**: Open a web browser and navigate to the UPchieve password reset endpoint.

**Expected Output**: The password reset form loads, prompting for an email address.

**Success Indicators**:
- Reset page is accessible at https://app.upchieve.org/resetpassword
- Form field for email input is visible

### Step 2: Enter Victim's Email Address
procedure: [[procedures/Intercept-and-Modify-UPchieve-Password-Reset-Request]]

**Objective**: Submit the victim's email to trigger the reset request that will be intercepted and modified.

**Instructions**: Input the victim's email address (e.g., victim@gmail.com) into the form field and submit the request.

**Expected Output**: The form submission triggers an HTTP POST request to the backend.

**Success Indicators**:
- Form is submitted without errors
- Request is captured in the proxy tool

### Step 3: Intercept the Request
procedure: [[procedures/Intercept-and-Modify-UPchieve-Password-Reset-Request]]

**Objective**: Capture the outgoing password reset request using a proxy to allow modification.

**Instructions**: Configure Burp Suite as a proxy and intercept the HTTP POST request from the form submission.

**Expected Output**: The raw HTTP request is held in Burp Suite's proxy interceptor.

**Success Indicators**:
- Request body shows {"email": "victim@gmail.com"}
- No immediate server response

### Step 4: Modify the JSON Body to Include Multiple Emails
procedure: [[procedures/Intercept-and-Modify-UPchieve-Password-Reset-Request]]

**Objective**: Alter the request to inject the attacker's email alongside the victim's, exploiting the lack of validation.

**Instructions**: In Burp Suite, edit the JSON body from {"email": "victim@gmail.com"} to {"email": ["victim@gmail.com", "attacker@gmail.com"]}.

**Expected Output**: Modified request body reflects the email array.

**Success Indicators**:
- JSON parses correctly as an array
- No syntax errors in the editor

### Step 5: Forward the Modified Request
procedure: [[procedures/Intercept-and-Modify-UPchieve-Password-Reset-Request]]

**Objective**: Send the tampered request to the server to generate a shared reset token.

**Instructions**: Forward the modified request in Burp Suite to the server.

**Expected Output**: Server processes the request and queues emails.

**Success Indicators**:
- HTTP response indicates success (e.g., 200 OK)
- No validation errors from the backend

### Step 6: Receive the Same Password Reset Link in Both Emails
procedure: [[procedures/Use-Shared-Reset-Token-for-Account-Takeover]]

**Objective**: Confirm the exploit by receiving the identical reset token in both victim and attacker inboxes.

**Instructions**: Check email inboxes for both accounts; the server sends the same token to all emails in the array.

**Expected Output**: Identical reset links arrive in both emails.

**Success Indicators**:
- Reset email received in attacker's inbox
- Link contains the same token as intended for victim

### Step 7: Access the Reset Link from Attacker's Email
procedure: [[procedures/Use-Shared-Reset-Token-for-Account-Takeover]]

**Objective**: Use the intercepted token to access the victim's password reset form without victim interaction.

**Instructions**: Click the reset link in the attacker's email to open the reset form.

**Expected Output**: Browser loads the password reset page pre-authenticated for the victim's account.

**Success Indicators**:
- Form allows new password entry
- No additional verification required

### Step 8: Reset the Password to Complete Takeover
procedure: [[procedures/Use-Shared-Reset-Token-for-Account-Takeover]]

**Objective**: Change the victim's password to gain full unauthorized access.

**Instructions**: Enter a new password in the form and submit to update the account credentials.

**Expected Output**: Confirmation of password reset; login with new credentials succeeds.

**Success Indicators**:
- Password change succeeds
- Attacker can log in to victim's account

## Attack Chain Summary

### Key Achievements

1. Bypassed single-email validation in password reset endpoint
2. Received victim's reset token without their knowledge
3. Achieved full account takeover with minimal interaction

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---

*Last updated: 2023-10-01T00:00:00Z*
