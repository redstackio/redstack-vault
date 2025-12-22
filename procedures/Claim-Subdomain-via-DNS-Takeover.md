---
id: proc-uuid-claim-1181762
name: Claim-Subdomain-via-DNS-Takeover
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:26.830Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - subdomain-takeover
  - dns
  - initial-access
commands:
  - '[[commands/dig-verify-takeover]]'
platforms:
  - AWS
  - Cloud
tools:
  - '[[tools/dig]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Claim-Subdomain-via-DNS-Takeover

## Summary

This procedure demonstrates claiming a dangling subdomain by registering the associated cloud resource, such as an S3 bucket or Elastic IP linked to a terminated EC2 instance, to redirect traffic and impersonate the service.

## Description

Once a dangling DNS record is identified (e.g., pointing to terminated EC2), if the record aliases a claimable AWS service, create the resource with the matching name. For EC2-related IPs, request release if possible. Update DNS propagation allows control. This enables hosting phishing pages or malicious scripts under the legitimate domain, compromising brand trust. Requires an AWS account for claiming.

## Requirements

1. AWS account with permissions to create resources (e.g., S3 buckets)
2. Identified dangling DNS record from prior reconnaissance
3. Knowledge of the exact resource type (e.g., CNAME target)

## Defense

Defensive measures and detection strategies:

- Lock down resource names to prevent squatting (e.g., reserved S3 bucket names)
- Use DNSSEC for integrity checks
- Monitor subdomain resolutions and alert on changes to non-owned IPs

## Objectives

1. Gain control over the subdomain by claiming the dangling resource
2. Redirect traffic to attacker-controlled content
3. Achieve phishing or impersonation for further exploitation

## Instructions

### Step 1: Register the Dangling Resource

**Context**: Create the cloud resource matching the DNS target to hijack it.

**Command** (AWS CLI example, assuming S3-like):
```bash
aws s3 mb s3://exact-bucket-name-from-dns --region us-east-1
```

> Use AWS CLI to create the resource. For EC2 Elastic IP, use `aws ec2 allocate-address`. The DNS will propagate to your new resource.

### Step 2: Verify Takeover

**Context**: Confirm the subdomain now points to your resource.

**Command** ([[commands/dig-verify-takeover]]):
```bash
dig ███.wavecell.com
```

> Re-query DNS and access the subdomain URL. Successful if it serves your uploaded test page (e.g., via S3 static hosting).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/dig-verify-takeover]]

## Tools Used

- [[tools/dig]]

## Tags

- [[subdomain-takeover]]
- [[DNS]]
- [[initial-access]]
