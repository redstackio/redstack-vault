---
id: proc-nextcloud-create-conflict-mount
tags:
  - nextcloud
  - external-storage
  - sftp
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
  - '[[T1133.003]]'
updated_at: '2025-12-14T17:29:19.891Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[T1133.003]]'
---
# Create-Conflicting-External-Storage-Mount

## Summary

This procedure allows a non-privileged user in Nextcloud 10.0 to create an external SFTP storage mount with a name identical to an existing admin-shared local storage, setting the stage for masking the admin's resources within a shared group.

## Description

In Nextcloud 10.0, the external storage feature lacks unique name enforcement across users in shared groups. An attacker can exploit this by mounting a personal SFTP storage with the same name as the admin's shared local storage (e.g., 'localstrg'). When shared, this conflicts with and masks the admin's mount for other group members, enabling the attacker to hide legitimate files or expose controlled content. This requires group membership and UI access; outcomes include resource override without admin privileges.

## Requirements

1. Nextcloud 10.0 instance with external storage enabled
2. Attacker account in a group with an admin-shared storage (e.g., 'samplegroup')
3. Access to an external SFTP server controlled by the attacker (host, root, credentials)
4. Web browser for Nextcloud UI access

## Defense

Defensive measures and detection strategies:

- Enforce unique storage names via custom validation in Nextcloud config
- Monitor external storage creations for name conflicts in shared groups using audit logs
- Restrict non-admin users from creating/sharing external storages
- Regularly audit shared resources for masking anomalies

## Objectives

1. Establish a conflicting mount to override admin resources
2. Prepare for group-wide propagation of the mask
3. Achieve effective privilege escalation through resource control

## Instructions

### Step 1: Log In as Attacker and Access Settings

**Context**: Gain access to the external storage configuration UI to initiate mount creation.

Log into Nextcloud as the attacker user and navigate to personal Settings > External Storages.

> Ensure you are in the correct group ('samplegroup') where the admin has already shared a storage named 'localstrg'.

### Step 2: Configure and Create SFTP Mount

**Context**: Set up the conflicting storage using SFTP to match the admin's name exactly.

Add a new external storage: Select SFTP as type, name it 'localstrg', enter SFTP host details (e.g., host IP, root path '/'), provide username and password for the attacker-controlled SFTP server, check 'Enable sharing'.

> No command execution; all via UI form submission. Verify mount by checking if it appears in the list without errors.

### Step 3: Validate Mount Functionality

**Context**: Test the new mount to ensure it loads attacker-controlled files.

Navigate to Files in the UI and access 'localstrg' as the attacker; confirm SFTP files are visible and editable.

> Expected: Attacker sees their own SFTP content; no visibility of admin's local storage yet.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[External Remote Services]] External Remote Services

### Sub-Techniques

- [[T1133.003]] External Remote Services: Drive-by Compromise (adapted for storage masking)

## Commands Used


## Tools Used


## Tags

- [[nextcloud]]
- [[external-storage]]
- [[sftp]]
- [[privilege-escalation]]
