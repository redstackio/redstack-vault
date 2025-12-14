---
data: 'curl -X GET "https://target/swagger" -H "Accept: text/html"'
tags:
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.591Z'
id: 6b7c26a0-da47-4d04-8691-34cc9844f957
verified: false
validated: true
submitted: true
---
# curl-get-swagger-docs

## Command

```bash
curl -X GET "https://target/swagger" -H "Accept: text/html"
```

## Description

This command probes for exposed Swagger API documentation by sending a GET request to a common documentation path retrieving HTML content if available.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `"https://target/swagger"` | Target URL for Swagger UI | Yes |
| `-H "Accept: text/html"` | Sets accept header for HTML response | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://example.com/swagger" -H "Accept: text/html"
```

### Advanced Usage

```bash
curl -X GET "https://example.com/api-docs" -H "Accept: text/html" -o swagger.html
```

## Expected Output

HTML content of Swagger UI or 200 OK with API specs if exposed; 404 if not present.

## Related

- [[Related Procedure]]
