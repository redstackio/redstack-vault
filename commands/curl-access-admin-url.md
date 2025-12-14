---
data: 'curl -L -v https://TARGET/admin'
tags:
  - web
  - recon
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.605Z'
id: 0adcdb41-9e9a-4b4f-bb6d-440be388a11b
verified: false
validated: true
submitted: true
---
# curl-access-admin-url

## Command

```bash
curl -L -v https://TARGET/admin
```

## Description

This command uses curl to access a suspected admin URL on a target web application, following redirects to uncover hidden admin panels or backends like Ghost.io. It is useful during reconnaissance to test for predictable paths without authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-L` | Follow HTTP redirects (e.g., 3xx responses) | Yes |
| `-v` | Verbose mode to display headers and response details | Yes |
| `https://TARGET/admin` | The target URL with suspected admin path; replace TARGET with the domain (e.g., blog.brave.com) | Yes |

## Examples

### Basic Usage

```bash
curl -L -v https://blog.brave.com/admin
```

### Advanced Usage

```bash
curl -L -v -H "User-Agent: Mozilla/5.0" https://blog.brave.com/admin
```

> Adds a user-agent header to mimic a browser if the site blocks default curl agents.

## Expected Output

Verbose output showing the request/response, including a redirect (e.g., HTTP/1.1 301 Moved Permanently, Location: https://brave.ghost.io/ghost/signin/). Successful execution reveals the admin endpoint without errors.

## Related

- [[Related Procedure: Enumerate-Admin-Panel-via-Predictable-URL]]
