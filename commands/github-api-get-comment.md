---
id: cmd-uuid-002
data: >-
  curl -H "Authorization: token YOUR_PAT_TOKEN" -H "Accept:
  application/vnd.github.v3+json"
  https://your-github-enterprise-server/api/v3/repos/OWNER/REPO/issues/comments/COMMENT_ID
tags:
  - api
  - github
  - get
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-12-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.691Z'
verified: false
validated: true
submitted: true
---
# github-api-get-comment

## Command

```bash
curl -H "Authorization: token YOUR_PAT_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://your-github-enterprise-server/api/v3/repos/OWNER/REPO/issues/comments/COMMENT_ID
```

## Description

This command retrieves details of a specific issue comment from GitHub Enterprise Server API to verify modifications or inspect content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Authorization: token YOUR_PAT_TOKEN"` | Authenticates with PAT | Yes |
| `-H "Accept: application/vnd.github.v3+json"` | Sets API version | Yes |
| `https://your-github-enterprise-server/api/v3/repos/OWNER/REPO/issues/comments/COMMENT_ID` | Target endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -H "Authorization: token ghp_abc123" -H "Accept: application/vnd.github.v3+json" https://github.example.com/api/v3/repos/user/repo/issues/comments/123
```

### Advanced Usage

```bash
curl -H "Authorization: token ghp_abc123" -H "Accept: application/vnd.github.v3+json" -s https://github.example.com/api/v3/repos/user/repo/issues/comments/123 | jq '.body'
```

## Expected Output

JSON object with comment details, e.g., {"id": 123, "body": "Comment text", "created_at": "..."}.

## Related

- [[commands/github-api-update-comment]]
- [[procedures/Exploit-GitHub-PAT-for-Issue-Comment-Modification]]
