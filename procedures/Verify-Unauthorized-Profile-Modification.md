---
tags:
  - idor
  - web
  - verification
type: procedure
tools:
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: e28cb840-a1ce-4dff-8980-3c803b60463f
created_at: '2025-12-14T17:25:47.545Z'
updated_at: '2025-12-14T17:25:47.545Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Unauthorized-Profile-Modification

## Summary

This procedure checks the victim's profile in their session to confirm the IDOR exploitation resulted in unauthorized changes.

## Description

After forwarding the modified request from the attacker session, refresh the victim's profile page in Chrome to observe alterations to fields like username, mobile number, residential address, company name, and size. This validates the vulnerability, showing no victim interaction was needed, with outcomes confirming high-impact risks like impersonation.

## Requirements

1. Active victim session in [[tools/Google-Chrome]]
2. Recent exploitation from previous step

## Defense

Defensive measures and detection strategies:

- Real-time notifications for profile changes
- Immutable audit trails for modifications
- User confirmation required for sensitive updates

## Objectives

1. Visually confirm profile alterations
2. Assess modifiable fields and impact
3. Document evidence for reporting

## Instructions

### Step 1: Refresh Victim Profile Page

**Context**: Reload to display changes.

No specific command; browser action.

> In Chrome, navigate to or refresh https://mtnmobad.mtnbusiness.com.ng/#/userProfile. Expected output: Updated details visible, e.g., changed username or address.

### Step 2: Document Changes

**Context**: Screenshot or note modifications.

No specific command; manual.

> Compare pre- and post-exploit profile. Expected output: Evidence of unauthorized edits, such as new mobile number.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Chrome]]

## Tags

- [[idor]]
- [[web]]
- [[verification]]
