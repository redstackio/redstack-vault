---
id: tool-uuid-002
url: null
tags:
  - s3-upload
  - python-script
  - cloud
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.917Z'
validated: true
submitted: true
---
# aws-py

**Status**: Unverified

## Overview

aws.py is a custom Python script designed for proof-of-concept exploitation of the BCM Messenger S3 misconfiguration, simplifying the upload of arbitrary files using presigned POST credentials.

## Description

The script automates parsing JSON presigned data from the API, base64-encoding files, determining MIME types, and sending multipart/form-data POST requests to the S3 endpoint. It targets the 'bcm-hk' bucket and outputs public URLs upon success, useful for demonstrating arbitrary storage abuse.

## Features

- Feature 1: Handles presigned POST fields (key, Policy, Signature, etc.)
- Feature 2: Supports any file type/size (up to 64MB per policy)
- Feature 3: Base64 encoding for binary files and MIME type detection

## Installation

### Requirements

- Python 3.6+
- Libraries: requests, json, base64, mimetypes, sys (install via pip install requests)

### Install Commands

```bash
# No formal install; save as aws.py and run with python
pip install requests
```

## Basic Usage

```bash
python aws.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `filename` | Path to file (positional arg) | 
| `--presigned` | Path to JSON file (default: presigned.json) | No |

## Examples

### Example 1: Basic Usage

```bash
python aws.py document.txt
```

### Example 2: Advanced Usage

```bash
python aws.py --presigned custom.json largefile.zip
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- S3 logs showing POST from Python User-Agent
- Anomalous file uploads to profile/ paths
- Monitor for base64-encoded payloads in requests

## Related Procedures


## Related Tools

- [[tools/aws-cli]]
- [[tools/Boto3]]

## References

- Custom PoC from HackerOne report #764243
- AWS S3 Presigned POST Docs: https://docs.aws.amazon.com/AmazonS3/latest/userguide/PresignedUrlUploadObject.html
