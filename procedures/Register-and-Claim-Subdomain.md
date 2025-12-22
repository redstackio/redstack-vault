---
id: proc-uuid-register-claim-subdomain
tags:
  - subdomain-takeover
  - dns
  - aws
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/dig-dns-lookup]]'
verified: false
platforms:
  - DNS
  - Cloud (AWS)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:38:39.464Z'
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
# Register and Claim Subdomain

## Summary

This procedure claims control of a dangling subdomain by registering it with the service provider referenced in the DNS record, such as an unclaimed AWS S3 bucket, allowing the attacker to redirect traffic to their infrastructure.

## Description

For the mozaws.net case, the dangling CNAME points to an inactive AWS resource. The attacker creates an account on AWS and registers the exact resource name (e.g., bucket), which automatically claims the DNS resolution. This grants full control over the subdomain without altering the original DNS.

## Requirements

1. Account on the target provider (e.g., AWS for S3).
2. Identified dangling record from prior reconnaissance.
3. Understanding of the provider's claiming process (e.g., S3 bucket naming rules).

## Defense

Defensive measures and detection strategies:

- Pre-emptively claim all potential dangling resources on common providers.
- Monitor for new registrations on critical resource names using provider alerts.
- Use automated scanners like dnstakeover to detect and notify on takeovers.

## Objectives

1. Secure control of the subdomain via provider registration.
2. Verify DNS propagation to the new resource.
3. Prepare for content hosting.

## Instructions

### Step 1: Identify Target Provider

**Context**: Determine the service from the CNAME (e.g., s3.amazonaws.com).

Review prior DNS output to confirm provider.

### Step 2: Register Resource

**Context**: Create the resource matching the dangling name.

For AWS S3, use AWS Console or CLI:

```bash
aws s3 mb s3://dangling-bucket-name
```

> Expected output: Bucket created successfully.

### Step 3: Verify Claim

**Context**: Confirm DNS now points to your resource.

Use [[commands/dig-dns-lookup]]:

**Command** ([[commands/dig-dns-lookup]]):
```bash
dig +short CNAME vulnerable-sub.mozaws.net
```

> Expected output: Resolves to your new bucket's endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-lookup]]

## Tools Used


## Tags

- [[subdomain-takeover]]
- [[aws]]
