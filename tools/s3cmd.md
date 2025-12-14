---
id: tool-001-s3cmd
url: 'https://github.com/s3tools/s3cmd'
tags:
  - s3
  - aws
  - cloud
  - upload
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:12.801Z'
validated: true
submitted: true
---
# s3cmd

**Status**: Unverified

## Overview

s3cmd is a command-line tool for managing Amazon S3 and other cloud storage services, commonly used for uploading, downloading, and syncing files. In security contexts, misconfigurations during uploads can lead to information disclosure via preserved metadata headers.

## Description

s3cmd allows interaction with S3 buckets for operations like putting objects, which by default preserves local file metadata (e.g., ownership, timestamps) in custom headers like x-amz-meta-s3cmd-attrs. This can inadvertently expose system details such as usernames on public objects. It's particularly relevant in offensive security for testing upload misconfigurations and in defensive scenarios for secure uploads.

## Features

- Feature 1: Upload/download files and directories to/from S3
- Feature 2: Preserve or exclude file metadata with flags like --no-preserve
- Feature 3: Support for ACLs, encryption, and multipart uploads

## Installation

### Requirements

- Python 2.7 or 3.x
- AWS credentials configured

### Install Commands

```bash
# Via pip
pip install s3cmd

# Or download from GitHub and install
wget https://github.com/s3tools/s3cmd/releases/download/v2.3.3/s3cmd-2.3.3.tar.gz
tar -xzf s3cmd-2.3.3.tar.gz
cd s3cmd-2.3.3
python setup.py install
```

## Basic Usage

```bash
s3cmd --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `--no-preserve` | Do not preserve file attributes in metadata |
| `--acl-public` | Set object ACL to public-read |

## Examples

### Example 1: Basic Usage

```bash
s3cmd put file.txt s3://mybucket/
```

### Example 2: Advanced Usage

```bash
s3cmd put file.txt s3://mybucket/ --no-preserve --acl-public
```

> Uploads without metadata disclosure and makes it publicly accessible.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Log S3 access patterns showing uploads from s3cmd user agents
- Detection method 2: Scan object metadata for preserved attributes like uname/gname

## Related Procedures

- [[procedures/Inspect-S3-Response-Headers-for-Metadata-Disclosure]]

## Related Tools

- [[aws-cli]]
- [[boto3]]

## References

- Official documentation: https://s3tools.org/s3cmd
- GitHub repository: https://github.com/s3tools/s3cmd
