---
id: proc-uuid-003
tags:
  - subdomain-takeover
  - aws
  - cloudfront
  - exploit
type: procedure
tools:
  - '[[tools/AWS-CloudFront]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:38:39.996Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create CloudFront Distribution for Takeover

## Summary

This procedure exploits a dangling CNAME by creating a new AWS CloudFront distribution configured with the target subdomain as an alternate domain name, allowing the attacker to host arbitrary content and claim control.

## Description

Once a dangling CNAME to CloudFront is identified, an attacker with an AWS account can create a distribution that matches the CNAME, effectively taking over the subdomain. The distribution is pointed to an origin like an S3 bucket hosting PoC files (e.g., phishing pages). This bypasses the need for domain ownership, as CloudFront validates only the CNAME match. Impact includes serving malicious content on the victim's domain.

## Requirements

1. Valid AWS account with CloudFront permissions
2. Identified dangling CNAME (e.g., rider.uber.com -> d123.cloudfront.net)
3. S3 bucket or custom origin for hosting content

## Defense

Defensive measures and detection strategies:

- Delete or re-point dangling CNAMEs immediately after service migrations
- Monitor AWS for unauthorized distributions using the subdomain CNAME
- Use AWS Config rules to alert on unclaimed CloudFront resources

## Objectives

1. Claim the subdomain by associating the CNAME with a new distribution
2. Host attacker-controlled content
3. Demonstrate full control without apex domain access

## Instructions

### Step 1: Set Up Origin

**Context**: Prepare content to serve from the distribution.

Create an S3 bucket and upload PoC files (e.g., index.html with "Takeover Successful").

> Make the bucket public for static hosting.

### Step 2: Create Distribution

**Context**: Configure CloudFront to use the dangling CNAME.

In AWS Console: Navigate to CloudFront > Create Distribution. Set Alternate Domain Names (CNAMEs) to rider.uber.com. Select the S3 origin. Deploy the distribution.

> Wait for deployment (10-15 minutes). The distribution ID will be assigned, and CNAME validated.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/AWS-CloudFront]]

## Tags

- [[subdomain-takeover]]
- [[aws]]
- [[cloudfront]]
- [[exploit]]
