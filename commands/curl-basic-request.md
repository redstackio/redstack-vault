---
id: cmd-002
data: 'curl -I https://apps-staging.pingone.com/'
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
updated_at: '2025-12-14T17:26:17.666Z'
verified: false
validated: true
submitted: true
---
# curl-basic-request

## Command

```bash
curl -I https://apps-staging.pingone.com/
```

## Description

This command performs a HEAD request to verify access controls on the main application endpoint, expecting a 403 Forbidden response to confirm protection before targeting static files.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -I | Use HEAD method instead of GET | Yes |
| URL | Target main endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -I https://apps-staging.pingone.com/
```

### Advanced Usage

```bash
curl -I -H "User-Agent: Mozilla/5.0" https://apps-staging.pingone.com/
```

> Includes a custom User-Agent header to mimic browser requests.

## Expected Output

HTTP headers indicating forbidden access, e.g.:

```
HTTP/1.1 403 Forbidden
Content-Type: application/json
...
```

## Related

- [[Related Procedure: Bypass-Authentication-to-Access-Static-package.json-File]]
