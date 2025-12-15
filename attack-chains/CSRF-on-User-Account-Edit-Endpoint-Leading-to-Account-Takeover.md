---
id: ac-csrf-account-takeover-1624421
tags:
  - csrf
  - account-takeover
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Register-Account-on-Target-Application]]'
  - '[[procedures/Observe-User-Data-Edit-Request-Format]]'
  - '[[procedures/Modify-Content-Type-Header-for-CSRF-Exploitation]]'
  - '[[procedures/Create-0-Click-HTML-POC-for-CSRF-Attack]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:06.765Z'
description: >-
  A multi-stage attack exploiting CSRF vulnerability on the user account edit
  endpoint to enable unauthorized changes to email or password, resulting in
  full account takeover.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# CSRF on User Account Edit Endpoint Leading to Account Takeover

Multi-stage attack chain demonstrating a complete attack workflow exploiting a CSRF vulnerability in the user account edit endpoint at https://█████/user/account, allowing attackers to forge requests and takeover victim accounts by changing email or password without authentication.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Register Account] --> B[Observe Edit Request]
    B --> C[Modify Content-Type]
    C --> D[Deploy HTML PoC]
    D --> E[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome or Firefox for testing)
- Text editor for creating HTML PoC

### Target Environment

- Web application with user account management at https://█████/user/account
- No specific ports or services beyond standard HTTPS (443)

### Initial Access Requirements

- Ability to register a new account
- Network access to the target domain
- No prior credentials needed for initial registration

## Detailed Attack Procedures

### Step 1: Register an Account
procedure: [[procedures/Register-Account-on-Target-Application]]

**Objective**: Gain initial access to the application by creating a test account to observe and interact with the user edit functionality.

**Instructions**: Navigate to the registration page and complete the signup process using valid user details.

**Expected Output**: Successful account creation with access to the user account dashboard.

**Success Indicators**:
- Confirmation email or login success
- Access to https://█████/user/account

### Step 2: Observe User Data Edit Request
procedure: [[procedures/Observe-User-Data-Edit-Request-Format]]

**Objective**: Analyze the normal format of user data edit requests to identify the expected content type and structure.

**Instructions**: Attempt to edit user data (e.g., change a non-sensitive field) while monitoring the network traffic in browser developer tools to capture the JSON-based request.

**Expected Output**: Captured request showing Content-Type: application/json and JSON payload for user updates.

**Success Indicators**:
- Request details visible in network tab
- Server accepts JSON and updates data

### Step 3: Modify Content-Type for Exploitation
procedure: [[procedures/Modify-Content-Type-Header-for-CSRF-Exploitation]]

**Objective**: Test the server's acceptance of form-urlencoded requests without CSRF tokens to confirm the vulnerability.

**Instructions**: Using browser tools or a proxy, intercept the edit request, change the Content-Type header to application/x-www-form-urlencoded, and submit with form data to update user information like email.

**Expected Output**: Server processes the request and updates the account data without requiring a CSRF token.

**Success Indicators**:
- Unauthorized data change confirmed (e.g., email updated)
- No token validation error

### Step 4: Create and Deploy HTML PoC
procedure: [[procedures/Create-0-Click-HTML-POC-for-CSRF-Attack]]

**Objective**: Develop an automated exploit to perform a 0-click CSRF attack, allowing remote takeover of victim accounts.

**Instructions**: Create an HTML file with an auto-submitting form targeting the endpoint, host it on a controllable server, and lure victims to visit it (e.g., via phishing).

**Expected Output**: Victim's account email or password changed upon page load, enabling takeover.

**Success Indicators**:
- PoC triggers update in victim session
- Verified in browser videos on Chrome and Firefox

## Attack Chain Summary

### Key Achievements

1. Identified CSRF flaw by bypassing JSON expectation with form-urlencoded
2. Demonstrated unauthorized account modifications
3. Created 0-click PoC for practical exploitation
4. Achieved full account takeover via email/password reset

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
