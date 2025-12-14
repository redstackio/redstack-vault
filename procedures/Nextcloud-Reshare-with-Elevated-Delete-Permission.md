---
tags:
  - nextcloud
  - reshare
  - escalation
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/nextcloud-reshare-with-delete-permission]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:19.909Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b1705603-567f-48eb-ac14-e38ac315318f
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Nextcloud-Reshare-with-Elevated-Delete-Permission

## Summary

This procedure exploits the Nextcloud sharing vulnerability by resharing a received folder with unauthorized delete permissions added, leveraging the propagation of implied delete from root mounts in View.php to escalate privileges.

## Description

User1, with only read+reshare (17) on /test, uses the sharing API to reshare to User2 with permissions=25 (read=1 + reshare=16 + delete=8). The root cause is in lib/private/Files/View.php at line 1389, where PERMISSION_DELETE is added to root mounts for unsharing, but this incorrectly allows adding delete to sub-shares. This enables malicious resharing beyond original permissions, affecting Nextcloud master and 16.x.

## Requirements

1. User1 credentials with received share on /test
2. curl tool for API interaction
3. Target Nextcloud API endpoint accessible (e.g., port 8081)

## Defense

Defensive measures and detection strategies:

- Patch Nextcloud to fix View.php permission propagation
- Monitor OCS API calls for anomalous permission values in shares
- Disable resharing if not needed

## Objectives

1. Reshare with escalated delete permission
2. Grant User2 unauthorized delete access
3. Exploit implied permission bug

## Instructions

### Step 1: Prepare Reshare Request

**Context**: Authenticate as User1 and target the sharing API endpoint.

Ensure User2 exists in Nextcloud.

> Expected: User2 available for sharing.

### Step 2: Execute Reshare

**Context**: Send POST to create reshare with permissions=25.

**Command** ([[commands/nextcloud-reshare-with-delete-permission]]):
```bash
curl --user user1:user1 "http://172.17.0.1:8081/ocs/v1.php/apps/files_sharing/api/v1/shares" -H "OCS-APIRequest: true" -X POST --data 'path=/test&shareType=0&shareWith=user2&permissions=25'
```

> This creates a user share (shareType=0) to User2. Expected output: XML response with <statuscode>100</statuscode> for success.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used

- [[commands/nextcloud-reshare-with-delete-permission]]

## Tools Used

- [[tools/curl]]

## Tags

- nextcloud
- escalation
