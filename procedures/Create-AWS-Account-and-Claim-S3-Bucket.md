---
id: proc-claim-s3-bucket
tags:
  - subdomain-takeover
  - aws-s3
  - initial-access
type: procedure
tools: []
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
updated_at: '2025-12-14T04:51:26.848Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create AWS Account and Claim S3 Bucket

## Summary

This procedure outlines creating an AWS account and registering an S3 bucket to claim a subdomain with a dangling CNAME, gaining control over the domain's resolution.

## Description

Attackers exploit unowned S3 endpoints by creating a bucket with the subdomain's exact name (e.g., news-static.semrush.com), which AWS routes traffic to. This targets cloud misconfigurations in web environments, with outcomes including full subdomain control for malicious hosting. Requires a valid email for AWS signup; no target credentials needed.

## Requirements

1. Valid email and phone for AWS verification
2. Internet access to AWS console
3. Identified vulnerable subdomain from prior recon

## Defense

Defensive measures and detection strategies:

- Register all potential S3 bucket names proactively
- Use AWS Organizations to monitor bucket creations
- Set up alerts for DNS changes via Route 53

## Objectives

1. Secure AWS account for S3 operations
2. Claim the subdomain by bucket creation
3. Verify control through resolution

## Instructions

### Step 1: Sign Up for AWS Account

**Context**: Establish access to S3 services.

**Instructions**: Visit aws.amazon.com, select 'Create an AWS Account', provide details, and complete verification. Use free tier to avoid costs.

> Upon success, access the S3 console at console.aws.amazon.com/s3.

### Step 2: Create and Configure S3 Bucket

**Context**: Register the bucket to hijack the CNAME.

**Instructions**: In S3 console, click 'Create bucket', enter 'news-static.semrush.com' as name, select region (e.g., us-east-1), uncheck 'Block all public access'. Add public read policy as shown in attack chain.

> Bucket creation claims the subdomain instantly due to DNS propagation.

### Step 3: Validate Claim

**Context**: Confirm takeover.

**Instructions**: Browse to http://news-static.semrush.com; it should show your bucket's default page or error if empty.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[aws-s3]]
- [[cloud]]
