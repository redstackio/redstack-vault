---
id: cmd-uuid-004
data: >-
  curl -u {username}:{password} -X GET
  "https://your-jira.atlassian.net/rest/api/3/permissions"
tags:
  - jira-api
  - permissions-enum
type: command
output: JSON list of permission schemes and IDs for querying specific permissions
executor: curl
platforms:
  - Web
  - Cloud
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.133Z'
verified: false
validated: true
submitted: true
---
# jira-list-permissions

## Command

```bash
curl -u {username}:{password} -X GET "https://your-jira.atlassian.net/rest/api/3/permissions"
```

## Description

Retrieve all available permission schemes in the Jira instance to identify keys for targeted queries.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u {username}:{password}` | Basic auth credentials | Yes |

## Examples

### Basic Usage

```bash
curl -u admin:pass -X GET "https://jiraxsstest.atlassian.net/rest/api/3/permissions"
```

## Expected Output

JSON: {"permission": [{"id": "ADMINISTER", "key": "ADMINISTER", ...}]}

## Related

- [[commands/jira-check-project-permissions]]
- [[procedures/Setup-Jira-Test-Environment]]
