---
tags:
  - information-disclosure
  - aws-s3
  - bucket-enumeration
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-list-s3-bucket]]'
platforms:
  - AWS
techniques:
  - '[[Data from Information Repositories]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[Sharepoint]]'
id: 816c4c0d-adaa-4800-8024-6da092a38c6e
created_at: '2025-12-14T17:25:13.469Z'
updated_at: '2025-12-14T17:25:13.469Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---
# List-Contents-of-Public-AWS-S3-Bucket

## Summary

This procedure enumerates the contents of a publicly accessible AWS S3 bucket, allowing unauthorized listing and potential download of sensitive files or endpoints.

## Description

AWS S3 buckets with public read and list permissions expose their directory structure and files to anyone with the URL. JetBlue's bucket at https://███████.travelproducts.jetblue.com/ is misconfigured this way, enabling attackers to discover internal documents, configurations, or API endpoints without credentials.

## Requirements

1. Public URL to the S3 bucket
2. Basic HTTP tools for listing
3. No AWS credentials needed

## Defense

Defensive measures and detection strategies:

- Set bucket policies to deny public access
- Enable S3 access logging and monitor for list operations
- Use AWS Config rules to detect public buckets

## Objectives

1. List bucket objects
2. Identify sensitive files
3. Download or reference exposed data

## Instructions

### Step 1: Retrieve Bucket Listing

**Context**: Fetch the root directory listing to view available objects.

**Command** ([[commands/curl-list-s3-bucket]]):
```bash
curl -s https://███████.travelproducts.jetblue.com/
```

> Outputs XML or HTML with <Key> elements listing files and folders. Parse for sensitive names like configs or backups.

### Step 2: Extract File Links

**Context**: Parse the response to get direct links to contents.

**Command** ([[commands/curl-list-s3-bucket]]):
```bash
curl -s https://███████.travelproducts.jetblue.com/ | grep -o 'href="[^"]*"' | cut -d'"' -f2
```

> Lists href paths, allowing follow-up downloads of individual files.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Data from Information Repositories]] Data from Information Repositories

### Sub-Techniques

- [[Sharepoint]] SharePoint

## Commands Used

- [[commands/curl-list-s3-bucket]]

## Tools Used


## Tags

- information-disclosure
- aws-s3
