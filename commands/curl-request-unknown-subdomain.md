---
data: 'curl -H "Host: unknownsub.example.gov" http://example.gov'
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
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.519Z'
id: 9ddc70af-9be5-41d0-b3b1-610f02238808
verified: false
validated: true
submitted: true
---
# curl-request-unknown-subdomain

## Command

```bash
curl -H "Host: unknownsub.example.gov" http://example.gov
```

## Description

This command uses curl to send an HTTP request to a target domain while spoofing the Host header to an unknown subdomain, testing for fallback routing misconfigurations in proxy servers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H` | Sets a custom header, here the Host to the unknown subdomain | Yes |
| `http://example.gov` | The base URL to request, which triggers proxy routing | Yes |

## Examples

### Basic Usage

```bash
curl -H "Host: testsub.18f.gov" http://18f.gov
```

### Advanced Usage

```bash
curl -v -H "Host: testsub.18f.gov" http://18f.gov
```

## Expected Output

A successful response from the server, potentially including content served for the spoofed subdomain if the vulnerability exists. Look for HTTP 200 with unexpected content or verbose logs showing proxy behavior.

## Related

- [[Related Procedure]]
