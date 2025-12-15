---
data: >-
  curl -X POST
  'http://target-nextcloud/index.php/settings/ajax/togglegroups.php' -H
  'Content-Type: application/x-www-form-urlencoded' -H 'Cookie:
  oc_session=your_session; requesttoken=your_token' -d
  'username=test&group=test'
tags:
  - nextcloud
  - http-request
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.572Z'
id: 47b3f7ac-56d8-493b-a2d4-e18a8ee0b359
verified: false
validated: true
submitted: true
---
# curl-nextcloud-toggle-groups-normal

## Command

```bash
curl -X POST 'http://target-nextcloud/index.php/settings/ajax/togglegroups.php' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: oc_session=your_session; requesttoken=your_token' -d 'username=test&group=test'
```

## Description

This command demonstrates a standard POST request to Nextcloud's group toggle endpoint for normal operation, toggling a test user in a test group. Use it to baseline the endpoint's response format.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H 'Content-Type: ...'` | Sets form-encoded content type | Yes |
| `-H 'Cookie: ...'` | Provides authentication session and token | Yes |
| `-d 'username=test&group=test'` | Parameters for user and group | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'http://target-nextcloud/index.php/settings/ajax/togglegroups.php' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: oc_session=your_session; requesttoken=your_token' -d 'username=test&group=test'
```

### Advanced Usage

Replace placeholders with actual values; add verbose flag `-v` for debugging.

```bash
curl -v -X POST 'http://target-nextcloud/index.php/settings/ajax/togglegroups.php' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: oc_session=your_session; requesttoken=your_token' -d 'username=test&group=test'
```

## Expected Output

JSON success response like {"data":{"username":"test","action":"add","groupname":"test"},"status":"success"} for successful toggle.

## Related

- [[Related Procedure: Test-Normal-Admin-Group-Removal-in-Nextcloud]]
