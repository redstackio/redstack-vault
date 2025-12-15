---
id: cmd-998457-cors-test
data: >-
  curl -X OPTIONS "https://target.com/graphql" -H "Origin: https://evil.com" -H
  "Access-Control-Request-Method: GET" -v
tags:
  - cors
  - test
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:42.838Z'
verified: false
validated: true
submitted: true
---
# curl-cors-test

## Command

```bash
curl -X OPTIONS "https://target.com/graphql" -H "Origin: https://evil.com" -H "Access-Control-Request-Method: GET" -v
```

## Description

This command performs a CORS preflight request to check if the endpoint allows cross-origin GET methods from untrusted origins, identifying permissive policies.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X OPTIONS` | HTTP OPTIONS for preflight | Yes |
| `-H "Origin: ..."` | Simulates cross-origin | Yes |
| `-H "Access-Control-Request-Method: GET"` | Requests GET permission | Yes |
| `-v` | Verbose for headers | No |

## Examples

### Basic Usage

```bash
curl -X OPTIONS "https://target.com/graphql" -H "Origin: https://evil.com" -v
```

### Advanced Usage

```bash
curl -X OPTIONS "https://target.com/graphql" -H "Origin: https://evil.com" -H "Access-Control-Request-Method: GET" -H "Access-Control-Request-Headers: Cookie" -v
```

## Expected Output

Headers like Access-Control-Allow-Origin: * or https://evil.com, Access-Control-Allow-Methods: GET, indicating vulnerability.

## Related

- [[Related Procedure: Leverage-Permissive-CORS-for-Cross-Origin-Requests]]
