---
id: proc-ufsimporturl-exploit-001
name: Invoke-ufsImportURL-for-Other-User-Avatar
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.483Z'
tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - access-control
  - file-upload
  - idor
  - rocket-chat
commands:
  - '[[commands/invoke-ufsimporturl-ddp]]'
platforms:
  - Web
  - Node.js
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---

# Invoke-ufsImportURL-for-Other-User-Avatar

## Summary

This procedure exploits the lack of userId validation in Rocket.Chat's ufsImportURL API method (FileUpload.js line 210) to upload an image from a URL and assign it as an avatar to any other user, bypassing access controls and enabling privacy violations or social engineering.

## Description

The attack targets the ufsImportURL method in the FileUpload module, which imports files from URLs into the 'Avatars' store without checking if the provided userId matches the authenticated user. This IDOR-like vulnerability allows arbitrary avatar modification. The scenario involves an authenticated low-privilege user sending a crafted DDP payload over WebSocket. Prerequisites: Authenticated session and known target userId. Outcomes: Unauthorized avatar change, stored in GridFS, visible upon client refresh.

## Requirements

1. Authenticated WebSocket session to Rocket.Chat
2. Target userId (obtainable via API enumeration if needed)
3. Publicly accessible image URL for upload
4. WebSocket client or browser console for DDP calls

## Defense

Defensive measures and detection strategies:

- Validate userId against authenticated user in FileUpload.js
- Log and alert on avatar upload attempts with mismatched userIds
- Restrict file upload endpoints to authorized roles only
- Use input sanitization and rate limiting on ufsImportURL

## Objectives

1. Bypass access control to modify another user's avatar
2. Demonstrate privacy impact through unauthorized data alteration
3. Highlight storage backend risks like GridFS exposure

## Instructions

### Step 1: Prepare DDP Payload

**Context**: Construct the JSON payload for the ufsImportURL method, including the target userId in file metadata.

No command; manually format the payload with image URL, file details, and userId.

> Payload ready for transmission, ensuring 'Avatars' store is specified.

### Step 2: Send DDP Method Call

**Context**: Invoke the method via authenticated WebSocket to trigger the upload.

**Command** ([[commands/invoke-ufsimporturl-ddp]]):
```json
{"msg":"method","method":"ufsImportURL","params":["https://radicallyopensecurity.com/images/ros-logo.gif",{"name": "ros.jpg", "extension": "jpg", "type": "text/plain", "userId": "<TARGET_USER_ID>"},"Avatars"],"id":"15"}
```

> Send via WebSocket; expect a success response like {"msg":"result", "result": true, "id": "15"}. The image is fetched, uploaded, and set as the target's avatar.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/invoke-ufsimporturl-ddp]]

## Tools Used


## Tags

- access-control
- file-upload
- idor
- rocket-chat
