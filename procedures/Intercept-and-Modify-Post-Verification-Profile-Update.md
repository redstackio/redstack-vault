---
id: proc-exness-profile-modify-001
tags:
  - api-modification
  - profile-update
type: procedure
tools:
  - '[[tools/Burp-Suite-CE]]'
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/patch-exness-personal-info]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:12.739Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# Intercept and Modify Post-Verification Profile Update

## Summary

This procedure intercepts the automatic profile update request triggered after KYC verification and modifies it via Burp Repeater to arbitrarily change personal information without re-authentication or validation, completing the identity spoofing attack.

## Description

The vulnerable PATCH endpoint /kyc_back/api/v2/surveys/personal_info lacks restrictions post-verification, allowing unauthenticated updates despite GUI locks. Intercepted during the flow, the JSON body is altered (e.g., name, DoB, address) and replayed. Targets my.exness.com API; expected: Successful update reflected in profile.

## Requirements

1. Verified account from prior steps
2. Burp Suite configured for interception
3. Knowledge of JSON payload structure

## Defense

Defensive measures and detection strategies:

- Enforce re-verification or auth tokens on profile updates
- Rate-limit API calls to personal info endpoints
- Log and alert on post-verification changes; integrate with audit trails

## Objectives

1. Exploit unauthenticated API for profile changes
2. Spoof identity for fraudulent use
3. Confirm bypass of KYC controls

## Instructions

### Step 1: Locate and Intercept Request

**Context**: Find the profile update request in Burp history after verification completes.

No command; use Burp GUI:
- In HTTP history, search for PATCH to /kyc_back/api/v2/surveys/personal_info.
- Right-click and "Send to Repeater".

> Request loaded in Repeater for modification.

### Step 2: Modify and Replay Request

**Context**: Alter JSON to new arbitrary values and send to update profile.

Execute [[commands/patch-exness-personal-info]] equivalent in Burp Repeater:

The body is modified to:
```json
{"first_name":"test-1","last_name":"test-2","test-3":"","dob":"1990-01-01","address":"test-4"}
```
- Click Send in Repeater.

> HTTP 200 with {"status":"OK"} confirms update.

### Step 3: Verify Changes

**Context**: Refresh profile pages to ensure updates persist.

No command; browser navigation:
- Visit https://my.exness.com/pa/settings/profile or https://my.exnesstrade.pro/settings/personalInfo.
- Check for new details.

> Profile shows modified info without re-verification prompt.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/patch-exness-personal-info]]

## Tools Used

- [[tools/Burp-Suite-CE]]

## Tags

- api-bypass
- request-replay
