---
tags:
  - xss
  - self-xss
  - uber
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Uber-Partners-Portal]]'
  - '[[procedures/Navigate-to-Profile-Edit-Page]]'
  - '[[procedures/Inject-XSS-Payload-in-VAT-Field]]'
  - '[[procedures/Save-Profile-to-Store-Payload]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:26.686Z'
description: >-
  A stored self-XSS vulnerability in the VAT number field of Uber's Partners
  Profile page allows injection of JavaScript payloads that execute only in the
  attacker's own browser session upon viewing the profile.
skill_level: beginner
impact_level: low
id: 385ce5f8-a88b-432a-9609-99c2eb552676
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Stored Self-XSS in Uber Partners Profile VAT Number Field

Multi-stage attack chain demonstrating exploitation of a stored self-XSS vulnerability in Uber's Partners Portal, where an injected payload in the VAT number field executes JavaScript only in the attacker's browser upon profile view.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Login to Portal] --> B[Navigate to Profile]
    B --> C[Inject XSS Payload]
    C --> D[Save Changes]
    D --> E[View Profile to Trigger]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Web platform
- Access to Uber Partners Portal at https://partners.uber.com
- Valid Uber partner credentials

### Initial Access Requirements

- Valid login credentials for Uber Partners account
- Direct network access to the internet
- No prior access needed beyond authentication

## Detailed Attack Procedures

### Step 1: Access Uber Partners Portal
procedure: [[procedures/Access-Uber-Partners-Portal]]

**Objective**: Authenticate and gain access to the Uber Partners dashboard to reach editable profile sections.

**Instructions**: Open a web browser and navigate to the Uber Partners website, then enter credentials to log in.

**Expected Output**: Successful login redirect to the partners dashboard.

**Success Indicators**:
- Dashboard loads without errors
- User profile options are visible

### Step 2: Navigate to Profile Edit Page
procedure: [[procedures/Navigate-to-Profile-Edit-Page]]

**Objective**: Reach the profile editing interface where the vulnerable VAT number field is located.

**Instructions**: From the dashboard, click on the profile or account settings link to access the edit page at https://partners.uber.com/profile/.

**Expected Output**: Profile edit form loads, including the VAT number input field.

**Success Indicators**:
- URL matches https://partners.uber.com/profile/
- Input fields for profile details are editable

### Step 3: Inject XSS Payload in VAT Field
procedure: [[procedures/Inject-XSS-Payload-in-VAT-Field]]

**Objective**: Insert a malicious JavaScript payload into the VAT number field to test for XSS injection.

**Instructions**: Locate the VAT number input field and enter the payload: `'><img src=x onerror=alert(0)> "><img src=x onerror=alert(0)> <script>alert(0)</script>`.

**Expected Output**: Payload is accepted without immediate validation errors.

**Success Indicators**:
- Payload text appears in the input field
- No client-side blocking occurs

### Step 4: Save Profile to Store Payload
procedure: [[procedures/Save-Profile-to-Store-Payload]]

**Objective**: Persist the injected payload in the user's profile for later execution upon viewing.

**Instructions**: Submit the profile form by clicking the save or update button.

**Expected Output**: Profile updates successfully, storing the payload server-side.

**Success Indicators**:
- Confirmation message for saved changes
- No server-side rejection of the input

## Attack Chain Summary

### Key Achievements

1. Successful injection of XSS payload into a stored profile field
2. Demonstration of self-XSS execution limited to the attacker's session
3. Identification of insufficient input sanitization in Uber's Partners Portal

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2024-01-01T00:00:00Z*
