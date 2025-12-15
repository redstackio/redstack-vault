---
data: >-
  GET /srvgtw001/merchant/password/reset HTTP/1.1

  Host: mpos.mtn.co.sz

  Cookie: cookiesession1=678B28894C92B8E298EA67025D4086C2

  Cache-Control: max-age=0

  Sec-Ch-Ua: "Not;A=Brand";v="24", "Chromium";v="128"

  Sec-Ch-Ua-Mobile: ?0

  Sec-Ch-Ua-Platform: "Windows"

  Accept-Language: en-US,en;q=0.9

  Upgrade-Insecure-Requests: 1

  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
  (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36

  Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7

  Sec-Fetch-Site: none

  Sec-Fetch-Mode: navigate

  Sec-Fetch-User: ?1

  Sec-Fetch-Dest: document

  Accept-Encoding: gzip, deflate, br

  Priority: u=0, i

  Connection: keep-alive
tags:
  - recon
  - debug
type: command
output: null
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:17.595Z'
id: b699fdb2-9064-43bc-b104-a1c5af7efc8b
verified: false
validated: true
submitted: true
---
# burp-intercept-password-reset

## Command

```http
GET /srvgtw001/merchant/password/reset HTTP/1.1
Host: mpos.mtn.co.sz
Cookie: cookiesession1=678B28894C92B8E298EA67025D4086C2
Cache-Control: max-age=0
Sec-Ch-Ua: "Not;A=Brand";v="24", "Chromium";v="128"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Priority: u=0, i
Connection: keep-alive
```

## Description

Sends an HTTP GET request to the Laravel password reset endpoint to trigger debug mode output when intercepted with Burp Suite, revealing sensitive information.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Host | Target domain (mpos.mtn.co.sz) | Yes |
| Path | Endpoint (/srvgtw001/merchant/password/reset) | Yes |
| User-Agent | Browser emulation string | Yes |
| Cookie | Session cookie if needed | No |

## Examples

### Basic Usage

Send via Burp Repeater or browser proxy.

### Advanced Usage

Modify headers for evasion.

## Expected Output

HTTP 500 response with HTML containing Laravel debug info: stack traces, file paths, APP_DEBUG=true, version 8.83.27.

## Related

- [[Related Procedure: Discover-Laravel-Debug-Mode-via-Password-Reset]]
