---
data: >-
  GET / HTTP/1.1

  Host: www.████████

  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101
  Firefox/58.0

  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/-;q=0.8

  Accept-Language: en-US,en;q=0.5

  Accept-Encoding: gzip, deflate

  Cookie: mt=rid=6130; ASPSESSIONIDQABQSQCS=GNPLOPOCDIGPIKHGFMDDBLBG;
  googtrans=/en/zh-TW

  Connection: close

  Upgrade-Insecure-Requests: 1
tags:
  - recon
  - http
type: command
output: HTTP/1.1 200 OK with HTML content from legitimate site
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.014Z'
id: 6b310606-98a7-4dc8-8c36-d92ced3399d3
verified: false
validated: true
submitted: true
---
# normal-http-get-to-target

## Command

```http
GET / HTTP/1.1
Host: www.████████
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/-;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Cookie: mt=rid=6130; ASPSESSIONIDQABQSQCS=GNPLOPOCDIGPIKHGFMDDBLBG; googtrans=/en/zh-TW
Connection: close
Upgrade-Insecure-Requests: 1
```

## Description

Sends a baseline HTTP GET request to the target DoD website to verify normal operation and capture standard response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Host | Target domain (www.████████) | Yes |
| User-Agent | Browser simulation string | Yes |
| Cookie | Session and tracking cookies | No |

## Examples

### Basic Usage

```http
GET / HTTP/1.1
Host: www.████████
User-Agent: Mozilla/5.0 ...
```

### Advanced Usage

Include custom cookies for session persistence.

## Expected Output

Standard 200 OK response with website content; no errors or redirects.

## Related

- [[commands/ssrf-host-header-get]]
