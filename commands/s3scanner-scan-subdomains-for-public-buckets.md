---
type: command
executor: bash
data: python3 s3scanner.py -l $_DOMAIN_LIST -o $_OUTPUT_FILE
tags:
  - s3
  - enumeration
  - recon
platforms:
  - Linux
  - AWS
verified: true
validated: true
---

# s3scanner-scan-subdomains-for-public-buckets

## Command

```bash
python3 s3scanner.py -l $_DOMAIN_LIST -o $_OUTPUT_FILE
```

## Description

This command runs the s3scanner Python script to scan a list of domains or subdomains for publicly accessible S3 buckets. It generates potential bucket names by transforming input domains (e.g., removing dots and hyphens) and tests each for public read access via HTTP HEAD requests to the S3 endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN_LIST | Path to a text file containing domains/subdomains, one per line (e.g., domains.txt) | Yes |
| $_OUTPUT_FILE | Path to the output file where public bucket names will be written (e.g., buckets.txt) | Yes |
| -l | Flag to specify the input domain list file | Built-in |
| -o | Flag to specify the output file for results | Built-in |

## Examples

### Basic Usage

```bash
python3 s3scanner.py -l domains.txt -o public-buckets.txt
```

### Advanced Usage

```bash
python3 s3scanner.py -l subdomains.txt -o results.txt -b bucket_blacklist.txt
```

(Additional flags like -b for blacklisting known private buckets can be added if supported by the tool version.)

## Expected Output

The command outputs progress to stdout, showing tested bucket names and access status (e.g., 'Bucket example-bucket is public!'). Upon completion, $_OUTPUT_FILE contains a list of public bucket names, one per line, such as:

```
example-public-bucket
leaked-config-bucket
```

No output file entry means no public buckets were found.

## Related

- [[procedures/Scan-for-Public-S3-Buckets-from-Subdomain-List]]
- [[commands/aws-s3-ls-list-bucket-contents]]
