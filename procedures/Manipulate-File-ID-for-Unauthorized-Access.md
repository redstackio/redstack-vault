---
tags:
  - idor
  - exploit
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:28.667Z'
sub_techniques: []
id: 1d9a15b4-ab3f-4ac6-aabe-45c0d6d5df77
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Manipulate-File-ID-for-Unauthorized-Access

## Summary

This procedure exploits the IDOR vulnerability by substituting another user's file ID into the Compose Email attachment request, allowing the system to fetch unauthorized file data without proper checks.

## Description

Once the file ID format is known, this procedure intercepts and modifies the API request in the Lark Compose Email function to reference a target file ID obtained from another user. The attack assumes horizontal privilege escalation where the attacker has a valid session but targets another user's resources. In the web environment, this is done via request tampering. Success results in the server returning the private file's content or metadata.

## Requirements

1. Valid Lark session
2. Known target file ID (e.g., from enumeration or leak)
3. Browser developer tools or proxy for request modification

## Defense

Defensive measures and detection strategies:

- Enforce user-specific access controls on all object references
- Rate-limit file access requests and alert on cross-user patterns
- Validate file ownership against session user ID on every request

## Objectives

1. Tamper with the file ID in the attachment request
2. Trigger server response with unauthorized data
3. Confirm access to non-owned resources

## Instructions

### Step 1: Intercept and Modify Request

**Context**: Use tools to alter the file ID parameter in the API call.

In the Compose Email interface, initiate a file attachment request. Use the browser's Network tab or a proxy to capture the request. Edit the JSON payload or query parameter for the file ID (e.g., change "file_id": "your_id" to "file_id": "target_user_id"). Replay the modified request.

> The server will process the request as if the file belongs to the current user, returning a success response with the target file's details due to missing authorization.

**Expected Output**: 200 OK response containing target file metadata.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[idor]]
- [[exploit]]
- [[web]]
