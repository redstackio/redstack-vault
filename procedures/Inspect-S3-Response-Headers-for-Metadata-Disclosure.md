---
id: proc-001-inspect-s3-headers
tags:
  - information-disclosure
  - s3
  - aws
  - metadata
  - reconnaissance
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-fetch-headers]]'
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:25:12.829Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Inspect-S3-Response-Headers-for-Metadata-Disclosure

## Summary

This procedure demonstrates how to passively inspect HTTP response headers from S3-served objects to uncover disclosed system metadata, such as the 'root' username, file permissions, timestamps, and MD5 hashes, aiding in reconnaissance without active exploitation.

## Description

In scenarios where S3 objects are uploaded using tools like s3cmd without proper flags, local file metadata is preserved in the `x-amz-meta-s3cmd-attrs` header. This procedure targets public web endpoints serving such objects, using simple header inspection to reveal sensitive information. The attack requires no authentication and can be performed with basic tools like curl or a browser's developer tools. Expected outcomes include exposure of system usernames (e.g., 'root'), UIDs/GIDs, modes, and timestamps, which could assist attackers in mapping the target's environment.

## Requirements

1. Network access to the target HTTPS URL (e.g., https://federation.data.gov/)
2. Installation of curl or equivalent HTTP client
3. Basic knowledge of HTTP headers and browser developer tools

## Defense

Defensive measures and detection strategies:

- Use s3cmd with the `--no-preserve` flag during uploads to strip metadata
- Configure S3 bucket policies to exclude custom metadata headers from responses
- Monitor access logs for unusual header inspection requests (e.g., repeated HEAD requests)
- Implement WAF rules to detect or block requests probing for specific headers

## Objectives

1. Gather victim host information through passive observation of public responses
2. Identify potential misconfigurations in cloud storage setups
3. Collect metadata for further reconnaissance or social engineering

## Instructions

### Step 1: Fetch Response Headers

**Context**: Retrieve the HTTP headers from the target S3-served resource to locate the metadata-disclosing header.

**Command** ([[commands/curl-fetch-headers]]):
```bash
curl -I https://federation.data.gov/
```

> This command performs a HEAD request to fetch headers without downloading the body. Expected output includes all response headers; scan for `x-amz-meta-s3cmd-attrs` containing details like `uid:0/gname:root/uname:root/gid:0/mtime:1482273904`.

### Step 2: Analyze Metadata

**Context**: Parse the extracted header for sensitive information to assess disclosure impact.

**Command** (Manual inspection or grep):
```bash
curl -I https://federation.data.gov/ | grep x-amz-meta-s3cmd-attrs
```

> Filter specifically for the metadata header. Successful output reveals system attributes, indicating a vulnerability if non-default info like 'root' is present.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-headers]]

## Tools Used

- [[tools/curl]]

## Tags

- information-disclosure
- s3
- aws
- metadata
- reconnaissance
