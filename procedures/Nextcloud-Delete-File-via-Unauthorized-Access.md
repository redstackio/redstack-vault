---
tags:
  - nextcloud
  - deletion
  - unauthorized
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/nextcloud-delete-file-via-dav]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:19.905Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: bfa4c5cf-cc9b-47c4-8bc1-1b1a9d070b00
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Nextcloud-Delete-File-via-Unauthorized-Access

## Summary

This procedure demonstrates the impact of the privilege escalation by using the elevated delete permission on the reshared folder to unauthorizedly delete the original owner's file via WebDAV.

## Description

After resharing with delete permission, User2 can access and delete /test/file.txt, which removes it from User0's storage. This exploits the vulnerability's propagation issue, allowing non-owners (or self via groups) to delete files. Applicable to Nextcloud's DAV endpoints, confirming the escalation from read to delete.

## Requirements

1. User2 credentials with the reshared folder
2. curl for WebDAV DELETE request
3. DAV endpoint accessible (e.g., /remote.php/dav/)

## Defense

Defensive measures and detection strategies:

- Enable file delete auditing in Nextcloud
- Use immutable shares or restrict resharing chains
- Monitor DAV DELETE requests for unauthorized users

## Objectives

1. Delete file using escalated permissions
2. Confirm impact on original owner
3. Validate vulnerability exploitation

## Instructions

### Step 1: Access Reshared File

**Context**: Log in as User2 and verify /test/file.txt is visible with delete option.

Via web UI: Navigate to shared /test.

> Expected: File present and deletable.

### Step 2: Execute Deletion

**Context**: Use WebDAV DELETE to remove the file.

**Command** ([[commands/nextcloud-delete-file-via-dav]]):
```bash
curl --user user2:user2 "http://172.17.0.1:8081/remote.php/dav/files/user2/test/file.txt" -H "OCS-APIRequest: true" -X DELETE
```

> Expected output: HTTP 204 No Content, file removed.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used

- [[commands/nextcloud-delete-file-via-dav]]

## Tools Used

- [[tools/curl]]

## Tags

- nextcloud
- deletion
