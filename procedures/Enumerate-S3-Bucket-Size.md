---
id: 95dbbaf1-5fc2-49e5-a86c-73ae8a7ea6eb
name: Enumerate-S3-Bucket-Size
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:53.661902+00:00'
updated_at: '2023-04-06T03:55:53.679503+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Active Scanning]]'
sub_techniques: []
tags:
  - '[[tags/Amazon Bucket S3 AWS]]'
  - '[[tags/Basic tests]]'
  - '[[tags/Check bucket disk size]]'
  - aws
  - s3
  - enumeration
  - reconnaissance
  - cloud
commands:
  - '[[commands/aws-s3-ls-recursive-no-sign]]'
  - '[[commands/sum-s3-object-sizes]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# Enumerate-S3-Bucket-Size

## Summary

This procedure demonstrates how to enumerate the total size of a publicly accessible Amazon S3 bucket without requiring AWS authentication credentials. By recursively listing all objects in the bucket and processing the output to sum file sizes, attackers can assess the volume of data stored, which helps evaluate the potential value of the target for further exploitation or data theft.

## Description

Amazon S3 buckets that are misconfigured as public allow unauthenticated access to list and potentially download contents. This procedure uses the AWS CLI in no-sign mode to bypass authentication, recursively enumerates all objects to retrieve their sizes, filters irrelevant output lines, and calculates the aggregate size in megabytes. This technique is useful in reconnaissance phases to gauge data quantity without alerting monitoring systems that require signed requests. It assumes the bucket permits anonymous LIST operations; if downloads are also public, this can be extended to exfiltration. The approach relies on standard AWS CLI piping with grep and awk for post-processing, making it lightweight and executable on any system with AWS CLI installed.

## Requirements

1. AWS CLI installed and accessible in the system's PATH.
2. Knowledge of the target S3 bucket name (e.g., obtained via subdomain enumeration or public leak searches).
3. Network access to AWS S3 endpoints (no VPN or proxy blocking required for public buckets).
4. Basic shell environment (Bash) for piping commands.

## Defense

- Configure S3 buckets with private access policies and block public ACLs to prevent anonymous listing.
- Enable AWS CloudTrail logging for S3 data events to monitor anonymous access attempts.
- Implement AWS Config rules to alert on public bucket exposures and use Macie for sensitive data discovery.
- Rate-limit API calls and monitor for unusual recursive LIST requests from unknown IPs.

## Objectives

1. Confirm public accessibility of the S3 bucket without authentication.
2. Recursively list all objects to gather size metadata.
3. Calculate and display the total storage size in megabytes to assess data volume.
4. Identify potential high-value targets based on size for prioritized follow-up enumeration or exfiltration.

## Instructions

### Step 1: List S3 Bucket Objects Without Authentication

**Context**: This step verifies public access and retrieves a recursive listing of all objects in the bucket, including their sizes. The --no-sign flag allows unauthenticated requests, which only succeed if the bucket permits anonymous LIST actions. This provides the raw data needed for size calculation.

**Command** ([[commands/aws-s3-ls-recursive-no-sign]]):
```bash
aws s3 ls s3://$_BUCKET_NAME --recursive --no-sign
```

> Replace $_BUCKET_NAME with the target bucket (e.g., example-bucket). This command outputs lines like '2023-01-01 12:00:00   1024 file.txt' for each object. If the bucket is private, it will error with 'AccessDenied'. Pipe this output directly to the next step or save to a file (e.g., > objects.txt) for offline processing.

### Step 2: Calculate Total Size from Listing Output

**Context**: Process the output from Step 1 to filter out header/footer lines and sum the size column (bytes) using awk, converting the total to megabytes. This aggregates the data volume without downloading files, providing a quick size estimate to inform attack decisions like feasibility of exfiltration.

**Command** ([[commands/sum-s3-object-sizes]]):
```bash
[output from Step 1] | grep -v -E "(Bucket: |Prefix: |LastWriteTime|^$|--)" | awk 'BEGIN {total=0}{total+=$3}END{print total/1024/1024" MB"}'
```

> Pipe the listing directly (e.g., aws ... | grep ... | awk ...) or use 'cat objects.txt |' if saved to file. The grep excludes non-data lines, and awk sums the third column (size in bytes), dividing by 1024^2 for MB. If no objects, output is '0 MB'.
