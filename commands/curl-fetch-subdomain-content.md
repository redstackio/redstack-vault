---
id: cmd-curl-fetch
data: curl v.zego.com
tags:
  - web
  - verification
type: command
output: <!-- hackerone.com/ian -->
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:49.475Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-subdomain-content

## Command

```bash
curl v.zego.com
```

## Description

Sends an HTTP GET request to the subdomain and retrieves the response body, used to verify if custom content is being served after a takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `v.zego.com` | The URL or domain to fetch | Yes |

## Examples

### Basic Usage

```bash
curl v.zego.com
```

### Advanced Usage

```bash
curl -v v.zego.com  # Verbose output with headers
```

## Expected Output

<!-- hackerone.com/ian -->

## Related

- [[Related Procedure|procedures/Verify-Subdomain-Takeover-with-Custom-Content]]
