---
id: cmd-001
name: curl-initiate-oidc
type: command
executor: bash
data: 'curl -c cookies.txt -L "https://target.com/login?openIdConnect=1"'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:57.570Z'
platforms:
  - Linux
  - macOS
  - Web
tags:
  - recon
  - web
verified: false
validated: true
submitted: true
---

# curl-initiate-oidc

## Command

```bash
curl -c cookies.txt -L "https://target.com/login?openIdConnect=1"
```

## Description

Initiates the OIDC login flow on a Nextcloud target, saving session cookies for later use.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-c cookies.txt` | Save cookies to file | Yes |
| `-L` | Follow redirects | Yes |
| URL | Target login endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -c cookies.txt -L "https://target.com/login?openIdConnect=1"
```

### Advanced Usage

```bash
curl -c cookies.txt -L -v "https://target.com/login?openIdConnect=1"
```

## Expected Output

HTML redirect or response indicating OIDC flow start; cookies file populated with session data.

## Related

- [[Related Procedure]]
