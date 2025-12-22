---
data: >-
  curl -G "https://openapi.starbucks.com/searchasyoutype/v1/search" -d
  "query=coffee" -d "siteBaseUrl=http://example.com" --header "x-api-key:
  YOUR_API_KEY"
tags:
  - web
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 88113327-b268-4947-aef1-3954905a3649
created_at: '2025-12-14T03:46:31.595Z'
updated_at: '2025-12-14T03:46:31.595Z'
verified: false
validated: true
submitted: true
---
# curl-access-search-endpoint

## Command

```bash
curl -G "https://openapi.starbucks.com/searchasyoutype/v1/search" -d "query=coffee" -d "siteBaseUrl=http://example.com" --header "x-api-key: YOUR_API_KEY"
```

## Description

This command sends a GET request to the Starbucks search endpoint with sample parameters to check for input reflection. Use it during reconnaissance to inspect HTML output for vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-G` | Treat data as query parameters for GET | Yes |
| `-d "query=coffee"` | Search query parameter | Yes |
| `-d "siteBaseUrl=http://example.com"` | Base URL parameter to test reflection | Yes |
| `--header "x-api-key: YOUR_API_KEY"` | API key header (replace with valid key if needed) | Optional |

## Examples

### Basic Usage

```bash
curl -G "https://openapi.starbucks.com/searchasyoutype/v1/search" -d "query=coffee" -d "siteBaseUrl=http://example.com"
```

### Advanced Usage

```bash
curl -G "https://openapi.starbucks.com/searchasyoutype/v1/search" -d "query=coffee" -d "siteBaseUrl=http://example.com" --header "x-api-key: abc123" -o response.html
```

## Expected Output

HTML response body with reflected parameters, e.g., lines containing 'http://example.com' in tags. Pipe to grep for quick check: | grep siteBaseUrl.

## Related

- [[Related Procedure: Identify Reflected XSS in siteBaseUrl Parameter]]
