---
tags:
  - phishing
  - content-hosting
  - subdomain-hijack
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T04:51:26.496Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[T1105.003]]'
id: 682f0b8a-9258-4d7b-ab8a-29fd520736b9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Host Content on Taken Over Subdomain

## Summary

This procedure uploads custom content to a claimed S3 bucket and verifies that the subdomain resolves to it, completing the takeover and enabling attacks like phishing.

## Description

After claiming the bucket, attackers upload HTML or other files configured for public access. For the Equifax subdomain test.www.midigator.com, this allows serving fake pages under the trusted domain. The technical approach uses S3's static hosting; prerequisites include bucket ownership. Expected outcomes: subdomain serves attacker content, leading to impersonation, phishing, or reputation harm. Target is web browsers accessing the subdomain.

## Requirements

1. Control over the claimed S3 bucket
2. AWS CLI or console access
3. Custom content files (e.g., index.html with PoC)

## Defense

Defensive measures and detection strategies:

- Implement bucket policies restricting public access post-creation
- Monitor web traffic for anomalous content on subdomains
- Use certificate transparency logs to detect unauthorized domain usage

## Objectives

1. Demonstrate full control by serving custom content
2. Validate the takeover's impact through accessibility
3. Enable follow-on attacks like phishing under the victim's domain

## Instructions

### Step 1: Upload Content to Bucket

**Context**: Prepare and sync files to the S3 bucket root for immediate serving as the index page.

**Command**:
```bash
echo "<h1>Proof of Subdomain Takeover</h1><p>Hosted on claimed S3 bucket.</p>" > index.html
echo "Error page" > error.html
aws s3 cp index.html s3://test.www.midigator.com/ --region us-west-1
aws s3 cp error.html s3://test.www.midigator.com/ --region us-west-1
```

> These commands create sample files and upload them. Expected output: "upload: index.html to s3://test.www.midigator.com/index.html". Ensure public-read ACL if needed: `aws s3api put-object-acl --bucket test.www.midigator.com --key index.html --acl public-read --region us-west-1`.

### Step 2: Verify Serving

**Context**: Access the subdomain URL to confirm it loads the uploaded content instead of AWS errors.

**Instructions**: Open http://test.www.midigator.com in a browser or use curl: `curl http://test.www.midigator.com`. Look for the custom HTML in the response.

> Successful verification shows the PoC page, often captured via screenshot for reports.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques

- [[T1105.003]]

## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[subdomain-hijack]]
