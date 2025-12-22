---
tags:
  - shared-access
  - privilege-escalation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6d073d1e-7967-4e54-b5e2-af0182427d2d
created_at: '2025-12-13T23:52:55.370Z'
updated_at: '2025-12-13T23:52:55.370Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Accept-Shared-Access-Invitation

## Summary

Accept a shared administrator invitation in Streamlabs to gain temporary access to the victim's account dashboard.

## Description

Using the invitation link provided by the victim, log in with the attacker's credentials and confirm access. This links the accounts, allowing the attacker to view and modify the victim's settings as an admin. The access is temporary and tied to the invitation's expiration.

## Requirements

1. Valid invitation link from victim
2. Attacker's Streamlabs account credentials
3. Logged-in browser session

## Defense

Defensive measures and detection strategies:

- Review and revoke shared access regularly
- Alert on new access grants
- Limit shared access duration

## Objectives

1. Establish shared admin privileges
2. Prepare for impersonation
3. Avoid detection during acceptance

## Instructions

### Step 1: Open Invitation Link

**Context**: Use the attacker's session to accept without alerting the victim.

**Instructions**: Paste the invitation link into the attacker's logged-in browser and click to confirm.

**Expected Output**: Success message confirming access.

### Step 2: Check Access Grants

**Context**: Verify the new shared access entry.

**Instructions**: Navigate to the attacker's shared-access page to see the victim's account listed.

**Expected Output**: Victim's username with admin role.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[access-grant]]
- [[impersonation]]
