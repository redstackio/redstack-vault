---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Remote System Discovery]]'
sub_techniques: []
tags:
  - aws-s3
  - reconnaissance
  - cloud-discovery
  - file-listing
commands:
  - '[[commands/dig-dns-lookup-s3-bucket-name]]'
  - '[[commands/nslookup-reverse-dns-s3-ip]]'
  - '[[commands/aws-s3-ls-bucket-no-auth]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# List-Files-in-S3-Bucket

## Summary

This procedure demonstrates how to list files in an Amazon S3 bucket, focusing on publicly accessible or unsecured buckets for reconnaissance purposes. It involves determining the bucket's AWS region via DNS resolution and then using the AWS CLI to enumerate contents without authentication, helping identify potential sensitive data exposure such as configuration files or credentials.

## Description

Amazon S3 buckets are commonly used for cloud storage, and misconfigurations can lead to public access, allowing attackers to enumerate and potentially exfiltrate data. This procedure targets such buckets by first resolving the bucket's endpoint to identify its region (as S3 regions affect access endpoints), then listing objects within the bucket. It assumes no valid AWS credentials are needed, relying on the --no-sign-request flag for anonymous access. This is useful in red team engagements to map cloud assets and discover valuable information during discovery phases. The target environment is AWS cloud infrastructure, and success depends on the bucket's permission settings.

## Requirements

1. AWS CLI installed on the attacker's machine (version 2 recommended for full S3 support).
2. Network access to AWS endpoints (no firewall blocks on ports 443 for HTTPS).
3. Knowledge of the target S3 bucket name (e.g., obtained from prior reconnaissance like subdomain enumeration).
4. Optional: Access to DNS resolution tools like dig or nslookup (standard on Linux/macOS).

## Defense

- Ensure S3 buckets are secured with bucket policies denying public access and using least-privilege IAM roles.
- Implement AWS CloudTrail logging to monitor S3 API calls, including anonymous requests, and set up alerts for unusual ListBucket operations.
- Use AWS Config rules to enforce encryption and access controls, and regularly audit bucket permissions with tools like PAWS or AWS IAM Access Analyzer.
- Deploy network security measures like AWS WAF or VPC endpoints to restrict access to S3 from unauthorized sources.

## Objectives

1. Resolve the S3 bucket's IP address and determine its AWS region via DNS lookups.
2. Enumerate files and objects within the S3 bucket without authentication.
3. Identify any sensitive data or structure in the bucket for further exploitation.

## Instructions

### Step 1: Resolve S3 Bucket DNS to Obtain IP Address

**Context**: S3 bucket names resolve to regional endpoints. Use DNS lookup to get the IP address associated with the bucket, which is necessary for subsequent reverse lookup to identify the region. This step avoids trial-and-error region guessing, as S3 buckets are region-specific.

**Command** ([[commands/dig-dns-lookup-s3-bucket-name]]):
```bash
dig $_BUCKET_NAME
```

> This command queries DNS for the A record of the S3 bucket name. If the bucket exists and is publicly resolvable, it returns the IP address of the S3 endpoint. Replace $_BUCKET_NAME with the target bucket (e.g., flaws.cloud). If no IP is returned, the bucket may not exist or be private.

**Expected Output**:
```
;; ANSWER SECTION:
flaws.cloud.    5    IN    A    52.218.192.11
```

### Step 2: Perform Reverse DNS Lookup to Identify AWS Region

**Context**: With the IP address from Step 1, perform a reverse DNS lookup to reveal the S3 endpoint hostname, which includes the region (e.g., us-west-2). This ensures the correct --region flag is used in AWS CLI commands, preventing access errors.

**Command** ([[commands/nslookup-reverse-dns-s3-ip]]):
```bash
nslookup $_IP_ADDRESS
```

> This command resolves the IP back to a hostname in the format s3-website-{region}.amazonaws.com or similar. Use the extracted region (e.g., us-west-2) for the next step. If the reverse lookup fails, try alternative tools like host or whois for IP details.

**Expected Output**:
```
Non-authoritative answer:
11.192.218.52.in-addr.arpa name = s3-website-us-west-2.amazonaws.com.
```

### Step 3: List Contents of the S3 Bucket

**Context**: Now that the region is known, use the AWS CLI to list objects in the bucket anonymously. This step verifies public access and enumerates the file structure. If the bucket is secured, this will fail with an access denied error, indicating no exposure.

**Command** ([[commands/aws-s3-ls-bucket-no-auth]]):
```bash
aws s3 ls s3://$_BUCKET_NAME/ --no-sign-request --region $_REGION
```

> This command lists all objects in the root of the specified S3 bucket without signing the request (anonymous access). The --region flag must match the bucket's location from Step 2. For nested directories, add --recursive for full enumeration. Success confirms public readability; failure suggests private bucket.

**Expected Output**:
```
2023-01-01 12:00:00     1234 example-file.txt
2023-01-02 13:00:00      567 config.json
```

> Output shows object keys, sizes, and last modified dates. Look for sensitive files like .env, credentials, or backups.
