---
id: ac-stored-xss-oberlo-profile
tags:
  - xss
  - stored-xss
  - javascript-injection
  - session-hijacking
  - oberlo
  - shopify
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Oberlo-Account]]'
  - '[[procedures/Access-Oberlo-Profile-Settings]]'
  - '[[procedures/Inject-XSS-Payload-into-Profile-Name]]'
  - '[[procedures/Verify-XSS-Payload-Execution]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:18.242Z'
description: >-
  A multi-step attack exploiting a stored XSS vulnerability in the Oberlo
  application's user profile name field to inject and execute malicious
  JavaScript, enabling session hijacking and data theft for viewers of the
  profile.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Stored XSS in Oberlo Profile Name Field for JavaScript Execution and Session Hijacking

Multi-stage attack chain demonstrating a complete stored XSS exploitation workflow in the Oberlo application, allowing attackers to inject malicious JavaScript into a user's profile name, which executes for any viewer of that profile.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Account Creation] --> B[Access Profile]
    B --> C[Payload Injection]
    C --> D[Execution and Impact]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Oberlo web application (https://app.oberlo.com)
- No specific services or ports required beyond standard HTTPS (443)
- Internet access to the Oberlo platform

### Initial Access Requirements

- No prior credentials needed; attack begins with free account registration
- Attacker must be able to create an account on Oberlo
- Victim must view the attacker's profile page

## Detailed Attack Procedures

### Step 1: Account Creation
procedure: [[procedures/Create-Oberlo-Account]]

**Objective**: Establish a user account on the Oberlo platform to access profile editing features.

**Instructions**: Register a new account using valid email and password. This provides the necessary authentication to modify the profile.

**Expected Output**: Successful login and dashboard access.

**Success Indicators**:
- Confirmation email received
- Redirect to Oberlo dashboard

### Step 2: Access Profile Settings
procedure: [[procedures/Access-Oberlo-Profile-Settings]]

**Objective**: Navigate to the profile editing interface where the vulnerable name field is located.

**Instructions**: From the dashboard, click on settings and select the account profile section to reach the editable form.

**Expected Output**: Profile settings page loads with form fields visible.

**Success Indicators**:
- URL matches https://app.oberlo.com/settings/account/profile
- Name field is editable

### Step 3: Payload Injection
procedure: [[procedures/Inject-XSS-Payload-into-Profile-Name]]

**Objective**: Inject a malicious JavaScript payload into the name field to store and later execute it.

**Instructions**: Enter the payload `"><img src=x onerror=alert(document.domain)>` into the Name field and save the profile.

**Expected Output**: Profile saves without errors; payload is stored.

**Success Indicators**:
- No validation errors on save
- Profile updates successfully

### Step 4: Verify Execution
procedure: [[procedures/Verify-XSS-Payload-Execution]]

**Objective**: Confirm the payload executes in the browser context when the profile is viewed.

**Instructions**: View the profile page (e.g., by logging out and accessing via another account or incognito). The alert should trigger, demonstrating execution.

**Expected Output**: JavaScript alert box appears showing the domain.

**Success Indicators**:
- Alert executes on page load
- No sanitization blocks the script

## Attack Chain Summary

### Key Achievements

1. Successful account creation and profile access
2. Injection of unsanitized JavaScript payload
3. Execution of payload leading to arbitrary code in victim browsers
4. Potential for session hijacking or data exfiltration

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
