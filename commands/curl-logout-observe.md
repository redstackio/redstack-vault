---
id: cmd-curl-logout-observe
data: 'curl -X GET "https://www.expedia.com/?logout=1" -v'
tags:
  - web-testing
  - redirect
type: command
output: |-
  HTTP/2 302 
  Location: https://www.expedia.com/
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:34.937Z'
verified: false
validated: true
submitted: true
---
# curl-logout-observe

## Command

```bash
curl -X GET "https://www.expedia.com/?logout=1" -v
```

## Description

Observes the default logout redirect on Expedia.com to confirm normal behavior before exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `-v` | Verbose output for headers | Yes |
| URL | Target logout endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://www.expedia.com/?logout=1" -v
```

### Advanced Usage

```bash
curl -X GET "https://www.vrbo.com/?logout=1" -v --cookie "session=abc"
```

## Expected Output

Verbose logs showing 302 redirect to homepage, e.g., Location: https://www.expedia.com/.

## Related

- [[Related Procedure: Trigger-Open-Redirect-on-Logout]]
