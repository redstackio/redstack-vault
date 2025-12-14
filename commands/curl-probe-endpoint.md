---
id: cmd-uuid-probe
data: 'curl -X GET https://target-navy-system.com/upload'
tags:
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
updated_at: '2025-12-14T05:32:13.354Z'
verified: false
validated: true
submitted: true
---
# curl-probe-endpoint

## Command

```bash
curl -X GET https://target-navy-system.com/upload
```

## Description

Probes an HTTP endpoint to check accessibility and response, useful for verifying exposed upload tools without authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `https://target-navy-system.com/upload` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -X GET https://target-navy-system.com/upload
```

### Advanced Usage

```bash
curl -X OPTIONS https://target-navy-system.com/upload -v
```

## Expected Output

HTTP 200 response with upload form HTML or JSON details indicating no restrictions.

## Related

- [[Related Procedure|procedures/Access-Exposed-File-Upload-Endpoint]]
