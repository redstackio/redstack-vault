---
tags:
  - hosting
  - poc
  - subdomain-takeover
  - phishing
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - AWS
  - Web
techniques:
  - '[[Remote File Copy]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: b900887b-e1a0-43c4-97ec-9e91d2223409
created_at: '2025-12-14T05:32:31.165Z'
updated_at: '2025-12-14T05:32:31.165Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Host Proof-of-Concept on Taken-Over Subdomain

## Summary

This procedure demonstrates hosting a proof-of-concept webpage on a claimed AWS S3 bucket to validate subdomain takeover and showcase potential impacts like cookie theft or phishing.

## Description

With the S3 bucket claimed, configure it for static website hosting and upload PoC content (e.g., HTML for cookie exfiltration). The subdomain now serves this content, proving control. This targets web-facing subdomains in AWS setups. Expected outcomes: Accessible malicious page at the subdomain URL, enabling attacks like bypassing CSP/CORS or SSRF whitelisting via trusted domain.

## Requirements

1. Claimed S3 bucket from prior step
2. Static HTML files for PoC (e.g., JavaScript for cookie theft)
3. Public read access configured on bucket

## Defense

Defensive measures and detection strategies:

- Enable S3 bucket logging and monitor for unexpected uploads
- Implement domain takeover detection tools like dnstake or subjack
- Use CSP and CORS policies that don't rely solely on subdomain trust

## Objectives

1. Validate subdomain control by serving content
2. Demonstrate attack impacts (phishing, theft)
3. Highlight risks for remediation

## Instructions

### Step 1: Configure Bucket for Hosting

**Context**: Enable static website hosting on the S3 bucket.

In AWS console: S3 > Bucket > Properties > Static website hosting > Enable, set index document to index.html.

Also, update bucket policy for public read:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicRead",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::unclaimed-bucket-name/*"
    }
  ]
}
```

> Apply policy; success: Bucket endpoint accessible publicly.

### Step 2: Upload PoC Content

**Context**: Serve a test page demonstrating control.

Upload index.html with PoC (e.g., <script>alert('Takeover');</script> or cookie theft script) via console or CLI.

```bash
aws s3 cp index.html s3://unclaimed-bucket-name/
```

> Access at https://www.███████/ (or punycode); expected: Page loads from subdomain.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[hosting]]
- [[poc]]
- [[subdomain-takeover]]
