---
data: >-
  while read subdomain; do curl -s -o /dev/null -w "%{http_code}
  %{url_effective}\n" http://$subdomain/; done < subdomains.txt >
  status_codes.txt
tags:
  - reconnaissance
  - http-probe
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.387Z'
id: d46a4e46-9718-47c3-873e-02212c4195a7
verified: false
validated: true
submitted: true
---
# curl-check-http-status

## Command

```bash
while read subdomain; do curl -s -o /dev/null -w "%{http_code} %{url_effective}\n" http://$subdomain/; done < subdomains.txt > status_codes.txt
```

## Description

This bash loop uses curl to check HTTP status codes for a list of subdomains, helping identify 404 responses indicative of dangling records.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `subdomains.txt` | Input file with subdomains | Yes |
| `status_codes.txt` | Output file for results | Yes |

## Examples

### Basic Usage

```bash
while read subdomain; do curl -s -o /dev/null -w "%{http_code} %{url_effective}\n" http://$subdomain/; done < subdomains.txt > status_codes.txt
```

### Advanced Usage

Add timeout: ```bash
while read subdomain; do curl -s -m 10 -o /dev/null -w "%{http_code} %{url_effective}\n" http://$subdomain/; done < subdomains.txt > status_codes.txt
```

## Expected Output

Lines like "404 http://www.codefi.consensys.net/" in status_codes.txt.

## Related

- [[procedures/Identify-and-Verify-Dangling-Subdomains]]
