---
data: 'curl "https://try.discourse.org/u/my/preferences.css"'
tags:
  - recon
  - http
type: command
output: |-
  HTTP/1.1 200 OK
  X-Discourse-Route: users/preferences
  X-Discourse-Username: test
  <meta name="csrf-token" content="6bE...VnlQ==" /> and CF-Cache-Status: HIT
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.435Z'
id: e41b00ea-a030-45ca-8aab-d1a95cfff155
verified: false
validated: true
submitted: true
---
# curl-get-u-my-preferences-css

## Command

```bash
curl "https://try.discourse.org/u/my/preferences.css"
```

## Description

Requests the user preferences page with .css extension to cache authenticated user-specific content including CSRF token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://try.discourse.org/u/my/preferences.css | Path to preferences with .css | Yes |

## Examples

### Basic Usage

```bash
curl "https://try.discourse.org/u/my/preferences.css"
```

### Advanced Usage

```bash
curl -v "https://try.discourse.org/u/my/preferences.css" | grep -i cache
```

## Expected Output

200 OK with X-Discourse-Username header and CSRF meta; cache HIT on repeat.

## Related

- [[commands/curl-get-u-x-css]]
