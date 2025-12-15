---
id: cmd-271407-curl-fetch
data: 'curl -v https://dev-domain.example.com/'
tags:
  - web
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:56.815Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-domain

## Command

```bash
curl -v https://dev-domain.example.com/
```

## Description

This command uses curl to fetch the content of a development domain with verbose output, allowing inspection of HTTP responses to confirm lack of authentication and direct access to sensitive pages.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose mode to show headers and details | Yes |
| `https://dev-domain.example.com/` | Target URL to fetch | Yes |

## Examples

### Basic Usage

```bash
curl -v https://dev-domain.example.com/
```

### Advanced Usage

```bash
curl -v -H "User-Agent: Mozilla/5.0" https://dev-domain.example.com/admin
```

## Expected Output

A verbose HTTP response showing 200 OK status, no authentication challenges, and the raw HTML or data from the page, indicating successful unauthorized access.

## Related

- [[Related Procedure|procedures/Access-Unauthenticated-Development-Domain]]
