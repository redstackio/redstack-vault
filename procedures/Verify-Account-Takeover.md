---
tags:
  - account-takeover
  - verification
  - login
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Account Manipulation]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 0bb8db7c-a2fd-40ba-9bfc-bc4b7fd945b0
created_at: '2025-12-14T17:33:24.588Z'
updated_at: '2025-12-14T17:33:24.588Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Verify-Account-Takeover

## Summary

This procedure confirms the success of the CSRF attack by logging into the target Discourse site with the attacker's Yahoo account and accessing the victim's resources.

## Description

Post-payload delivery, the attacker tests the linkage by initiating a Yahoo-based login to Discourse. Successful authentication redirects through the callback, granting access to the victim's account due to the forced connection. Verification involves checking profile details, posts, and settings to ensure full control.

## Requirements

1. Successful payload processing by victim
2. Attacker's Yahoo credentials
3. Clean browser session without prior cookies

## Defense

Defensive measures and detection strategies:

- Audit logs for unexpected account linkages
- Multi-factor authentication on external providers
- Alert on login from new IP/user agents

## Objectives

1. Log in using the linked Yahoo account
2. Confirm access to victim's data
3. Validate full takeover

## Instructions

### Step 1: Attempt Yahoo Login

**Context**: Start the login process on Discourse using Yahoo.

No command executed; navigate to https://try.discourse.org and select Yahoo login option.

> Complete Yahoo authentication in the popup.

### Step 2: Follow Redirects

**Context**: Observe the post-login behavior to confirm connection.

No command executed; after login, expect redirect to https://try.discourse.org/auth/yahoo/null.

> This indicates successful linkage.

### Step 3: Access Victim's Account

**Context**: Verify control by interacting with the account.

No command executed; go to https://try.discourse.org/ and check the user's profile, posts, or preferences.

> Attacker can now perform actions as the victim.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[verification]]
