---
id: proc-nextcloud-verify-masking
tags:
  - nextcloud
  - verification
  - masking
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
  - '[[Archive Collected Data]]'
updated_at: '2025-12-14T17:29:19.884Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Archive Collected Data]]'
---
# Verify-Masking-on-Victim

## Summary

This procedure confirms the success of the privilege escalation in Nextcloud 10.0 by accessing the masked storage as a victim user, ensuring only the attacker's files are visible and the admin's are hidden.

## Description

Post-sharing, the victim (another group member) accesses 'localstrg' via the Nextcloud UI, where the conflicting SFTP mount overrides the admin's local storage due to name collision. This verifies the escalation, as the non-privileged attacker has effectively controlled group-visible resources. No additional setup needed beyond prior steps; outcomes demonstrate hiding of legit files or exposure to attacker content, highlighting the vulnerability.

## Requirements

1. Conflicting storage shared with group (from prior procedures)
2. Victim account in 'samplegroup'
3. Nextcloud 10.0 UI access for victim
4. Admin's original 'localstrg' was accessible pre-attack

## Defense

Defensive measures and detection strategies:

- Audit user views of shared storages for discrepancies
- Implement storage name namespaces per user/group
- Enable anomaly detection for resource access patterns
- Train admins to use unique, descriptive storage names

## Objectives

1. Validate masking effect on non-attacker group member
2. Confirm privilege escalation impact
3. Identify potential for broader abuse

## Instructions

### Step 1: Log In as Victim

**Context**: Switch to victim perspective to test visibility.

Log into Nextcloud as the victim user in 'samplegroup'.

> Ensure victim had prior access to admin's 'localstrg'.

### Step 2: Access the Storage

**Context**: Attempt to view the shared 'localstrg' to observe masking.

Navigate to Files > External Storages or search for 'localstrg'; open the folder.

> UI navigation; load the directory listing.

### Step 3: Inspect Content

**Context**: Confirm only attacker's files are shown, masking admin's.

Browse files in 'localstrg'; verify absence of admin's local files and presence of SFTP content only.

> Expected: Victim sees attacker-controlled files exclusively; no admin content.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Archive Collected Data]] Archive Collected Data (adapted for masking verification)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[nextcloud]]
- [[verification]]
- [[masking]]
- [[privilege-escalation]]
