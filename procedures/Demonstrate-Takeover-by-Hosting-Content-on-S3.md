---
id: 123e4567-e89b-12d3-a456-426614174003
name: Demonstrate Takeover by Hosting Content on S3
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:23.524Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Remote File Copy]]'
sub_techniques:
  - '[[T1105.003]]'
tags:
  - subdomain-takeover
  - xss
  - phishing
  - aws-s3
commands:
  - '[[commands/aws-upload-file-to-s3]]'
platforms:
  - AWS
  - Web
tools:
  - '[[tools/AWS-CLI]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---

# Demonstrate Takeover by Hosting Content on S3

## Summary

This procedure uploads arbitrary content, such as an XSS PoC, to the claimed S3 bucket to demonstrate full subdomain control and potential for malicious payloads.

## Description

After claiming the bucket, attackers can host HTML, scripts, or redirects on the subdomain. In this case, an XSS.html file was uploaded to http://users.tweetdeck.com/XSS.html, proving the ability to inject scripts into user sessions or distribute malware.

## Requirements

1. Claimed S3 bucket with write access
2. AWS CLI configured
3. Local file prepared for upload (e.g., HTML PoC)

## Defense

Defensive measures and detection strategies:

- Enable S3 bucket logging and monitor uploads
- Implement WAF rules to block unexpected content on subdomains
- Conduct regular subdomain takeover scans with tools like Subjack

## Objectives

1. Upload PoC content to bucket
2. Verify accessibility via subdomain
3. Simulate impact like XSS execution

## Instructions

### Step 1: Prepare and Upload PoC File

**Context**: Create a test file and sync it to S3 for serving.

**Command** ([[commands/aws-upload-file-to-s3]]):
```bash
echo '<script>alert("XSS via Takeover")</script>' > XSS.html
aws s3 cp XSS.html s3://users.tweetdeck.com/XSS.html --region us-east-1
```

> Output: upload: XSS.html to s3://users.tweetdeck.com/XSS.html.

### Step 2: Verify Hosting

**Context**: Access the uploaded content to confirm control.

**Command** ([[commands/curl-fetch-url]]):
```bash
curl http://users.tweetdeck.com/XSS.html
```

> Expected: The HTML script content is returned, executable in browsers.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques

- [[T1105.003]]

## Commands Used

- [[commands/aws-upload-file-to-s3]]
- [[commands/curl-fetch-url]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- [[xss]]
- [[malware-hosting]]
