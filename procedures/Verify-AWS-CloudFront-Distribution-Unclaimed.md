---
tags:
  - aws
  - cloudfront
  - verification
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/aws-cloudfront-list-distributions]]'
platforms:
  - AWS
techniques:
  - '[[Hardware]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: f7065d07-6f75-454a-9a75-159a6c114481
created_at: '2025-12-14T04:38:49.853Z'
updated_at: '2025-12-14T04:38:49.853Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Verify-AWS-CloudFront-Distribution-Unclaimed

## Summary

This procedure checks if an AWS CloudFront distribution referenced by a target's DNS CNAME is unclaimed, meaning it's not associated with the domain owner's AWS account, allowing potential takeover.

## Description

Attackers verify CloudFront ownership by querying AWS APIs or console for the distribution ID from the CNAME (e.g., *.cloudfront.net). If unclaimed, anyone can associate it. This targets misconfigurations where services are deleted but DNS isn't updated, as in the cdn.grab.com case. Requires AWS CLI setup or console access; used post-DNS recon to confirm exploitability.

## Requirements

1. AWS CLI installed and configured (for API queries)
2. Distribution ID from DNS lookup
3. Access to AWS console for manual verification

## Defense

Defensive measures and detection strategies:

- Use AWS Config to monitor distribution associations
- Scan for dangling DNS records with tools like Subjack or DNSDumpster
- Enable CloudFront access logs and alert on unauthorized associations

## Objectives

1. Query for distribution ownership tied to the CNAME
2. Confirm lack of registration by the target
3. Prepare for claiming if unclaimed

## Instructions

### Step 1: List Distributions via CLI

**Context**: Use AWS CLI to search for distributions associated with the target CNAME.

**Command** ([[commands/aws-cloudfront-list-distributions]]):
```bash
aws cloudfront list-distributions --query 'DistributionList.Items[?contains(Aliases.Items, `cdn.grab.com`)].Id' --output text
```

> If no output, the distribution is unclaimed. This queries globally; success shows empty or unrelated IDs.

### Step 2: Manual Console Check

**Context**: Log into AWS console and search for the distribution ID to verify ownership.

**Command** ([[commands/aws-cloudfront-list-distributions]]):
```bash
aws cloudfront list-distributions --query 'DistributionList.Items[].DomainName'
```

> Cross-reference with CNAME; if not matching target's account, it's available. Console search for ID confirms.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used

- [[commands/aws-cloudfront-list-distributions]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- [[aws]]
- [[cloudfront]]
- [[verification]]
