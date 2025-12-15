---
tags:
  - account-takeover
  - login
  - mfa-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Account Manipulation]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 919d63c2-9d0d-4f75-94ed-ff3ec296214d
created_at: '2025-12-14T17:33:06.685Z'
updated_at: '2025-12-14T17:33:06.685Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Attempt-Account-Takeover-with-Reset-Password

## Summary

This procedure uses the reset password to log in as the target user, achieving account takeover and access to tenant resources, limited by MFA if enabled.

## Description

After resetting the password, the attacker attempts authentication with the victim's email and new password. Success grants full access to the account's features in the shared tenant, potentially allowing data exfiltration or further actions. MFA serves as a mitigation, prompting additional verification and blocking login if not bypassed.

## Requirements

1. Known new password from the reset step
2. Target user's email address
3. No MFA enabled on the account (or bypass method if applicable)

## Defense

Defensive measures and detection strategies:

- Mandate MFA for all users, especially in shared tenants
- Alert on login attempts from unusual IPs post-reset
- Implement session invalidation on password changes

## Objectives

1. Gain authenticated access to the victim's account
2. Explore and exploit accessible resources
3. Assess MFA's role in mitigation

## Instructions

### Step 1: Logout from Admin Session

**Context**: Clear current session to attempt victim login.

Log out of the tenant admin account to avoid session conflicts.

> Expected: Clean logout; application redirects to login page.

### Step 2: Attempt Login with New Credentials

**Context**: Use the reset password to authenticate as the victim.

Enter the target's email and the newly set password on the login form. Submit and observe the response.

> Expected: Login success or MFA prompt.

### Step 3: Handle MFA and Access Resources

**Context**: Proceed if login succeeds, or note mitigation.

If no MFA, access the dashboard; if MFA enabled, login fails at that stage. Document the outcome.

> Expected: Full account access without MFA; blocked with MFA.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[login]]
- [[mfa-bypass]]
