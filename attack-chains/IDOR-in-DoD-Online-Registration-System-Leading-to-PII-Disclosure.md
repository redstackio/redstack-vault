---
tags:
  - idor
  - pii-leak
  - dod
  - web
  - access-control
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
procedures:
  - '[[procedures/Create-User-Account-on-DoD-Platform]]'
  - '[[procedures/Access-Update-Profile-Endpoint]]'
  - '[[procedures/Exploit-IDOR-by-Manipulating-User-ID]]'
step_count: 3
techniques:
  - '[[Account Discovery]]'
description: >-
  A multi-step attack exploiting an Insecure Direct Object Reference (IDOR)
  vulnerability in the U.S. Department of Defense's online registration and
  profile management system to disclose other users' personally identifiable
  information (PII).
skill_level: intermediate
impact_level: high
id: 8e3c631a-5ac9-4045-ad5d-6bf4ea7d336a
created_at: '2025-12-14T17:25:34.295Z'
updated_at: '2025-12-14T17:25:34.295Z'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# IDOR in DoD Online Registration System Leading to PII Disclosure

Multi-stage attack chain demonstrating a complete attack workflow exploiting an IDOR vulnerability in the U.S. Department of Defense's JOINOnline platform to gain unauthorized access to other users' PII, such as names and email addresses.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Account Creation] --> B[Profile Access]
    B --> C[IDOR Exploitation]
    C --> D[PII Disclosure]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome with Developer Tools)

### Target Environment

- Web platform
- Access to the public-facing DoD registration site
- No specific ports or services beyond standard HTTPS (443)

### Initial Access Requirements

- Internet access
- No prior credentials needed for initial registration
- Valid email for account creation

## Detailed Attack Procedures

### Step 1: Account Creation
procedure: [[procedures/Create-User-Account-on-DoD-Platform]]

**Objective**: Establish a legitimate user account on the DoD platform to gain authenticated access for subsequent steps.

**Instructions**: Navigate to the registration page and complete the signup process with valid details.

**Expected Output**: Successful account creation with login credentials and an assigned numeric user ID.

**Success Indicators**:
- Confirmation email received
- Ability to log in to the dashboard

### Step 2: Access Update Profile Endpoint
procedure: [[procedures/Access-Update-Profile-Endpoint]]

**Objective**: Log in and navigate to the profile update section to identify the user ID parameter in the URL.

**Instructions**: After logging in, go to the Update Profile section and observe the URL structure containing the <user-id>.

**Expected Output**: Profile page loads with the authenticated user's details and URL showing the numeric ID.

**Success Indicators**:
- Profile page accessible
- User ID visible in the URL (e.g., https://www.example.com/JOINOnline/UpdateProfile/12345)

### Step 3: IDOR Exploitation
procedure: [[procedures/Exploit-IDOR-by-Manipulating-User-ID]]

**Objective**: Manipulate the user ID parameter to access and disclose PII from other users' profiles without authorization.

**Instructions**: Modify the numeric user-id in the URL to a different valid ID and reload the page to view unauthorized data.

**Expected Output**: Target user's name and email address displayed on the page.

**Success Indicators**:
- Unauthorized PII visible
- No authentication prompts or errors for the manipulated ID

## Attack Chain Summary

### Key Achievements

1. Successful creation of a test account on the DoD platform
2. Identification of the vulnerable Update Profile endpoint
3. Unauthorized disclosure of other users' PII via IDOR manipulation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01*
