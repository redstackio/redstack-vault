---
tags:
  - 2fa-bypass
  - access-control
  - hackerone
  - business-logic
type: attack_chain
tools: []
tactics:
  - '[[Defense Evasion]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2024-01-01T12:00:00Z'
procedures:
  - '[[procedures/Create-Test-Programs-in-HackerOne]]'
  - '[[procedures/Configure-2FA-Requirement-for-Program]]'
  - '[[procedures/Submit-Report-from-Non-2FA-Account]]'
  - '[[procedures/Transfer-Report-to-2FA-Required-Program]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:48.007Z'
description: >-
  Demonstrates a business logic vulnerability allowing reports from non-2FA
  enabled users to bypass 2FA requirements when transferred to restricted
  programs by a program manager.
skill_level: intermediate
impact_level: low
id: ab041d31-39a9-47c8-b3e4-0a810d582814
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Bypass 2FA Submission Requirement via Report Transfer in HackerOne

Multi-stage attack chain demonstrating a complete attack workflow exploiting a lack of validation in HackerOne's report transfer feature, allowing non-2FA authenticated reports to enter 2FA-mandated programs.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Test Programs] --> B[Configure 2FA Requirement]
    B --> C[Submit Non-2FA Report]
    C --> D[Transfer to 2FA Program]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (web-based UI actions only)

### Target Environment

- HackerOne platform (web application)
- Required services/ports: Standard HTTPS (443)
- Network access requirements: Internet access to hackerone.com

### Initial Access Requirements

- HackerOne account with program manager privileges for test programs
- A secondary account without 2FA enabled
- No prior access beyond standard user registration

## Detailed Attack Procedures

### Step 1: Create Test Programs
procedure: [[procedures/Create-Test-Programs-in-HackerOne]]

**Objective**: Set up two programs to simulate restricted and non-restricted environments for testing report submission and transfer.

**Instructions**: Log in to HackerOne as a program owner or admin, navigate to the programs dashboard, and create two new programs named 'h1R' (non-restricted) and 'h1B' (to be 2FA-restricted). Ensure you have manager access to both.

**Expected Output**: Two active test programs visible in the dashboard.

**Success Indicators**:
- Programs 'h1R' and 'h1B' created successfully
- Manager privileges confirmed for both

### Step 2: Configure 2FA Requirement
procedure: [[procedures/Configure-2FA-Requirement-for-Program]]

**Objective**: Enable 2FA enforcement for new report submissions on one program to establish the restricted policy.

**Instructions**: Access the settings for the 'h1B' program, go to the 'Submission Requirements' section, and toggle on the option to require 2FA for new report submissions. Save the changes.

**Expected Output**: Confirmation that 2FA is now mandated for 'h1B' submissions.

**Success Indicators**:
- 2FA requirement enabled in 'h1B' settings
- Attempting direct submission to 'h1B' from non-2FA account fails validation

### Step 3: Submit Report from Non-2FA Account
procedure: [[procedures/Submit-Report-from-Non-2FA-Account]]

**Objective**: Create a vulnerability report using an account without 2FA to the non-restricted program.

**Instructions**: Log in to HackerOne with a non-2FA enabled account, navigate to the 'h1R' program page, and submit a test vulnerability report with sample details (e.g., a benign finding).

**Expected Output**: Report successfully submitted and visible in the 'h1R' program's report list.

**Success Indicators**:
- Report ID generated for the submission
- No 2FA prompt during submission to 'h1R'

### Step 4: Transfer Report to 2FA-Required Program
procedure: [[procedures/Transfer-Report-to-2FA-Required-Program]]

**Objective**: Move the non-2FA report to the restricted program, bypassing the 2FA check due to lack of validation on transfer.

**Instructions**: Switch to the program manager account, open the report in 'h1R', select the transfer option, choose 'h1B' as the destination, and confirm the transfer.

**Expected Output**: Report successfully transferred to 'h1B' without requiring reporter 2FA.

**Success Indicators**:
- Report appears in 'h1B' program's inbox
- No error or 2FA enforcement during transfer

## Attack Chain Summary

### Key Achievements

1. Successfully created test environments to isolate the vulnerability.
2. Configured a 2FA policy that is bypassed via transfer.
3. Submitted and transferred a report, undermining the security control.
4. Demonstrated low-severity impact requiring privileged access but exposing policy enforcement flaws.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Defense Evasion]]

---
*Last updated: 2024-01-01T12:00:00Z*
