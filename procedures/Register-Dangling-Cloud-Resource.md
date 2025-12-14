---
id: proc-uuid-register-dangling-resource
tags:
  - aws
  - cloud
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/aws-create-bucket]]'
verified: false
platforms:
  - Cloud
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:26.460Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Register Dangling Cloud Resource

## Summary

This procedure claims a dangling cloud resource (e.g., AWS S3 bucket) referenced by a subdomain's DNS record, achieving control over the subdomain without direct access to the target's infrastructure.

## Description

Following discovery of a dangling DNS record under mozaws.net pointing to a non-existent AWS resource, this step involves registering that exact resource name on the cloud provider. Once claimed, incoming DNS traffic routes to the attacker's instance, enabling takeover. This targets cloud environments like AWS and requires a new or existing account on the provider. Outcomes include full control of the subdomain for further exploitation.

## Requirements

1. Identified dangling resource name from DNS query.
2. AWS account (free tier sufficient for basic services).
3. AWS CLI installed and configured.

## Defense

Defensive measures and detection strategies:

- Use reserved resource names or locks to prevent squatting.
- Monitor cloud provider logs for new resource creations matching DNS entries.
- Implement DNS TTL reductions and validation scripts.

## Objectives

1. Secure ownership of the dangling resource.
2. Route subdomain traffic to attacker-controlled endpoint.
3. Validate takeover success.

## Instructions

### Step 1: Create the Resource

**Context**: Register the exact resource (e.g., S3 bucket) named in the dangling DNS CNAME.

**Command** ([[commands/aws-create-bucket]]):
```bash
aws s3api create-bucket --bucket dangling-subdomain.mozaws.net --region us-east-1
```

> This creates the bucket if available. Expected output: JSON confirmation of bucket creation.

### Step 2: Configure Public Access

**Context**: Enable public serving to receive DNS-routed traffic.

**Command** ([[commands/aws-create-bucket]] with policy):
```bash
aws s3api put-bucket-policy --bucket dangling-subdomain.mozaws.net --policy file://public-policy.json
```

> Upload a policy allowing public reads. Success if bucket is accessible via HTTP.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

- [[commands/aws-create-bucket]]

## Tools Used

-

## Tags

- [[aws]]
- [[cloud]]
- [[subdomain-takeover]]
