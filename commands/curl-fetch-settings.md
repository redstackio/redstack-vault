---
id: cmd-uuid-1
data: 'curl "https://accounts.firefox.com/settings?flowId=test123" -v'
tags:
  - recon
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:23.621Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-settings

## Command

```bash
curl "https://accounts.firefox.com/settings?flowId=test123" -v
```

## Description

Fetches the Firefox Accounts settings page with a test flowId parameter to inspect for reflection in the HTML response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target endpoint with flowId | Yes |
| -v | Verbose output for headers | No |

## Examples

### Basic Usage

```bash
curl "https://accounts.firefox.com/settings?flowId=test123" -v
```

### Advanced Usage

```bash
curl -s "https://accounts.firefox.com/settings?flowId=test123" | grep flowId
```

## Expected Output

HTTP response with HTML body containing unescaped 'test123' insertion, e.g., lines showing <script> or div with the value.

## Related

- [[commands/grep-reflection]]
