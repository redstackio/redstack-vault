---
type: procedure
description: >-
  Identifies publicly accessible S3 buckets derived from a list of subdomains
  using s3scanner, then enumerates their contents with AWS CLI.
verified: true
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Vulnerability Scanning]]'
sub_techniques: []
tags:
  - s3
  - bucket-enumeration
  - reconnaissance
  - aws
  - cloud
commands:
  - '[[commands/s3scanner-scan-subdomains-for-public-buckets]]'
  - '[[commands/aws-s3-ls-list-bucket-contents]]'
platforms:
  - AWS
  - Linux
tools:
  - '[[tools/s3scanner]]'
  - '[[tools/aws-cli]]'
skill_level: beginner
impact_level: medium
detection_risk: low
validated: true
---

# Scan-for-Public-S3-Buckets-from-Subdomain-List

## Summary

This procedure scans a list of subdomains or domains for potentially public Amazon S3 buckets using the s3scanner tool, which generates possible bucket names based on the input and checks their accessibility. Once public buckets are identified, it uses the AWS CLI to list the contents of each bucket, revealing any exposed files or data that could contain sensitive information like configuration files, API keys, or credentials.

## Description

Misconfigured S3 buckets are a common source of data leaks in AWS environments, often due to overly permissive public access policies. This procedure automates the discovery of such buckets by deriving potential bucket names from subdomain lists (e.g., app.example.com might yield 'app-example-com' as a bucket name) and testing for public readability. It is particularly useful during reconnaissance phases of penetration testing or red team engagements targeting cloud infrastructure. The process requires no AWS credentials since it only checks public access, but success depends on the accuracy of subdomain enumeration upstream. Expected outcomes include a list of accessible buckets and their file inventories, which can lead to further exploitation if sensitive data is found.

## Requirements

1. A text file containing a list of subdomains or domains, one per line (e.g., generated from tools like subfinder or Amass).
2. s3scanner tool installed and accessible via Python.
3. AWS CLI installed (version 2 recommended) for bucket content enumeration.
4. Network access to AWS S3 endpoints (no authentication needed for public buckets).
5. Basic Linux/bash environment for execution.

## Defense

Defensive measures and detection strategies:

- Implement least-privilege access policies on S3 buckets using bucket policies and IAM roles to block public reads.
- Enable S3 server access logging and monitor CloudTrail for unusual ListBucket API calls from unknown IPs.
- Use AWS Config rules to alert on public bucket creation and scan existing buckets with tools like PIIFinder or AWS Trusted Advisor.
- Rate limiting and WAF rules can mitigate automated scanning attempts.

## Objectives

1. Discover publicly accessible S3 buckets associated with target subdomains.
2. Enumerate and list files within identified public buckets to assess data exposure.
3. Identify potential sensitive data leaks for further investigation or exploitation.

## Instructions

### Step 1: Scan Subdomains for Public S3 Buckets

**Context**: This step uses s3scanner to generate potential S3 bucket names from the input subdomain list and checks if they are publicly accessible. It filters out private buckets and outputs only those that allow anonymous reads, providing a starting point for data enumeration.

**Command** ([[commands/s3scanner-scan-subdomains-for-public-buckets]]):
```bash
python3 s3scanner.py -l $_DOMAIN_LIST -o $_OUTPUT_FILE
```

> The command reads the domain list file, tests derived bucket names (e.g., converting 'sub.example.com' to 'sub-example-com'), and writes public ones to the output file. Run this in the directory where s3scanner.py is located. If the bucket is public, it will be listed; otherwise, access is denied.

### Step 2: List Contents of Discovered Buckets

**Context**: After identifying public buckets, this step iterates through the output list to recursively list all objects (files and folders) within each bucket using AWS CLI. This reveals the structure and names of exposed data, helping to pinpoint valuable assets without downloading everything.

**Command** ([[commands/aws-s3-ls-list-bucket-contents]]):
```bash
for i in $(cat $_BUCKET_LIST); do aws s3 ls s3://$i --recursive 2>/dev/null || true; done;
```

> The loop processes each bucket name from the input file, executing 'aws s3 ls' to list contents. The --recursive flag shows all nested objects. Errors (e.g., permission denied on re-testing) are suppressed to continue processing. Successful output displays file paths, sizes, and last modified dates for each bucket.
