---
tags:
  - sqli
  - bypass
  - authentication
  - web
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
procedures:
  - '[[procedures/Navigate-to-Teavana-Account-Page]]'
  - '[[procedures/Access-Teavana-Create-Shopping-Account-Form]]'
  - '[[procedures/Test-Partner-ID-Validation-Failure]]'
  - '[[procedures/Inject-SQL-Payload-to-Bypass-Validation]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Multi-stage manual attack exploiting SQL injection in the Teavana sign-up form
  to bypass partner ID validation, enabling unauthorized account creation
  without a valid Starbucks partner ID.
skill_level: intermediate
impact_level: medium
id: 8d2ec152-6d31-4518-a024-b7788483c343
created_at: '2025-12-14T03:46:20.660Z'
updated_at: '2025-12-14T03:46:20.660Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SQL Injection Bypass of Starbucks Partner ID Validation in Teavana Sign-Up Form

Multi-stage attack chain demonstrating a complete manual workflow to exploit SQL injection in the partner ID field of the Teavana sign-up form, allowing attackers to bypass validation checks and create accounts without a valid Starbucks partner ID. The attack was discovered through manual testing and leverages a classic SQL injection payload to alter query logic. A similar, less severe SQL injection behavior was observed in the Starbucks card addition feature, which alters error handling but does not enable data compromise or unauthorized actions.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Navigate to Account Page] --> B[Access Sign-Up Form]
    B --> C[Test Normal Input Failure]
    C --> D[Inject SQL Payload]
    D --> E[Bypass Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome or Firefox with developer tools for inspection)

### Target Environment

- Web platform
- Access to public-facing Teavana website (https://www.teavana.com)
- No special services or ports required beyond standard HTTPS (port 443)

### Initial Access Requirements

- No credentials needed
- Direct internet access to the target site
- No prior access required

## Detailed Attack Procedures

### Step 1: Navigate to the Account Page

procedure: [[procedures/Navigate-to-Teavana-Account-Page]]

**Objective**: Gain initial access to the Teavana account management section to begin the sign-up process.

**Instructions**: Open a web browser and directly visit the account page URL to load the sign-in interface.

**Expected Output**: The account page loads, displaying sign-in options and a link to create a new shopping account.

**Success Indicators**:
- Page loads without errors at https://www.teavana.com/us/en/account
- Sign-in and create account options are visible

### Step 2: Access the Create Shopping Account Form

procedure: [[procedures/Access-Teavana-Create-Shopping-Account-Form]]

**Objective**: Transition from the sign-in page to the account creation form where the vulnerable partner ID field is located.

**Instructions**: On the account page, click the 'Sign In' button, then select the 'Create Shopping Account' option to open the registration form.

**Expected Output**: The sign-up form appears, including fields for email, password, and the partner ID (partnerno) field.

**Success Indicators**:
- Form loads with input fields visible
- Partner ID field is present and editable

### Step 3: Test Partner ID Validation Failure

procedure: [[procedures/Test-Partner-ID-Validation-Failure]]

**Objective**: Verify the normal validation behavior by entering a standard invalid partner ID to confirm the bypass opportunity.

**Instructions**: In the partnerno field, enter a simple numeric value like '1234' and attempt to submit the form with other required fields filled (e.g., valid email and password).

**Expected Output**: The sign-up fails with an error message: 'We are unable to verify Starbucks partner ID'.

**Success Indicators**:
- Validation error displayed
- Form does not proceed to account creation

### Step 4: Inject SQL Payload to Bypass Validation

procedure: [[procedures/Inject-SQL-Payload-to-Bypass-Validation]]

**Objective**: Exploit the SQL injection vulnerability by injecting a payload that alters the query logic, allowing the sign-up to succeed without valid partner verification.

**Instructions**: Modify the input in the partnerno field to `'1234' OR 1=1` (without the outer quotes) and submit the form again with the same other details.

**Expected Output**: The sign-up succeeds unexpectedly, creating the account without partner ID verification.

**Success Indicators**:
- Account creation completes
- No validation error for partner ID
- User is redirected to the account dashboard or confirmation page

## Attack Chain Summary

### Key Achievements

1. Successfully bypassed Starbucks partner ID validation via SQL injection in the Teavana sign-up form.
2. Enabled unauthorized account creation for non-partners.
3. Identified similar SQL injection behavior in the Starbucks card addition feature, which redirects on invalid input but causes no further compromise.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01*
