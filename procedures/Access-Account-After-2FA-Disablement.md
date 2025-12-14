---
tags:
  - account-takeover
  - login-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:12.280Z'
skill_level: low
impact_level: high
detection_risk: high
sub_techniques: []
id: c3122b26-023d-4cd3-8f0f-b9d0c1ff676d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Account-After-2FA-Disablement

## Summary

This procedure logs into the HackerOne account using only email and password after the 2FA auto-disablement, achieving full account takeover.

## Description

Once the 24-hour window expires without cancellation, the 2FA protection is removed, allowing standard credential-based login. This exploits the improper access control in the reset flow, granting the attacker complete control over the victim's HackerOne account, including report access, settings changes, and further actions. The target is the post-reset login state on https://hackerone.com. Prerequisites include successful prior steps. Expected outcome is unrestricted account access.

## Requirements

1. 24 hours elapsed since reset trigger
2. Victim has not canceled the request
3. Valid email and password

## Defense

Defensive measures and detection strategies:

- Implement audit logs for 2FA disablements and alert on them
- Require re-enablement of 2FA post-reset with additional verification
- Use behavioral analytics to detect logins immediately after disablement

## Objectives

1. Confirm 2FA is disabled by absence of prompt
2. Gain full access to account resources
3. Validate takeover for further exploitation

## Instructions

### Step 1: Return to Login Page

**Context**: Attempt login after the waiting period.

Navigate to https://hackerone.com/account/sign_in.

> Page loads normally without prior session data.

### Step 2: Submit Credentials

**Context**: Enter details and observe no 2FA requirement.

Input email and password, then click submit.

> If successful, no TOTP field or reset option appears; direct to dashboard.

### Step 3: Verify Access

**Context**: Confirm full control.

Once logged in, navigate to sensitive areas like reports or settings to ensure unrestricted access.

> Account functions normally; 2FA status shows as disabled.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[login-bypass]]
