---
id: cmd-uuid-002
data: >-
  curl -u {username}:{password} -X GET
  "https://your-jira.atlassian.net/rest/api/3/mypermissions?permissions=ADMINISTER"
tags:
  - jira-api
  - permissions-check
type: command
output: >-
  JSON response indicating whether the permission is granted (e.g., false for
  Trusted user)
executor: curl
platforms:
  - Web
  - Cloud
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.148Z'
verified: false
validated: true
submitted: true
---
# jira-check-site-permissions

## Command

```bash
curl -u {username}:{password} -X GET "https://your-jira.atlassian.net/rest/api/3/mypermissions?permissions=ADMINISTER"
```

## Description

Check site-wide admin permissions for the user via Jira API, confirming limited access in attack validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u {username}:{password}` | Basic auth credentials | Yes |
| `permissions=ADMINISTER` | Site admin permission key | Yes |

## Examples

### Basic Usage

```bash
curl -u trusted-user:pass -X GET "https://jiraxsstest.atlassian.net/rest/api/3/mypermissions?permissions=ADMINISTER"
```

## Expected Output

JSON: {"permissions": [{"id": "ADMINISTER", "havePermission": false}]}

## Related

- [[commands/jira-check-project-permissions]]
- [[procedures/Setup-Jira-Test-Environment]]
