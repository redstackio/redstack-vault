---
id: 5566dbc8-33ee-454d-b162-4529d8369175
name: AWSBucketDump
type: tool
verified: true
created_at: '2019-08-28T21:17:28.128001+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - aws
  - s3
  - enumeration
  - reconnaissance
  - cloud
url: 'https://github.com/jordanpotti/AWSBucketDump'
validated: true
---

# AWSBucketDump

**Status**: Unverified

## Overview

AWSBucketDump is a command-line tool designed for quickly enumerating AWS S3 buckets associated with a target domain or organization. It generates common bucket name permutations and uses anonymous AWS API access to check for public buckets, listing their contents to identify potential sensitive data leaks like credentials, backups, or configuration files. Commonly used in reconnaissance phases of penetration testing to discover misconfigured cloud storage.

## Description

The tool leverages the AWS S3 API without requiring credentials, relying on public bucket policies. It supports domain-based permutation generation (e.g., appending 'backup', 'prod', 'dev'), custom wordlists for targeted names, and single bucket testing. If a bucket is public, it can recursively list or download objects. This makes it valuable for red team operations assessing cloud exposure, but it respects AWS rate limits to avoid detection.

## Features

- Feature 1: Automatic generation of bucket name permutations based on domain or organization name.
- Feature 2: Support for custom wordlists to test organization-specific bucket names.
- Feature 3: Anonymous access checking for public read permissions on buckets and objects.
- Feature 4: Recursive content listing and optional downloading of accessible files.
- Feature 5: Output formatting in CSV or text for easy parsing and reporting.

## Installation

### Requirements

- Python 2.7 or 3.x
- No additional AWS credentials needed (uses anonymous access)
- Optional: boto3 library for enhanced functionality (pip install boto3)

### Install Commands

```bash
# Clone the repository
 git clone https://github.com/jordanpotti/AWSBucketDump.git
 cd AWSBucketDump

# Make executable (if needed)
 chmod +x AWSBucketDump.py

# For Python 3 compatibility, may need to run with python3
```

On Kali Linux, it may be available via apt or manual install as above.

## Basic Usage

```python
python AWSBucketDump.py --help
```

This displays all available options and flags.

### Common Options

| Option | Description |
|--------|-------------|
| -l, --list | Specify domain or list file for bucket generation |
| -w, --wordlist | Use a custom wordlist for bucket names |
| -b, --bucket | Test a single specific bucket |
| -g, --grab | Download contents of accessible buckets |
| -o, --output | Specify output file format (e.g., CSV) |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

```python
python AWSBucketDump.py -l example.com
```

Enumerates and tests default permutations for example.com.

### Example 2: Advanced Usage

```python
python AWSBucketDump.py -l example.com -w custom_buckets.txt -g -o results.csv
```

Uses a wordlist, grabs contents, and saves to CSV.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Data from Cloud Storage]] Data from Cloud Storage Object

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: High volume of anonymous S3 ListBuckets and GetObject API calls from a single IP.
- Detection method 2: AWS CloudTrail logs showing access to multiple bucket names with permutation patterns (e.g., *-backup, *-prod).
- Detection method 3: Network monitoring for traffic to s3.amazonaws.com endpoints without authenticated sessions.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nmap]]
- [[AWS-CLI]]

## References

- Official GitHub: https://github.com/jordanpotti/AWSBucketDump
- AWS S3 Security Best Practices: https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html
