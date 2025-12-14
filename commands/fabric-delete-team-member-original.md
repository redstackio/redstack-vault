---
data: >-
  DELETE
  /accounts/54aa37d8f61d7749430127ee?admin=true&app_id=54aeafc28bfc55053d000028
  HTTP/1.1

  Host: fabric.io
tags:
  - http
  - delete
  - legitimate
type: command
output: HTTP 200 OK or equivalent success response indicating deletion
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.799Z'
id: 3229f828-fb27-462e-b51d-d7b989e7a654
verified: false
validated: true
submitted: true
---
# fabric-delete-team-member-original

## Command

```http
DELETE /accounts/54aa37d8f61d7749430127ee?admin=true&app_id=54aeafc28bfc55053d000028 HTTP/1.1
Host: fabric.io
```

## Description

This HTTP DELETE request legitimately removes a team member (Hackermember) from the authenticated user's own application (HackerApp) in Fabric.io. It is intercepted for analysis and serves as the baseline for modification in exploitation scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| account_id | ID of the user account to delete (e.g., 54aa37d8f61d7749430127ee) | Yes |
| admin | Flag indicating admin-level action (true) | Yes |
| app_id | ID of the target application (e.g., 54aeafc28bfc55053d000028) | Yes |

## Examples

### Basic Usage

```http
DELETE /accounts/{account_id}?admin=true&app_id={app_id} HTTP/1.1
Host: fabric.io
```

### Advanced Usage

Include authentication headers (e.g., cookies from session) for replay.

```http
DELETE /accounts/{account_id}?admin=true&app_id={app_id} HTTP/1.1
Host: fabric.io
Cookie: session=abc123
```

## Expected Output

HTTP 200 OK response body may include {"success": true, "message": "User removed"} or similar, confirming deletion from the team.

## Related

- [[commands/fabric-delete-team-member-modified]]
- [[procedures/Intercept-Legitimate-DELETE-Request-with-Burp-Proxy]]
