---
id: cmd-uuid-001
data: >-
  curl -u {username}:{password} -X GET
  "https://your-jira.atlassian.net/rest/api/3/mypermissions?permissions=ADMINISTER_PROJECTS"
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
updated_at: '2025-12-14T17:30:58.152Z'
verified: false
validated: true
submitted: true
---
# jira-check-project-permissions

## Command

```bash
curl -u {username}:{password} -X GET "https://your-jira.atlassian.net/rest/api/3/mypermissions?permissions=ADMINISTER_PROJECTS"
```

## Description

Query the Jira REST API to check if the authenticated user has permission to administer projects, useful for verifying role limitations in exploitation setups.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u {username}:{password}` | Basic auth credentials | Yes |
| `permissions=ADMINISTER_PROJECTS` | Permission key to query | Yes |

## Examples

### Basic Usage

```bash
curl -u basic-user:pass -X GET "https://jiraxsstest.atlassian.net/rest/api/3/mypermissions?permissions=ADMINISTER_PROJECTS"
```

### Advanced Usage

Query multiple: Replace with comma-separated keys.

## Expected Output

JSON: {"permissions": [{"id": "ADMINISTER_PROJECTS", "havePermission": false, "permissions": []}]}

## Related

- [[commands/jira-check-site-permissions]]
- [[procedures/Setup-Jira-Test-Environment]]
