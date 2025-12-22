---
id: proc-link-google-auth-001
name: Link-Google-Account-and-Authenticate
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.610Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques:
  - '[[T1078.004]]'
tags:
  - google-linkage
  - account-takeover
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Link-Google-Account-and-Authenticate

## Summary

This procedure completes the attack by logging out and authenticating with the attacker's Google account using the newly set email, linking it to the victim's Shopify staff or owner permissions.

## Description

After email update, the victim's account now points to the attacker's Google Apps email. Logging in via Google Apps authenticates the attacker's Google profile to the Shopify account, granting access to the victim's permissions. For owners, this can escalate to full control, especially when chained with XSS to trigger the update indirectly.

## Requirements

1. Email successfully updated to attacker's Google email
2. Access to the attacker's Google Apps account
3. No existing Google link on the target account

## Defense

Defensive measures and detection strategies:

- Require explicit confirmation for Google linkage changes
- Monitor authentication logs for unexpected Google logins
- Implement session invalidation on email updates

## Objectives

1. Establish persistent access via Google authentication
2. Verify takeover by accessing victim permissions
3. Chain with XSS for owner escalation if needed

## Instructions

### Step 1: Log Out of Current Session

**Context**: Clear the existing Shopify session to force re-authentication.

From the admin dashboard, click the profile icon and select "Log out".

### Step 2: Initiate Google Login

**Context**: Start the login process to trigger Google Apps authentication.

Navigate back to the Shopify login page and select "Log in with Google".

### Step 3: Authenticate with Attacker's Google Account

**Context**: Use the modified email to link the accounts.

Enter or select the attacker's Google Apps email during OAuth flow and complete authentication.

**Expected Output**: Redirect to Shopify dashboard with victim's permissions active.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

- [[T1078.004]]

## Commands Used


## Tools Used


## Tags

- google-auth
- linkage
- takeover
