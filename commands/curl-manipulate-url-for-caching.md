---
data: 'curl "https://target.com/dynamic-endpoint.css"'
tags:
  - web
  - recon
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: b1be9917-c20e-4e52-9808-1dc730881d0c
created_at: '2025-12-13T09:00:34.585Z'
updated_at: '2025-12-13T09:00:34.585Z'
verified: false
validated: true
submitted: true
---
# curl-manipulate-url-for-caching

## Command

```bash
curl "https://target.com/dynamic-endpoint.css"
```

## Description

Uses curl to manipulate a URL by appending a static extension to test for web cache deception vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | The target URL with appended extension | Yes |

## Examples

### Basic Usage

```bash
curl "https://www.glassdoor.com/dynamic-endpoint.css"
```

### Advanced Usage

```bash
curl "https://www.glassdoor.com/dynamic-endpoint.css" -H "Cookie: session-cookie"
```

## Expected Output

The response from the server, potentially including cacheable sensitive data.

## Related

- [[procedures/Identify-Dynamic-Endpoint-for-Web-Cache-Deception]]
- [[procedures/Force-Victim-to-Cache-gdToken-via-Deceptive-URL]]
