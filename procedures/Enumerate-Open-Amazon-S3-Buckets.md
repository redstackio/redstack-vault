---
type: procedure
tactics:
  - '[[Discovery]]'
techniques:
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - aws
  - s3
  - bucket-enumeration
  - discovery
  - open-bucket
platforms:
  - AWS
  - Web
commands:
  - '[[commands/curl-check-s3-bucket]]'
  - '[[commands/curl-extract-s3-bucket-name]]'
tools: []
verified: true
validated: true
---

# Enumerate Open Amazon S3 Buckets

## Summary

Enumerate Open Amazon S3 Buckets is a discovery technique that identifies publicly accessible S3 storage buckets, which may expose sensitive data like database backups, user records, or application code. This procedure covers methods to check for open buckets by name, attempt public listings, and extract hidden bucket names from website paths using URL encoding tricks.

## Description

Amazon S3 buckets are object storage services often misconfigured to be publicly readable, leading to data leaks. Attackers enumerate them during reconnaissance to gather intelligence. This involves direct URL access to check accessibility, querying public indexes for known open buckets, and exploiting site-specific paths that reveal S3 usage. The technique targets the AWS cloud environment and relies on HTTP requests to probe without authentication. Success depends on misconfigurations like public ACLs or enabled bucket listing. Use this in red team engagements to simulate data discovery, but note legal restrictions on real-world probing.

## Requirements

1. Internet connectivity to reach AWS endpoints.
2. A web browser or command-line tool like curl for HTTP requests.
3. Optional: Suspected bucket names from OSINT or a target website URL for path-based extraction.
4. No AWS credentials required for public buckets.

## Defense

- Configure S3 buckets as private by default and use bucket policies to deny public access.
- Disable public listing on the S3 service endpoint if not needed.
- Monitor AWS CloudTrail for unusual access patterns to buckets.
- Use server-side encryption and access logging to protect data.
- Scan websites for exposed S3 paths and implement path normalization to prevent encoding bypasses.

## Objectives

1. Identify publicly accessible S3 buckets and their contents.
2. Extract hidden S3 bucket names from third-party website integrations.
3. Gather sensitive data for further exploitation or reporting in security assessments.

## Instructions

### Step 1: Check Specific S3 Bucket Accessibility

**Context**: Test if a known or guessed bucket name is publicly accessible by sending an HTTP request to the S3 endpoint. This reveals if the bucket exists and allows listing contents without auth.

**Command** ([[commands/curl-check-s3-bucket]]):
```bash
curl http://s3.amazonaws.com/$_BUCKET_NAME/
```

> Replace $_BUCKET_NAME with the target bucket (e.g., 'example-bucket'). If open, this returns an XML listing of objects. Also try the regional format: http://$_BUCKET_NAME.s3.amazonaws.com/. For known open bucket searches, visit https://buckets.grayhatwarfare.com/ or http://flaws.cloud.s3.amazonaws.com/ in a browser to query databases of exposed buckets.

### Step 2: Attempt Public Bucket Listing

**Context**: If the S3 account has public bucket listing enabled (rare but possible misconfig), query the root endpoint to retrieve a list of all buckets. This provides a starting point for further checks.

**Instructions**: Use curl to GET the S3 root URL. Expected response is XML if listing is allowed; otherwise, a 403 Forbidden.

```bash
curl http://s3.amazonaws.com/
```

> Success shows <ListAllMyBucketsResult> with <Buckets> containing names like <Name>example-bucket</Name>. Use discovered names in Step 1.

### Step 3: Extract Bucket Name from Website Path

**Context**: Many websites store assets in S3 buckets. Append URL encoding (%C0, representing a null byte or path traversal) to a resource path to force an error response that leaks the backend S3 bucket name.

**Command** ([[commands/curl-extract-s3-bucket-name]]):
```bash
curl "http://$_TARGET_DOMAIN/$_RESOURCE_PATH%C0"
```

> Set $_TARGET_DOMAIN to the site (e.g., 'example.com') and $_RESOURCE_PATH to a known path (e.g., 'images/avatar/123'). The response may include errors like 'NoSuchKey' revealing the S3 bucket, e.g., 'example-bucket.s3.amazonaws.com'. If successful, proceed to Step 1 to browse the extracted bucket.
