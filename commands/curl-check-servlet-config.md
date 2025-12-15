---
data: 'curl -X PUT -T testfile.txt http://target:8080/upload/testfile.txt -v'
tags:
  - recon
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:17.460Z'
id: c464918c-1336-4a38-8278-512b430bca28
verified: false
validated: true
submitted: true
---
# curl-check-servlet-config

## Command

```bash
curl -X PUT -T testfile.txt http://target:8080/upload/testfile.txt -v
```

## Description

This command tests if the Tomcat Default Servlet allows write operations by attempting to upload a test file to the upload path.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X PUT` | Specifies the HTTP PUT method | Yes |
| `-T testfile.txt` | Uploads the file testfile.txt | Yes |
| `http://target:8080/upload/testfile.txt` | Target URL for upload | Yes |
| `-v` | Verbose output for response details | No |

## Examples

### Basic Usage

```bash
curl -X PUT -T testfile.txt http://target:8080/upload/testfile.txt -v
```

### Advanced Usage

```bash
curl -X PUT -T testfile.txt --header "Authorization: Basic dXNlcjpwd2Qi http://target:8080/upload/testfile.txt -v
```

## Expected Output

HTTP/1.1 201 Created or 200 OK if writes enabled; body may include file details. 403/405 if disabled.

## Related

- [[Related Procedure]]
