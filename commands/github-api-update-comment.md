---
id: cmd-uuid-001
data: >-
  curl -X PUT -H "Authorization: token YOUR_PAT_TOKEN" -H "Accept:
  application/vnd.github.v3+json" -d @update.json
  https://your-github-enterprise-server/api/v3/repos/OWNER/REPO/issues/comments/COMMENT_ID
tags:
  - api
  - github
  - update
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-12-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.693Z'
verified: false
validated: true
submitted: true
---
# github-api-update-comment

## Command

```bash
curl -X PUT \
  -H "Authorization: token YOUR_PAT_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  -d @update.json \
  https://your-github-enterprise-server/api/v3/repos/OWNER/REPO/issues/comments/COMMENT_ID
```

## Description

This command updates an issue comment in GitHub Enterprise Server via the REST API using a PAT for authentication. It exploits misconfigured scopes to modify comments with read-only issues permission.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X PUT` | Specifies the HTTP method for updating | Yes |
| `-H "Authorization: token YOUR_PAT_TOKEN"` | Authenticates with the PAT token | Yes |
| `-H "Accept: application/vnd.github.v3+json"` | Sets API version header | Yes |
| `-d @update.json` | Provides JSON payload from file | Yes |
| `https://your-github-enterprise-server/api/v3/repos/OWNER/REPO/issues/comments/COMMENT_ID` | Target API endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X PUT -H "Authorization: token ghp_abc123" -H "Accept: application/vnd.github.v3+json" -d '{"body": "New content"}' https://github.example.com/api/v3/repos/user/repo/issues/comments/123
```

### Advanced Usage

```bash
curl -X PUT -H "Authorization: token ghp_abc123" -H "Accept: application/vnd.github.v3+json" -d @payload.json -v https://github.example.com/api/v3/repos/user/repo/issues/comments/123
```

## Expected Output

Successful execution returns HTTP 200 with JSON like {"url": "...", "body": "Modified content", ...}. Errors include 403 for insufficient permissions or 404 for invalid IDs.

## Related

- [[commands/github-api-get-comment]]
- [[procedures/Exploit-GitHub-PAT-for-Issue-Comment-Modification]]
