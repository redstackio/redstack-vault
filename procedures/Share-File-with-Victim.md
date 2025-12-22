---
tags:
  - sharing
  - xss-delivery
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.390Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6b275436-109c-4b00-8cae-e19d5a30b749
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Share-File-with-Victim

## Summary

This procedure shares the malicious file with the target victim in Nextcloud, making it available for linking in shared contexts like conversations.

## Description

Sharing the file ensures the victim can access it without suspicion, as it appears as a normal shared document. The vulnerability relies on the filename persisting through sharing. This step sets up the delivery mechanism for the XSS payload in the Talk app's projects feature.

## Requirements

1. Malicious file created in attacker's storage
2. Victim's user account known and shareable
3. Permissions to share files with other users

## Defense

Defensive measures and detection strategies:

- Review shared files for suspicious names before accepting
- Enable notifications for all shares and audit them
- Sanitize filenames on share receipt

## Objectives

1. Grant victim read access to the malicious file
2. Maintain stealth by not altering file content
3. Prepare for integration into conversation projects

## Instructions

### Step 1: Open File Details

**Context**: Locate the malicious file and initiate sharing.

In the Files app, select the malicious file from step 1 and click the share icon.

### Step 2: Add Victim as Recipient

**Context**: Assign sharing permissions to the victim.

In the sharing dialog, search for and select the victim user, then set permissions to 'Can view' or 'Can edit' as needed.

**Expected Output**: Share link or confirmation that the victim has access; victim sees the file in their shared items.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[sharing]]
- [[nextcloud]]
