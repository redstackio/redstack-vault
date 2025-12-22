---
id: uuid-github-arbitrary
data: >-
  https://github.com/login?client_id=5f45cc999f7812d0b6d2&return_to=%2Flogin%2Foauth%2Fauthorize%3Fclient_id%3D5f45cc999f7812d0b6d2%26redirect_uri%3Dhttps%253A%252F%252Fedoverflow.com%252F1%26scope%3Dpublic_repo
tags:
  - oauth
  - manipulation
type: command
output: null
executor: browser
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:35.831Z'
verified: false
validated: true
submitted: true
---
# github-oauth-manipulate-redirect-to-arbitrary

## Command

```bash
# Execute in browser or via curl -L
https://github.com/login?client_id=5f45cc999f7812d0b6d2&return_to=%2Flogin%2Foauth%2Fauthorize%3Fclient_id%3D5f45cc999f7812d0b6d2%26redirect_uri%3Dhttps%253A%252F%252Fedoverflow.com%252F1%26scope%3Dpublic_repo
```

## Description

Initiates GitHub OAuth with manipulated redirect_uri to an arbitrary path (/1) on edoverflow.com, preventing code stripping. Use to test domain-wide whitelisting flaws.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| client_id | GitHub app ID (5f45cc999f7812d0b6d2) | Yes |
| return_to | Encoded authorize endpoint | Yes |
| redirect_uri | URL-encoded target path (https%3A%2F%2Fedoverflow.com%2F1) | Yes |
| scope | Permissions (public_repo) | Yes |

## Examples

### Basic Usage

```bash
https://github.com/login/oauth/authorize?client_id=5f45cc999f7812d0b6d2&redirect_uri=https%3A%2F%2Fedoverflow.com%2F1&scope=public_repo
```

### Advanced Usage

Wrap in return_to for full flow simulation as shown.

## Expected Output

Redirect to GitHub auth page, then back to https://edoverflow.com/1?code=... (code visible and not stripped).

## Related

- [[commands/github-oauth-manipulate-redirect-to-about]]
- [[procedures/Manipulate-Redirect-URI-to-Arbitrary-Path]]
