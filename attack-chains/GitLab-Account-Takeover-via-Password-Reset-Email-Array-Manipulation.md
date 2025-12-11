---
tags:
  - gitlab
  - account-takeover
  - improper-access-control
  - web-exploitation
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Content-Type-Converter]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Intercept-and-Modify-GitLab-Password-Reset-Request]]'
step_count: 7
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Exploits improper access control in GitLab's password reset functionality to
  achieve full account takeover by sending reset links to attacker-controlled
  emails.
skill_level: intermediate
impact_level: high
id: 0286801c-592b-45d4-809e-1d4d5ddef28a
created_at: '2025-12-11T03:48:06.092Z'
updated_at: '2025-12-11T03:48:06.092Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# GitLab Account Takeover via Password Reset Email Array Manipulation

Multi-stage attack chain demonstrating exploitation of improper access control in GitLab's password reset endpoint, allowing an attacker to receive a password reset link for a victim's account and achieve full takeover without victim interaction.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 7 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Reset Form] --> B[Intercept Request]
    B --> C[Convert to JSON]
    C --> D[Modify Payload]
    D --> E[Forward Request]
    E --> F[Receive Email]
    F --> G[Reset Password]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#e74c3c
    style F fill:#f39c12
    style G fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- [[tools/Content-Type-Converter]]

### Target Environment

- Platform: Web
- Services: GitLab
- Network access: Public access to GitLab instance

### Initial Access Requirements

- Knowledge of victim's email address
- Attacker-controlled email address
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Navigate to Password Reset Form - [[procedures/Intercept-and-Modify-GitLab-Password-Reset-Request]]

**Objective**: Access the password reset functionality on the GitLab web interface.

**Instructions**: Navigate to the 'Forgot Your Password?' link on the GitLab login page.

**Expected Output**: The password reset form is displayed, ready for email submission.

**Success Indicators**:
- Form loads successfully
- No authentication required for access

### Step 2: Enter Victim Email and Intercept Request - [[procedures/Intercept-and-Modify-GitLab-Password-Reset-Request]]

**Objective**: Submit the victim's email and capture the HTTP request for modification.

**Instructions**: Enter the victim's email (e.g., victim@gmail.com) in the form and submit it while intercepting the request using [[tools/Burp-Suite]].

**Expected Output**: The HTTP request is captured in Burp Suite's Proxy tab.

**Success Indicators**:
- Request is intercepted without errors
- Request body contains the submitted email

### Step 3: Convert Intercepted Request to JSON - [[procedures/Intercept-and-Modify-GitLab-Password-Reset-Request]]

**Objective**: Convert the request format to JSON to enable payload modification.

**Instructions**: In Burp Suite's HTTP Editor, right-click the intercepted request and select Extensions -> [[tools/Content-Type-Converter]] -> Convert to JSON.

**Expected Output**: The request body is converted to JSON format.

**Success Indicators**:
- Content-Type header changes to application/json
- Payload is now in editable JSON structure

### Step 4: Modify JSON Payload with Email Array - [[procedures/Intercept-and-Modify-GitLab-Password-Reset-Request]]

**Objective**: Alter the email parameter to an array including both victim and attacker emails.

**Instructions**: Edit the JSON payload to replace the email parameter with an array: {'user': {'email': ['victim@gmail.com', 'attacker@gmail.com']}}.

**Expected Output**: Modified JSON payload ready for submission.

**Success Indicators**:
- Array structure is valid JSON
- Both emails are included in the payload

### Step 5: Forward Modified Request - [[procedures/Intercept-and-Modify-GitLab-Password-Reset-Request]]

**Objective**: Send the altered request to the GitLab server.

**Instructions**: Use [[tools/Burp-Suite]] to forward the modified request.

**Expected Output**: Server processes the request and sends reset emails.

**Success Indicators**:
- HTTP response indicates success (e.g., 200 OK)
- No validation errors returned

### Step 6: Receive Password Reset Email

**Objective**: Obtain the reset link sent to the attacker's email.

**Instructions**: Check the attacker's email inbox for the password reset email from GitLab.

**Expected Output**: Email contains a valid password reset link.

**Success Indicators**:
- Email received in attacker's inbox
- Link is active and points to GitLab reset endpoint

### Step 7: Use Reset Link to Change Password

**Objective**: Reset the victim's password using the received link to achieve account takeover.

**Instructions**: Click the reset link in the email and set a new password for the victim's account.

**Expected Output**: Password changed successfully, allowing login as the victim.

**Success Indicators**:
- Successful password reset confirmation
- Ability to log in with new credentials

## Attack Chain Summary

### Key Achievements

1. Bypassed access controls to receive victim's reset link
2. Achieved full account takeover without victim interaction
3. Demonstrated vulnerability in GitLab's password reset handling

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

*Last updated: 2023-10-01*
