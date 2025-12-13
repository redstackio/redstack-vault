---
data: >-
  curl -H "Host: www.google.com" -H "User-Agent: Mozilla/5.0" -H "Accept: */*"
  https://target.com/contact/
tags:
  - http
  - injection
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 934cac17-5b18-48eb-9e9c-09a8f5e8a342
created_at: '2025-12-13T09:01:17.463Z'
updated_at: '2025-12-13T09:01:17.463Z'
verified: false
validated: true
submitted: true
---
# curl-host-header-injection-test

## Command

```bash
curl -H "Host: www.google.com" -H "User-Agent: Mozilla/5.0" -H "Accept: */*" https://target.com/contact/
```

## Description

This command uses curl to send an HTTP GET request with a modified Host header to test for host header injection vulnerabilities, simulating an attack by pointing to an external domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Host: www.google.com"` | Sets the spoofed Host header | Yes |
| `-H "User-Agent: Mozilla/5.0"` | Sets a standard User-Agent | No |
| `-H "Accept: */*"` | Sets the Accept header | No |
| `https://target.com/contact/` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -H "Host: www.google.com" https://target.com/contact/
```

### Advanced Usage

```bash
curl -H "Host: www.google.com" -H "User-Agent: Mozilla/5.0" -H "Accept: */*" -v https://target.com/contact/
```

## Expected Output

HTTP/1.1 421 Misdirected Request or similar server response indicating potential vulnerability.

## Related

- [[procedures/Test-for-Host-Header-Injection]]
- [[tools/curl]]
