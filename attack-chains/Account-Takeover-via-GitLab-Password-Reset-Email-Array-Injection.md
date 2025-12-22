---
id: ac-001
tags:
  - account-takeover
  - password-reset
  - email-injection
  - web-vulnerability
  - gitlab
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Content-Type-Converter]]'
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Initiate-GitLab-Password-Reset-Request]]'
  - '[[procedures/Intercept-and-Convert-Reset-Request-to-JSON]]'
  - '[[procedures/Modify-JSON-Payload-for-Email-Injection]]'
  - '[[procedures/Forward-Modified-Reset-Request]]'
  - '[[procedures/Complete-Account-Takeover-via-Reset-Link]]'
step_count: 6
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:34.528Z'
description: >-
  Exploits improper access control in GitLab's password reset endpoint to inject
  an attacker's email into the request, receiving a reset link and taking over
  the victim's account without interaction.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# Account Takeover via GitLab Password Reset Email Array Injection

Multi-stage attack chain demonstrating a complete account takeover workflow by exploiting a vulnerability in GitLab's password reset functionality. The attacker manipulates the reset request to receive a password reset link for the victim's account, allowing unauthorized password change and full access without victim awareness.

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
    A[Initiate Reset Request] --> B[Intercept Request]
    B --> C[Convert to JSON]
    C --> D[Modify Payload]
    D --> E[Forward Modified Request]
    E --> F[Receive and Use Reset Link]
    F --> G[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#f39c12
    style E fill:#3498db
    style F fill:#3498db
    style G fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- [[tools/Content-Type-Converter]]

### Target Environment

- GitLab web application (version vulnerable to CVE or similar, e.g., pre-patch for this issue)
- Required services/ports: HTTPS on port 443 for web access, email service for reset links
- Network access requirements: Direct internet access to GitLab instance, ability to proxy traffic

### Initial Access Requirements

- No prior credentials needed
- Knowledge of victim's email address
- Network position: Attacker must be able to intercept their own traffic to the target (local proxy setup)
- Prior access needed: None, but Burp Suite configured as proxy

## Detailed Attack Procedures

### Step 1: Initiate Password Reset Request
procedure: [[procedures/Initiate-GitLab-Password-Reset-Request]]

**Objective**: Start the password reset process by submitting the victim's email to trigger the initial request.

**Instructions**: Navigate to the GitLab login page and click the 'Forgot Your Password?' link. Enter the victim's email address (e.g., victim@gmail.com) in the form and submit it. This generates an HTTP POST request to the password reset endpoint.

**Expected Output**: The request is sent, but intercepted in the next step if proxy is active.

**Success Indicators**:
- Form submission completes without errors
- HTTP POST request visible in proxy tool

### Step 2: Intercept the Submit Request
procedure: [[procedures/Intercept-and-Convert-Reset-Request-to-JSON]]

**Objective**: Capture the password reset submission using a proxy to prepare for modification.

**Instructions**: With Burp Suite configured as your browser's proxy, submit the reset form. The tool will intercept the HTTP POST request to the forgot password endpoint.

**Expected Output**: Intercepted request displayed in Burp Suite's Proxy > HTTP History or Repeater tab.

**Success Indicators**:
- Request body shows the victim's email in form-encoded format
- No server response yet (held in intercept mode)

### Step 3: Convert Intercepted Request to JSON
procedure: [[procedures/Intercept-and-Convert-Reset-Request-to-JSON]]

**Objective**: Transform the form-encoded request into JSON for easier manipulation, exploiting the backend's JSON processing.

**Instructions**: In Burp Suite's HTTP Editor, right-click the request body and select Extensions > Content-Type Converter > Convert to JSON. Ensure the extension is installed from the BApp Store.

**Expected Output**: Request body now in JSON format, e.g., {"user":{"email":"victim@gmail.com"}}.

**Success Indicators**:
- Content-Type header updated to application/json
- Body parses as valid JSON without errors

### Step 4: Modify JSON Payload for Email Injection
procedure: [[procedures/Modify-JSON-Payload-for-Email-Injection]]

**Objective**: Alter the JSON to include the attacker's email in an array, causing reset links to be sent to both.

**Instructions**: Edit the JSON body in Burp Suite to change the email field to an array: {"user":{"email":["victim@gmail.com","attacker@gmail.com"]}}. This exploits the lack of validation for array inputs.

**Expected Output**: Modified JSON payload ready for forwarding.

**Success Indicators**:
- JSON validates (no syntax errors)
- Array includes both emails

### Step 5: Forward the Modified Request
procedure: [[procedures/Forward-Modified-Reset-Request]]

**Objective**: Submit the tampered request to trigger password reset emails to both addresses.

**Instructions**: In Burp Suite, click 'Forward' or 'Send' to release the request to the server.

**Expected Output**: Server processes the request, sending reset emails to both victim and attacker.

**Success Indicators**:
- HTTP response code 200 or success status
- Email received in attacker's inbox shortly after

### Step 6: Complete Account Takeover via Reset Link
procedure: [[procedures/Complete-Account-Takeover-via-Reset-Link]]

**Objective**: Use the received reset link to change the victim's password and gain access.

**Instructions**: Open the reset link from the attacker's email, enter a new password, submit, and then log in to the victim's account using the new credentials.

**Expected Output**: Password successfully reset; login succeeds with new password.

**Success Indicators**:
- Reset link works without expiration issues
- Full access to victim's GitLab account confirmed

## Attack Chain Summary

### Key Achievements

1. Bypassed single-email validation in password reset
2. Received unauthorized reset link for victim's account
3. Achieved complete account takeover without victim interaction

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Credential Access]] Credential Access

---
*Last updated: 2024-01-01T00:00:00Z*
