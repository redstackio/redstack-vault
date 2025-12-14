---
data: >-
  curl -X POST -H "Authorization: token YOUR_TOKEN" -H "Accept:
  application/vnd.github+json"
  https://ghe.example.com/api/v3/repos/OWNER/REPO/transfer -d '{"new_owner":
  "target-org"}'
tags:
  - api
  - transfer
type: command
output: '{"message": "Transfer started"}'
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:29.335Z'
id: 8b69633c-c863-4d16-9c32-7bd5093b729b
verified: false
validated: true
submitted: true
---
# curl-github-repo-transfer-rest

## Command

```bash
curl -X POST -H "Authorization: token YOUR_TOKEN" -H "Accept: application/vnd.github+json" https://ghe.example.com/api/v3/repos/OWNER/REPO/transfer -d '{"new_owner": "target-org"}'
```

## Description

Initiates a repository transfer in GitHub Enterprise Server via REST API. Use during race condition exploits to start the transfer process.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method for transfer | Yes |
| `-H "Authorization: token YOUR_TOKEN"` | Auth header with PAT | Yes |
| `-H "Accept: application/vnd.github+json"` | API version header | Yes |
| `https://ghe.example.com/api/v3/repos/OWNER/REPO/transfer` | Endpoint URL | Yes |
| `-d '{"new_owner": "target-org"}'` | JSON payload with target org | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Authorization: token ghp_abc123" -H "Accept: application/vnd.github+json" https://ghe.example.com/api/v3/repos/source-org/my-repo/transfer -d '{"new_owner": "target-org"}'
```

### Advanced Usage

```bash
curl -X POST -H "Authorization: token ghp_abc123" -H "Accept: application/vnd.github+json" -v https://ghe.example.com/api/v3/repos/source-org/my-repo/transfer -d '{"new_owner": "target-org"}'
```

## Expected Output

JSON response like {"message": "Transfer started for my-repo to target-org."} on success; 403 on insufficient perms.

## Related

- [[Related Procedure: Initiate-GitHub-Repository-Transfer-via-REST-API]]
