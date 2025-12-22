---
type: command
executor: bash
data: >-
  for i in $(cat $_BUCKET_LIST); do aws s3 ls s3://$i --recursive 2>/dev/null ||
  true; done;
tags:
  - s3
  - enumeration
  - aws
platforms:
  - Linux
  - AWS
verified: true
validated: true
---

# aws-s3-ls-list-bucket-contents

## Command

```bash
for i in $(cat $_BUCKET_LIST); do aws s3 ls s3://$i --recursive 2>/dev/null || true; done;
```

## Description

This bash loop command reads a list of S3 bucket names from a file and uses the AWS CLI to list all contents (files and directories) within each public bucket recursively. It is designed for enumerating exposed data in misconfigured buckets without requiring AWS credentials, as it targets public resources only.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_BUCKET_LIST | Path to a text file containing S3 bucket names, one per line (e.g., buckets.txt) | Yes |
| --recursive | Flag to list all objects including subdirectories | Built-in |
| 2>/dev/null || true | Suppresses error output and continues on failures (e.g., non-public buckets) | Built-in |

## Examples

### Basic Usage

```bash
for i in $(cat buckets.txt); do aws s3 ls s3://$i --recursive 2>/dev/null || true; done;
```

### Advanced Usage

```bash
for i in $(cat buckets.txt); do echo "Bucket: $i"; aws s3 ls s3://$i --recursive --human-readable --summarize 2>/dev/null || true; done;
```

(Adds bucket headers, human-readable sizes, and a summary of total objects/size per bucket.)

## Expected Output

For each public bucket, the command prints a directory-like listing of objects, including prefixes (folders), file names, sizes, and modification dates. Example for a bucket with exposed files:

```
2023-01-15 10:30:00     1024 config.json
2023-01-15 10:30:00    20480 api-keys.txt
2023-01-15 10:30:00        0 backups/
```

Non-public buckets produce no output due to error suppression. If all buckets are private, the command runs silently.

## Related

- [[procedures/Scan-for-Public-S3-Buckets-from-Subdomain-List]]
- [[commands/s3scanner-scan-subdomains-for-public-buckets]]
