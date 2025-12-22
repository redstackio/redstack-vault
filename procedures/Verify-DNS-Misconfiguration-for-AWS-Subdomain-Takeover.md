---
id: proc-uuid-2
tags:
  - dns-misconfig
  - aws-takeover
  - verification
type: procedure
tools:
  - '[[tools/Dig]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/dig-lookup-subdomain]]'
verified: false
platforms:
  - AWS
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:31.224Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify DNS Misconfiguration for AWS Subdomain Takeover

## Summary

This procedure confirms a DNS misconfiguration by verifying that a subdomain's record points to a terminated AWS resource, assessing the feasibility of claiming control via resource naming conflicts like S3 buckets.

## Description

Targeting environments like AWS, this verifies persistence of DNS records post-resource termination. In the 8x8 incident, the subdomain █.staging.█.8x8.com's CNAME to a defunct EC2 allowed takeover. It involves DNS queries and resource checks; prerequisites are public access and AWS knowledge. Outcomes: Confirmation of vulnerability for impersonation or malicious hosting.

## Requirements

1. Access to DNS resolution tools
2. Ability to query public AWS endpoints
3. AWS account for testing resource claims (optional for verification)

## Defense

Defensive measures and detection strategies:

- Automate DNS cleanup scripts on EC2 termination
- Monitor for unresolved CNAMEs using AWS CloudWatch or external scanners
- Enforce least privilege on DNS management to prevent lingering records

## Objectives

1. Validate dangling DNS status
2. Confirm resource availability for takeover
3. Assess impact on staging environment

## Instructions

### Step 1: Query Specific Subdomain DNS

**Context**: Perform a targeted lookup to confirm the record points to a terminated resource.

**Command** ([[commands/dig-lookup-subdomain]]):
```bash
dig +short █.staging.█.8x8.com
```

> This retrieves the CNAME or IP. Expected output: Resolution to an EC2 alias that returns no active response, indicating termination.

### Step 2: Check Resource Termination and Claimability

**Context**: Manually or via AWS CLI verify the EC2 is gone and the name is free (e.g., try creating S3 bucket with the alias).

**Command** ([[commands/dig-lookup-subdomain]]):
```bash
dig +trace █.staging.█.8x8.com
```

> Use trace for full delegation path. Expected output: Confirms persistence without active backend; success if AWS resource creation doesn't conflict with active services.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/dig-lookup-subdomain]]

## Tools Used

- [[tools/Dig]]

## Tags

- [[dns-misconfig]]
- [[aws-takeover]]
