---
id: proc-verify-deletion-impact
tags:
  - impact-verification
  - account-discovery
  - web
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:30.051Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Verify-Account-Deletion-Impact

## Summary

This procedure confirms the success of the IDOR exploitation by checking that the victim's account is deleted and all associated data is permanently lost on community.ubnt.com.

## Description

Post-exploitation, the victim's profile becomes inaccessible, and content like posts and badges vanishes. Browser cache may temporarily display old data, so clearing it ensures accurate verification. Victims can re-register but lose everything, highlighting the critical impact on user experience and data integrity.

## Requirements

1. Access to the forum post-deletion
2. Victim's username or ID for checks
3. Ability to clear browser cache

## Defense

Defensive measures and detection strategies:

- Implement soft deletes with recovery windows instead of hard deletion
- Notify users of deletion attempts via email
- Audit logs for unusual deletion patterns

## Objectives

1. Validate account and data removal
2. Assess recovery feasibility for victim
3. Document impact for reporting

## Instructions

### Step 1: Check Profile Access

**Context**: Attempt to view the victim's profile to confirm deletion.

Navigate to the victim's profile URL (e.g., https://community.ubnt.com/index.php?/profile/12345).

> Expect a 404 error or "user not found" message.

### Step 2: Verify Data Loss

**Context**: Search for victim content and test re-registration.

Use forum search for victim's username or posts; clear cache (Ctrl+Shift+R) if needed. Attempt to register a new account with the victim's old username.

> No posts, badges, or history appear; new account is empty.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[impact-verification]]
- [[account-discovery]]
- [[web]]
