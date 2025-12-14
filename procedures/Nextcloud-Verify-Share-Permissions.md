---
tags:
  - nextcloud
  - verification
  - permissions
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:19.912Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 3c8df518-eef4-4658-bee8-3ef856170635
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Nextcloud-Verify-Share-Permissions

## Summary

This procedure verifies that the shared folder permissions are correctly limited to read and reshare, confirming no initial delete access for the recipient, which sets the stage for demonstrating the escalation vulnerability.

## Description

After receiving the share, User1 logs in to Nextcloud and tests access to /test/file.txt. They should be able to read and download the file but receive a permission denied error on delete attempts. This confirms the baseline permissions (17) before exploiting the reshare flaw in the sharing API, where implied delete from root mounts in View.php allows escalation.

## Requirements

1. User1 credentials with received share
2. Access to Nextcloud web UI for testing read/delete
3. Optional: API access for scripted verification

## Defense

Defensive measures and detection strategies:

- Regularly audit user permissions on shared resources
- Log and alert on failed delete attempts to detect probing

## Objectives

1. Confirm read access works
2. Verify delete is blocked
3. Validate setup for escalation

## Instructions

### Step 1: Test Read Access

**Context**: As User1, attempt to view or download /test/file.txt via web UI.

Navigate to shared /test in Files app, open file.txt.

> Expected: File contents displayed or downloadable.

### Step 2: Test Delete Access

**Context**: Attempt to delete /test/file.txt to confirm denial.

Right-click file.txt, select Delete; or use API DELETE if scripted.

> Expected: Error message like 'Insufficient permissions'.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- nextcloud
- verification
