---
id: proc-bitwarden-eject-owner
tags:
  - bitwarden
  - account-removal
  - takeover
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:29:36.669Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
---
# Eject-Original-Organization-Owner

## Summary

Using newly escalated owner privileges, this procedure removes the legitimate original owner from the organization, finalizing the takeover and denying them access to shared resources.

## Description

With accountB as owner, access the members management UI and select the original owner (accountA) for removal. Confirm the ejection, which revokes all access. The original owner can then verify loss of access by attempting to log in. This step completes the attack by isolating the legitimate user, allowing the attacker sole control over passwords and organization data.

## Requirements

1. Owner privileges on the organization (post-escalation)
2. Logged-in session for the escalated account
3. No recovery mechanisms in place for ejected users

## Defense

Defensive measures and detection strategies:

- Require multi-owner confirmation for ejections
- Send alerts to all owners on member removals
- Implement audit trails and reversal options for role changes

## Objectives

1. Remove original owner from organization
2. Verify ejection and loss of access
3. Secure attacker control

## Instructions

### Step 1: Access Members Management

**Context**: Use owner rights to manage membership.

Log in with accountB (owner). Go to organization settings > Members.

### Step 2: Remove Original Owner

**Context**: Eject accountA to complete takeover.

Locate accountA in the members list. Click the remove or delete icon next to it, confirm the action in any prompt, and apply the change.

### Step 3: Validate Ejection

**Context**: Ensure the original owner is fully denied access.

Log out of accountB. Log in with accountA and check the organizations list or dashboard. The organization should no longer appear, or access should be revoked.

Log out and back in with accountA to confirm persistence.

**Expected Output**: accountA no longer a member; organization inaccessible.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[bitwarden]]
- [[account-removal]]
- [[takeover]]
