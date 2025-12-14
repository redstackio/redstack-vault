---
id: cmd-mtn-baseline
data: >-
  curl -X GET "http://mtn.com.ye/index.php/search/default?t=1&x=0&y=0" -H
  "Cookie: PHPSESSID=86ce3d04baa357ffcacf5d013679b696; lang=en;
  _ga=GA1.3.1859249834.1576704214; _gid=GA1.3.1031541111.1576704214; _gat=1;
  _gat_UA-44336198-10=1" -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64;
  rv:68.0) Gecko/20100101 Firefox/68.0"
tags:
  - recon
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.183Z'
verified: false
validated: true
submitted: true
---
# baseline-search-request

## Command

```bash
curl -X GET "http://mtn.com.ye/index.php/search/default?t=1&x=0&y=0" \
  -H "Cookie: PHPSESSID=86ce3d04baa357ffcacf5d013679b696; lang=en; _ga=GA1.3.1859249834.1576704214; _gid=GA1.3.1031541111.1576704214; _gat=1; _gat_UA-44336198-10=1" \
  -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"
```

## Description

Sends a standard HTTP GET to the search endpoint with baseline cookies to observe normal behavior before vulnerability testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP method | Yes |
| `t=1&x=0&y=0` | Query params for search | Yes |
| `Cookie` | Session and lang cookies | Yes |
| `User-Agent` | Browser simulation | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "http://mtn.com.ye/index.php/search/default?t=1&x=0&y=0" -H "Cookie: ... lang=en ..." -H "User-Agent: ..."
```

### Advanced Usage

Add `-v` for verbose output:

```bash
curl -v -X GET "http://mtn.com.ye/index.php/search/default?t=1&x=0&y=0" -H "Cookie: ..." -H "User-Agent: ..."
```

## Expected Output

HTTP 200 with HTML content, no errors, response time <1s.

## Related

- [[commands/sqli-single-quote-injection]]
- [[procedures/Discover-SQL-Injection-in-Lang-Cookie]]
