---
id: cmd-uuid-003
data: >-
  curl -u {username}:{password} -X GET
  "https://your-jira.atlassian.net/rest/api/3/mypermissions?permissions=BROWSE_PROJECTS,EDIT_ISSUES"
tags:
  - jira-api
  - permissions-check
type: command
output: >-
  JSON response showing denied access for restricted projects (e.g.,
  havePermission: false)
executor: curl
platforms:
  - Web
  - Cloud
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.142Z'
verified: false
validated: true
submitted: true
---
# jira-check-browse-edit-permissions

## Command

```bash
curl -u {username}:{password} -X GET "https://your-jira.atlassian.net/rest/api/3/mypermissions?permissions=BROWSE_PROJECTS,EDIT_ISSUES"
```

## Description

Verify permissions for browsing projects and editing issues, highlighting discrepancies when integration bypasses them.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u {username}:{password}` | Basic auth credentials | Yes |
| `permissions=BROWSE_PROJECTS,EDIT_ISSUES` | Comma-separated permission keys | Yes |

## Examples

### Basic Usage

```bash
curl -u basic-user:pass -X GET "https://jiraxsstest.atlassian.net/rest/api/3/mypermissions?permissions=BROWSE_PROJECTS,EDIT_ISSUES"
```

## Expected Output

JSON: Array of permissions with havePermission: false for restricted actions.

## Related

- [[commands/jira-check-project-permissions]]
- [[procedures/Exploit-Linked-Integration-for-Unauthorized-Access]]
