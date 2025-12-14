---
id: cmd-curl-gitlab-search-001
data: >-
  curl --request GET --header "PRIVATE-TOKEN: <YOUR-TOKEN>"
  https://gitlab.example.com/api/v4/projects/<project-id>/search?search=milestone&scope=milestones
tags:
  - api
  - gitlab
  - search
type: command
output: >-
  [{"id":123,"iid":1,"project_id":12,"title":"milestone","description":"milestone","state":"active","created_at":"2018-12-11T20:03:25.381Z","updated_at":"2018-12-11T20:03:25.381Z","due_date":null,"start_date":null,"web_url":"https://gitlab.example.com/namespace/project/milestones/1"}]
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:29.118Z'
verified: false
validated: true
submitted: true
---
# curl-gitlab-search-milestones

## Command

```bash
curl --request GET --header "PRIVATE-TOKEN: <YOUR-TOKEN>" https://gitlab.example.com/api/v4/projects/<project-id>/search?search=milestone&scope=milestones
```

## Description

This command performs a GET request to the GitLab search API to query milestones in a specific project using a search term, demonstrating unauthorized access when executed by a non-project member in restricted setups.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--request GET` | Specifies the HTTP method | Yes |
| `--header "PRIVATE-TOKEN: <YOUR-TOKEN>" ` | Authentication header with API token | Yes |
| `https://gitlab.example.com/api/v4/projects/<project-id>/search` | Base API endpoint with project ID | Yes |
| `?search=milestone` | Query parameter for search term | Yes |
| `&scope=milestones` | Limits search to milestones scope | Yes |

## Examples

### Basic Usage

```bash
curl --request GET --header "PRIVATE-TOKEN: glpat-abc123" https://gitlab.com/api/v4/projects/12345/search?search=security&scope=milestones
```

### Advanced Usage

```bash
curl --request GET --header "PRIVATE-TOKEN: glpat-abc123" --silent https://gitlab.example.com/api/v4/projects/12345/search?search=milestone&scope=milestones | jq '.[0].title'
```

## Expected Output

A JSON array of matching milestones, including id, title, description, state, dates, and web_url, even if the user lacks project membership.

## Related

- [[procedures/Enumerate-Milestones-via-GitLab-Search-API]]
