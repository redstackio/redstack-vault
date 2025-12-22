---
id: proc-002
name: Perform AWS Subdomain Takeover
tags:
  - subdomain-takeover
  - aws-exploit
  - dns-hijack
type: procedure
tools:
  - '[[tools/aws-cli]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/aws-s3-check]]'
verified: false
platforms:
  - AWS
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:31.199Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Perform AWS Subdomain Takeover

## Summary

This procedure exploits a dangling DNS record pointing to a terminated AWS EC2 instance by claiming the associated cloud resource, allowing control over the subdomain for malicious purposes like phishing.

## Description

Following discovery of a dangling record (e.g., ███████.8x8.com pointing to a defunct EC2), attackers check if the record aliases an unused AWS service like S3 or ELB. With an AWS account, they create the resource matching the DNS alias, effectively taking over the subdomain. This misconfiguration arises from incomplete cleanup after instance replacement. Expected outcomes: Attacker-hosted content on the subdomain, spoofing the parent domain.

## Requirements

1. AWS account with permissions to create EC2, S3, or ELB resources
2. Knowledge of the dangling record's target service
3. DNS propagation time consideration (up to 48 hours)

## Defense

Defensive measures and detection strategies:

- Automate DNS cleanup on resource termination using AWS Lambda
- Monitor for unauthorized resource creation via CloudTrail logs
- Implement domain lockdown with registry locks

## Objectives

1. Claim the unused AWS resource linked to the DNS record
2. Redirect or host malicious content on the subdomain
3. Achieve phishing or further compromise

## Instructions

### Step 1: Verify Resource Availability

**Context**: Confirm the dangling record points to a claimable AWS resource.

**Command** ([[commands/aws-s3-check]]):
```bash
aws s3api head-bucket --bucket dangling-bucket-name 2>/dev/null || echo "Bucket available"
```

> Attempts to access the bucket; failure indicates availability for creation. Expected output: Error if exists, or success message for takeover.

### Step 2: Create and Claim Resource

**Context**: Register the resource and update to match the DNS record.

**Command** ([[commands/aws-ec2-create]]):
```bash
aws ec2 run-instances --image-id ami-0abcdef1234567890 --count 1 --instance-type t2.micro --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=DanglingEC2}]'
```

> Launches a new EC2 instance or equivalent service. Then, configure DNS or wait for propagation. Expected output: Instance ID confirming creation, verifiable via ping to subdomain.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/aws-s3-check]]
- [[commands/aws-ec2-create]]

## Tools Used

- [[tools/aws-cli]]

## Tags

- [[subdomain-takeover]]
- [[aws-exploit]]
