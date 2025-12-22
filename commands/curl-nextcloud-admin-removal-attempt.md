---
data: >-
  curl -X POST
  'http://target-nextcloud/index.php/settings/ajax/togglegroups.php' -H
  'Content-Type: application/x-www-form-urlencoded' -H 'Cookie:
  oc_session=your_session; requesttoken=your_token' -d
  'username=admin&group=admin'
tags:
  - nextcloud
  - http-request
  - admin-removal
type: command
output: >-
  {"data":{"message":"Admins can't remove themself from the admin
  group"},"status":"error"}
executor: bash
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.569Z'
id: 040de003-da0f-4ee5-a3f1-d3a6e3b1518f
verified: false
validated: true
submitted: true
---
# curl-nextcloud-admin-removal-attempt

## Command

```bash
curl -X POST 'http://target-nextcloud/index.php/settings/ajax/togglegroups.php' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: oc_session=your_session; requesttoken=your_token' -d 'username=admin&group=admin'
```

## Description

This command attempts to remove the admin user from the admin group using standard parameters, which should fail due to server-side restrictions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H 'Content-Type: ...'` | Sets form-encoded content type | Yes |
| `-H 'Cookie: ...'` | Provides authentication session and token | Yes |
| `-d 'username=admin&group=admin'` | Targets admin user and group | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'http://target-nextcloud/index.php/settings/ajax/togglegroups.php' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: oc_session=your_session; requesttoken=your_token' -d 'username=admin&group=admin'
```

### Advanced Usage

Add `-v` for headers and response details.

## Expected Output

{"data":{"message":"Admins can't remove themself from the admin group"},"status":"error"}

## Related

- [[Related Procedure: Test-Normal-Admin-Group-Removal-in-Nextcloud]]
