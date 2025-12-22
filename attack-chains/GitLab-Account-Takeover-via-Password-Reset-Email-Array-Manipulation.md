---
tags:
  - gitlab
  - account-takeover
  - password-reset
  - http-manipulation
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Content-Type-Converter]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - GitLab
complexity: medium
procedures:
  - '[[procedures/Navigate-to-GitLab-Password-Reset-Page]]'
  - '[[procedures/Intercept-Password-Reset-Request-with-Burp-Suite]]'
  - '[[procedures/Convert-Request-to-JSON-Format]]'
  - '[[procedures/Modify-JSON-Payload-for-Email-Array]]'
  - '[[procedures/Forward-Modified-Request]]'
  - '[[procedures/Receive-and-Use-Password-Reset-Link]]'
step_count: 6
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Exploits a vulnerability in GitLab's password reset functionality to send
  reset links to both victim and attacker emails, enabling account takeover.
skill_level: intermediate
impact_level: high
id: 55bc0c0e-de67-4344-9a06-1837b8badbf1
created_at: '2025-12-11T06:10:31.188Z'
updated_at: '2025-12-11T06:10:31.188Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# GitLab Account Takeover via Password Reset Email Array Manipulation

Multi-stage attack chain demonstrating how to exploit a vulnerability in GitLab's password reset functionality by manipulating the email parameter into an array, allowing the reset link to be sent to both the victim's and attacker's emails without user interaction. This enables full account takeover using only the victim's email address.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Reset Page] --> B[Intercept Request]
    B --> C[Convert to JSON]
    C --> D[Modify Payload]
    D --> E[Forward Request]
    E --> F[Use Reset Link]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#e74c3c
    style F fill:#f39c12
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- [[tools/Content-Type-Converter]]

### Target Environment

- Web
- GitLab services
- No specific ports required beyond standard HTTP/HTTPS

### Initial Access Requirements

- Knowledge of victim's email address
- Access to a web browser and Burp Suite proxy
- Attacker-controlled email address

## Detailed Attack Procedures

### Step 1: Access Reset Page - [[procedures/Navigate-to-GitLab-Password-Reset-Page]]

**Procedure**: [[procedures/Navigate-to-GitLab-Password-Reset-Page]]

**Objective**: Initiate the password reset process by entering the victim's email.

**Expected Output**: The password reset form is submitted, and the request is ready for interception.

**Success Indicators**:
- Form submission triggers an HTTP request
- No errors on the page

### Step 2: Intercept Request - [[procedures/Intercept-Password-Reset-Request-with-Burp-Suite]]

**Procedure**: [[procedures/Intercept-Password-Reset-Request-with-Burp-Suite]]

**Objective**: Capture the HTTP request for the password reset submission using Burp Suite.

**Expected Output**: The request is intercepted in Burp Suite's Proxy tab.

**Success Indicators**:
- Request appears in Burp Suite
- Details of the request are visible for editing

### Step 3: Convert to JSON - [[procedures/Convert-Request-to-JSON-Format]]

**Procedure**: [[procedures/Convert-Request-to-JSON-Format]]

**Objective**: Use the Content-Type Converter extension in Burp Suite to change the request format to JSON for easier manipulation.

**Expected Output**: The request body is converted to JSON format.

**Success Indicators**:
- Content-Type header changes to application/json
- Payload is now in JSON structure

### Step 4: Modify Payload - [[procedures/Modify-JSON-Payload-for-Email-Array]]

**Procedure**: [[procedures/Modify-JSON-Payload-for-Email-Array]]

**Objective**: Alter the JSON payload to turn the email parameter into an array including both victim and attacker emails.

**Expected Output**: Modified payload with email array.

**Success Indicators**:
- Payload shows 'user': {'email': ['victim@gmail.com', 'attacker@gmail.com']}
- No syntax errors in JSON

### Step 5: Forward Request - [[procedures/Forward-Modified-Request]]

**Procedure**: [[procedures/Forward-Modified-Request]]

**Objective**: Send the modified request to the GitLab server to trigger password reset emails to both addresses.

**Expected Output**: Server processes the request and sends emails.

**Success Indicators**:
- HTTP response indicates success (e.g., 200 OK)
- Emails are received by attacker

### Step 6: Use Reset Link - [[procedures/Receive-and-Use-Password-Reset-Link]]

**Procedure**: [[procedures/Receive-and-Use-Password-Reset-Link]]

**Objective**: Access the reset link from the attacker's email, set a new password, and log in as the victim.

**Expected Output**: Successful login to the victim's account.

**Success Indicators**:
- Reset link works
- Password change is successful
- Access to victim's account confirmed

## Attack Chain Summary

### Key Achievements

1. Interception and modification of password reset request
2. Sending reset link to attacker without victim interaction
3. Full account takeover

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

*Last updated: 2023-10-01*
