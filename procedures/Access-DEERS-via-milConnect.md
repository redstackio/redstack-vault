---
id: proc-uuid-5
tags:
  - data-access
  - personnel-records
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:12.241Z'
skill_level: beginner
impact_level: critical
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-DEERS-via-milConnect

## Summary

This procedure submits compromised myPay credentials through the bypassed milConnect form to gain unauthorized access to the target's full DEERS personnel profile.

## Description

DEERS (Defense Enrollment Eligibility Reporting System) is accessible via milConnect authentication using myPay credentials. After enabling the form, submission grants comprehensive military personnel data. This concludes the chain with high-impact data exposure. Prerequisites: Bypassed form and credentials.

## Requirements

1. Enabled milConnect myPay login form
2. Compromised credentials
3. Browser session on milConnect

## Defense

Defensive measures and detection strategies:

- Decouple authentication between myPay and DEERS with separate MFA
- Audit logs for cross-service logins
- Behavioral analytics for unusual access patterns

## Objectives

1. Authenticate to milConnect with stolen creds
2. Retrieve full personnel records
3. Enable data exfiltration or modification

## Instructions

### Step 1: Input Credentials

**Context**: Fill the enabled form.

Enter username: targetuser, password: newpass into the fields.

### Step 2: Submit Form

**Context**: Trigger backend authentication.

Click the enabled submit button to log in.

**Expected Output**: Successful redirect to DEERS profile with complete records.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- deers-access
- linked-services
