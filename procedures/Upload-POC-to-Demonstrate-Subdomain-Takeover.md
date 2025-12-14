---
tags:
  - poc
  - upload
  - demonstration
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/aws-s3-cp-upload-poc]]'
platforms:
  - AWS
techniques:
  - '[[Remote File Copy]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 30387d38-248c-408a-91fe-e71106c29cf6
created_at: '2025-12-14T04:38:49.849Z'
updated_at: '2025-12-14T04:38:49.849Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-POC-to-Demonstrate-Subdomain-Takeover

## Summary

This procedure uploads a proof-of-concept file to the claimed CloudFront origin, demonstrating control over the subdomain by serving custom content.

## Description

After claiming, attackers upload an index.html (e.g., phishing page) to the origin server (S3/EC2), making it accessible via the subdomain. This proves takeover and simulates impacts like brand spoofing or cookie theft. For cdn.grab.com, it enables serving malicious JS for session hijacking if cookies are domain-scoped.

## Requirements

1. Claimed CloudFront distribution
2. Configured origin (e.g., S3 bucket)
3. POC file prepared (index.html with demo content)

## Defense

Defensive measures and detection strategies:

- Implement WAF rules to block unexpected content on CDNs
- Use certificate pinning or HSTS to prevent MITM
- Scan subdomains regularly with tools like Sublist3r and takeover checkers

## Objectives

1. Serve custom content from the subdomain
2. Verify accessibility and control
3. Highlight potential for phishing or exfiltration

## Instructions

### Step 1: Upload POC File

**Context**: Copy the HTML file to the S3 origin bucket.

**Command** ([[commands/aws-s3-cp-upload-poc]]):
```bash
aws s3 cp index.html s3://attacker-bucket/ --acl public-read
```

> Makes file public; index.html could contain <h1>Takeover POC</h1> or phishing form. Success: No errors, file listed.

### Step 2: Access and Verify

**Context**: Browse to the subdomain to confirm serving.

**Command** ([[commands/aws-s3-cp-upload-poc]]):
```bash
curl http://cdn.grab.com/index.html
```

> Outputs POC content, confirming takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/aws-s3-cp-upload-poc]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- [[poc]]
- [[upload]]
- [[demonstration]]
