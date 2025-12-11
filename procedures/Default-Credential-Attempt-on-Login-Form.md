---
tags:
  - cred-test
  - auth-bypass
type: procedure
tools:
  - '[[tools/jexboss]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-path-manipulation]]'
  - '[[commands/curl-directory-traversal]]'
  - '[[commands/jexboss-exploit]]'
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[Default Accounts]]'
id: 840598ff-5cbc-40af-990f-2880e012aee5
created_at: '2025-12-11T06:10:24.960Z'
updated_at: '2025-12-11T06:10:24.960Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---
# Default Credential Attempt on Login Form

## Summary

This procedure tests default credentials on a discovered login form, often revealing misconfigurations or red herrings in web applications.

## Description

Targeting the /josso/signin form, default credentials like 'admin'/'admin' are attempted, resulting in a success message but backend error. This step confirms credential handling and potential disables after attempts, serving as reconnaissance for further attacks.

## Requirements

1. Access to the login endpoint
2. HTTP POST capability
3. List of common default credentials

## Defense

Defensive measures and detection strategies:

- Enforce strong password policies and disable defaults
- Log and alert on failed login attempts

## Objectives

1. Test for weak authentication
2. Trigger errors for information disclosure
3. Identify red herrings in the attack path

## Instructions

### Step 1: Submit Default Credentials

**Context**: POST default creds to the form and observe response.

**Command** ([[commands/curl-path-manipulation]]):
```bash
curl -X POST "http://subdomain.starbucks.com/josso/signin" -d "username=admin&password=admin"
```

> Expect success message with error; note disable after attempt.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

- [[Default Accounts]]

## Commands Used

- [[commands/curl-path-manipulation]]

## Tools Used



## Tags

- [[cred-test]]
- [[auth-bypass]]
