---
id: cmd-uuid-001
data: python aws.py filename
tags:
  - s3-upload
  - python
  - file-transfer
type: command
output: >-
  File uploaded successfully. Public URL:
  https://bcm-hk.s3.ap-east-1.amazonaws.com/profile/.../filename
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.921Z'
verified: false
validated: true
submitted: true
---
# upload-to-s3-with-aws-py

## Command

```bash
python aws.py filename
```

## Description

Executes a custom Python script to upload a specified file to the misconfigured 'bcm-hk' S3 bucket using presigned POST credentials obtained from the BCM Messenger API. The script parses JSON credentials, base64-encodes the file, and sends a multipart POST request to S3.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `filename` | Path to the file to upload (supports any type/size up to 64MB) | Yes |

## Examples

### Basic Usage

```bash
python aws.py /home/user/document.pdf
```

### Advanced Usage

The script assumes presigned.json in the current directory; for multiple files, run sequentially.

```bash
python aws.py large-video.mp4
```

## Expected Output

Script logs: "Upload successful. URL: https://bcm-hk.s3.ap-east-1.amazonaws.com/profile/[key]/[hash]" followed by S3 204 response. File is publicly accessible.

## Related

- [[procedures/Upload-Arbitrary-Files-to-S3-Bucket]]
