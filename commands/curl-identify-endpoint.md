---
id: uuid-curl-identify
data: 'curl -X GET "http://target.com/api/items?filter_key=testkey" -v'
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
created_at: '2024-12-05T00:00:00Z'
updated_at: '2025-12-14T03:16:24.942Z'
verified: false
validated: true
submitted: true
---
# curl-identify-endpoint

## Command

```bash
curl -X GET "http://target.com/api/items?filter_key=testkey" -v
```

## Description

This command probes a Django web endpoint to identify if it uses JSON key filtering, potentially vulnerable to HasKey SQL injection. The -v flag provides verbose output for analyzing headers and errors.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP method | Yes |
| `URL` | Target endpoint with parameter | Yes |
| `-v` | Verbose mode for debugging | Yes |
| `?filter_key=testkey` | Test input for key parameter | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "http://target.com/api/items?filter_key=testkey" -v
```

### Advanced Usage

```bash
curl -X GET "http://target.com/api/items?filter_key='" -v --cookie "session=abc"
```

## Expected Output

HTTP response body with potential JSON data or error messages like Oracle ORA- errors indicating backend processing.

## Related

- [[commands/curl-sqli-payload]]
- [[procedures/Identify-Django-HasKey-Usage]]
