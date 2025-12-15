---
data: >-
  curl -o restricted_file.ext
  "https://app.larksuite.com/file/download?token=VALID_TOKEN_HERE"
tags:
  - download
  - http-request
  - exfiltration
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.588Z'
id: da01a41b-6e2f-45d3-ab78-fd902513644c
verified: false
validated: true
submitted: true
---
# curl-download-file

## Command

```bash
curl -o restricted_file.ext "https://app.larksuite.com/file/download?token=VALID_TOKEN_HERE"
```

## Description

This command uses curl to download a file from a direct URL, such as a token-protected endpoint in web applications. It is useful for testing unauthorized access or exfiltrating data by bypassing UI restrictions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-o` | Specifies the output file name | Yes |
| URL argument | The direct download URL with token | Yes |

## Examples

### Basic Usage

```bash
curl -o secret.doc "https://example.com/file?token=abc123"
```

### Advanced Usage

```bash
curl -o secret.doc -H "User-Agent: Mozilla/5.0" "https://app.larksuite.com/file/download?token=VALID_TOKEN" --fail
```

## Expected Output

The command outputs the file contents to the specified file path. On success, no stderr messages; the file size matches the expected document. Errors like 403 indicate permission issues, but in vulnerable cases, it succeeds silently.

## Related

- [[Related Procedure]]
