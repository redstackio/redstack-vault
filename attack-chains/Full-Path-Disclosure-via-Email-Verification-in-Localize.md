---
tags:
  - information-disclosure
  - path-disclosure
  - php-error
  - reconnaissance
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Register-Account-and-Trigger-Verification]]'
  - '[[procedures/Access-Verification-Link]]'
  - '[[procedures/Observe-Path-Disclosure-Error]]'
step_count: 3
techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:06.273Z'
description: >-
  A reconnaissance attack exploiting a PHP error in the email verification
  process to disclose the server's internal file system path.
skill_level: beginner
impact_level: medium
id: 6e521e44-dc75-4a76-890d-dd9d6d634abc
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Exploit Public-Facing Application]]'
---
# Full Path Disclosure via Email Verification in Localize

Multi-stage attack chain demonstrating a reconnaissance workflow to extract server path information from a PHP fatal error during email verification.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Account Registration] --> B[Verification Link Access]
    B --> C[Error Observation and Path Extraction]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Firefox or Chrome)
- Email account for receiving verification (e.g., Gmail)

### Target Environment

- Web application with PHP backend
- Email verification feature enabled
- Accessible registration endpoint

### Initial Access Requirements

- Public internet access to the target site (http://www.localize.io)
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Account Registration
procedure: [[procedures/Register-Account-and-Trigger-Verification]]

**Objective**: Create a test account to initiate the email verification process.

**Instructions**: Navigate to the registration page and sign up using a controlled email address. This triggers an email with a verification link.

**Expected Output**: Confirmation of account creation and receipt of verification email.

**Success Indicators**:
- Account registered successfully
- Verification email received in inbox

### Step 2: Access Verification Link
procedure: [[procedures/Access-Verification-Link]]

**Objective**: Visit the verification URL to trigger the vulnerable endpoint.

**Instructions**: Open the verification link from the email in a web browser. Alternatively, use curl for scripted access:

```bash
curl -i "http://www.localize.io/verify/e6be646b24pdd3w6d5c27ppa9a267ee7"
```

**Expected Output**: HTTP response containing the page content or error.

**Success Indicators**:
- Link accessed without authentication issues
- Response received from server

### Step 3: Observe Path Disclosure Error
procedure: [[procedures/Observe-Path-Disclosure-Error]]

**Objective**: Capture and analyze the PHP fatal error revealing the server path.

**Instructions**: Inspect the page or response for error messages. The error should display the full path like "/var/www/vhosts/lvps178-77-99-228.dedicated.hosteurope.de/httpdocs_localize/index.php".

**Expected Output**: PHP fatal error message with internal file path.

**Success Indicators**:
- Error message contains server file system path
- Path can be used for further reconnaissance

## Attack Chain Summary

### Key Achievements

1. Successful account registration and email verification trigger
2. Access to vulnerable endpoint without authentication
3. Extraction of sensitive server path information for potential follow-on attacks like directory traversal

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance

---
*Last updated: 2023-10-01T00:00:00Z*
