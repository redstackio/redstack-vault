---
id: proc-nextcloud-share-conflict
tags:
  - nextcloud
  - sharing
  - group-share
  - privilege-escalation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
  - Nextcloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:29:19.889Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[External Remote Services]]'
---
# Share-Conflicting-Storage-with-Group

## Summary

This procedure enables the attacker to share the conflicting external SFTP storage mount with the target group in Nextcloud 10.0, propagating the mask to other members and completing the privilege escalation setup.

## Description

After creating a conflicting mount, the attacker shares it via the Nextcloud UI with the group (e.g., 'samplegroup' including admin and victim). Due to the naming conflict, this overrides the admin's shared local storage for group members, who will see only the attacker's SFTP content. This abuses the sharing feature without unique name checks, allowing non-privileged control over group resources. Prerequisites include the conflicting mount; outcomes expose victims to masked or manipulated files.

## Requirements

1. Existing conflicting external storage mount named 'localstrg' (from prior procedure)
2. Attacker account in 'samplegroup' with sharing permissions
3. Nextcloud 10.0 with group sharing enabled
4. Web UI access

## Defense

Defensive measures and detection strategies:

- Disable external storage sharing for non-admin users
- Implement name collision detection in sharing workflows
- Log and alert on duplicate storage shares within groups
- Use role-based access to limit storage management

## Objectives

1. Distribute the conflicting mount to group members
2. Trigger masking of admin resources
3. Escalate influence over shared group content

## Instructions

### Step 1: Access the Conflicting Storage

**Context**: Locate the newly created SFTP mount in the UI for sharing.

Log in as attacker, go to Files, find 'localstrg' (SFTP), and select the share option.

> Confirm the storage shows attacker-controlled files.

### Step 2: Share with Group

**Context**: Propagate the mask by adding the group as a share recipient.

In the sharing dialog, search for and add 'samplegroup', confirm the share; enable any preview or edit permissions as needed.

> UI submission; no errors if permissions allow. Notification may appear for group members.

### Step 3: Confirm Share Propagation

**Context**: Verify the share is active and ready for masking.

Check the sharing tab on 'localstrg'; ensure 'samplegroup' is listed. Optionally, log in as another group member (non-victim) to preview.

> Expected: Share visible; masking effect pending victim access.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[External Remote Services]] External Remote Services

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[nextcloud]]
- [[sharing]]
- [[group-share]]
- [[privilege-escalation]]
