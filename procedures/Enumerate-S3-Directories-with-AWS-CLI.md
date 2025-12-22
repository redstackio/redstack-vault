---
id: proc-uuid-3
tags:
  - aws
  - s3
  - enumeration
  - cli
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/aws-s3-ls-root]]'
  - '[[commands/aws-s3-ls-admin-directory]]'
  - '[[commands/aws-s3-ls-beta-directory]]'
  - '[[commands/aws-s3-ls-localhost-directory]]'
  - '[[commands/aws-s3-ls-production-directory]]'
verified: false
platforms:
  - AWS
  - Cloud
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Cloud Storage]]'
updated_at: '2025-12-14T17:28:58.508Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Cloud Storage]]'
---
# Enumerate-S3-Directories-with-AWS-CLI

## Summary

This procedure uses AWS CLI to list contents of a public S3 bucket's root and subdirectories, revealing sensitive files for collection and potential exfiltration.

## Description

Leveraging the AWS Command Line Interface, attackers enumerate directories like admin, production, beta, and localhost in a misconfigured DoD S3 bucket. This automates discovery of manuals, documents, and media, building on browser access for efficient data harvesting in cloud environments.

## Requirements

1. AWS CLI installed and accessible
2. Public bucket path (no AWS credentials configured)
3. Terminal or command prompt

## Defense

Defensive measures and detection strategies:

- Encrypt S3 objects and restrict public ACLs
- Monitor for ListBucket API calls from unknown IPs via CloudTrail
- Use VPC endpoints to limit public internet access to S3

## Objectives

1. List all accessible directories and files
2. Identify sensitive DoD content
3. Facilitate targeted downloads

## Instructions

### Step 1: List Root Directory

**Context**: Enumerate top-level contents to overview exposure.

**Command** ([[commands/aws-s3-ls-root]]):
```bash
aws s3 ls s3://███/
```

> This lists objects in the root, showing directories like admin and production. Expected output: File names, sizes, and dates.

### Step 2: Enumerate Admin/Production Directory

**Context**: Dive into sensitive subfolders.

**Command** ([[commands/aws-s3-ls-admin-directory]]):
```bash
aws s3 ls s3://████/██████/
```

> Reveals manuals and media. Repeat for other paths.

### Step 3: Enumerate Beta Directory

**Context**: Check versioned or testing data.

**Command** ([[commands/aws-s3-ls-beta-directory]]):
```bash
aws s3 ls s3://███████/███████████████/
```

> Output includes DoD-related files.

### Step 4: Enumerate Localhost Directory

**Context**: Explore development artifacts.

**Command** ([[commands/aws-s3-ls-localhost-directory]]):
```bash
aws s3 ls s3://██████████/███████/
```

> Lists additional sensitive items.

### Step 5: Enumerate Additional Production Directory

**Context**: Cover remaining paths.

**Command** ([[commands/aws-s3-ls-production-directory]]):
```bash
aws s3 ls s3://██████████/████/
```

> Completes enumeration of exposed content.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Cloud Storage]] Data from Cloud Storage Object

### Sub-Techniques


## Commands Used

- [[commands/aws-s3-ls-root]]
- [[commands/aws-s3-ls-admin-directory]]
- [[commands/aws-s3-ls-beta-directory]]
- [[commands/aws-s3-ls-localhost-directory]]
- [[commands/aws-s3-ls-production-directory]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- aws
- s3
- collection
- enumeration
