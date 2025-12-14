---
id: cmd-curl-file-retrieve
data: 'curl https://█████████/delete.me'
tags:
  - web
  - retrieve
type: command
output: test file
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.115Z'
verified: false
validated: true
submitted: true
---
# curl-file-retrieve

## Command

```bash
curl https://█████████/delete.me
```

## Description

This command retrieves the contents of an uploaded file from a predictable public URL, verifying exposure after an arbitrary file upload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://█████████/delete.me` | Direct URL to the uploaded file | Yes |

## Examples

### Basic Usage

```bash
curl https://example.com/uploaded.txt
```

### Advanced Usage

```bash
curl -o retrieved.txt https://█████████/delete.me
```

## Expected Output

The raw contents of the file, such as 'test file,' confirming public access.

## Related

- [[Related Procedure|procedures/Access-Uploaded-File-Publicly]]
