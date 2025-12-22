---
tags:
  - account-takeover
  - twitter
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 67a85468-a3c9-40ee-9d7b-c7738ce040a3
created_at: '2025-12-14T17:33:06.116Z'
updated_at: '2025-12-14T17:33:06.116Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Reset-Password-Using-Old-Link

## Summary

This procedure completes the password reset using the persistent link from the old email, resulting in full account takeover for the now-updated email address.

## Description

With the reset page accessible via the old link, entering a new password modifies the account credentials. This grants control over the account tied to efgh@x.com, enabling data access, posting, or further compromise within minutes of the link's generation.

## Requirements

1. Active reset page from old link
2. Desired new password
3. Access to efgh@x.com for post-takeover verification

## Defense

Defensive measures and detection strategies:

- Multi-factor authentication on resets
- Alert on password changes shortly after email updates

## Objectives

1. Change account password
2. Achieve unauthorized access
3. Confirm takeover success

## Instructions

### Step 1: Enter New Password

**Context**: Submit the reset form.

On the reset page, input a strong new password and confirm it, then submit.

> Twitter processes the change without additional verification.

### Step 2: Verify Takeover

**Context**: Test the new credentials.

Log in using the new password; the account should respond to efgh@x.com queries.

> Full control is established.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[twitter]]
