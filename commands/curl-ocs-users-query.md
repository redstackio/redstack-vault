---
id: cmd-uuid-2
data: >-
  curl -X GET "https://{instance}/ocs/v2.php/cloud/users" -u
  "admin:{admin-pass}" -H "OCS-APIRequest: true"
tags:
  - api
  - nextcloud
  - enumeration
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:43.052Z'
verified: false
validated: true
submitted: true
---
# curl-ocs-users-query

## Command

```bash
curl -X GET "https://{instance}/ocs/v2.php/cloud/users" -u "admin:{admin-pass}" -H "OCS-APIRequest: true"
```

## Description

Queries the Nextcloud OCS API to list all users, useful for verifying unauthorized creations post-exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| {instance} | Nextcloud server URL (e.g., pentest.cloud.wtf) | Yes |
| {admin-pass} | Admin password for authentication | Yes |
| -H "OCS-APIRequest: true" | Header required for OCS API | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://pentest.cloud.wtf/ocs/v2.php/cloud/users" -u "admin:password" -H "OCS-APIRequest: true"
```

### Advanced Usage

Add output formatting with | xmllint --format -

```bash
curl ... | xmllint --format - | grep hacker
```

## Expected Output

XML response: `<ocs><meta><status>ok</status></meta><data><users><element>hacker</element>...</users></data></ocs>`

## Related

- [[Related Procedure]]
