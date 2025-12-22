---
tags:
  - idor
  - web
  - authorization-bypass
  - moneybird
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Moneybird-Accountant-Company-Edit-Endpoint-via-IDOR]]'
  - '[[procedures/Modify-Company-Name-Without-Authorization]]'
step_count: 2
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:29.521Z'
description: >-
  A multi-step attack exploiting an Insecure Direct Object Reference (IDOR)
  vulnerability in the Moneybird web application to access and modify accountant
  company details without authorization.
skill_level: beginner
impact_level: low
id: 09b2f483-dac8-4ec6-819a-9ac273a90622
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# IDOR in Moneybird Accountant Company Edit Endpoint Allowing Unauthorized Name Modification

Multi-stage attack chain demonstrating exploitation of an IDOR vulnerability in the Moneybird web application, allowing unauthorized access and modification of accountant company details.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Edit Endpoint] --> B[Modify Company Details]
    B --> C[Unauthorized Changes Applied]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser or [[tools/curl]]

### Target Environment

- Web platform (Moneybird application)
- Required services/ports: HTTPS (443)
- Network access requirements: Internet access to moneybird.com

### Initial Access Requirements

- Valid user session in Moneybird (authenticated as a non-admin user)
- Knowledge of target accountant company ID
- No elevated privileges needed

## Detailed Attack Procedures

### Step 1: Access Edit Endpoint
procedure: [[procedures/Access-Moneybird-Accountant-Company-Edit-Endpoint-via-IDOR]]

**Objective**: Gain unauthorized access to the edit page for an accountant company's details by manipulating the object reference in the URL.

**Instructions**: Navigate to the Moneybird edit endpoint using a manipulated company ID. Use a web browser or curl to fetch the page:

```bash
curl -H "Cookie: session=your_session_cookie" https://moneybird.com/user/accountant_company/edit?company_id=TARGET_COMPANY_ID
```

Replace `TARGET_COMPANY_ID` with the ID of the accountant company you wish to target (e.g., obtained from previous enumeration or guesswork).

**Expected Output**: The edit form for the target company's details loads without authorization errors, displaying fields like company name.

**Success Indicators**:
- Edit form accessible for a company not owned by the user
- No 403 Forbidden or access denied response

### Step 2: Modify Company Name Without Authorization
procedure: [[procedures/Modify-Company-Name-Without-Authorization]]

**Objective**: Submit changes to the company name or other details, bypassing permission checks due to the IDOR flaw.

**Instructions**: Fill in the edit form with modified values (e.g., change the company name) and submit. Using curl to simulate a POST request:

```bash
curl -X POST -H "Cookie: session=your_session_cookie" -d "company_name=Modified Company Name&company_id=TARGET_COMPANY_ID" https://moneybird.com/user/accountant_company/edit
```

Adjust form parameters based on the actual HTML form data observed in Step 1.

**Expected Output**: Success response (e.g., 200 OK or redirect to updated page) confirming the modification without errors.

**Success Indicators**:
- Company name updated in the application for the target entity
- No permission-related errors during submission

## Attack Chain Summary

### Key Achievements

1. Unauthorized access to sensitive accountant company edit functionality
2. Successful modification of company name without ownership
3. Demonstration of IDOR leading to potential data integrity issues

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
