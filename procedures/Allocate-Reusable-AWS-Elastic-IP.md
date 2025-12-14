---
id: proc-uuid-002
name: Allocate-Reusable-AWS-Elastic-IP
tags:
  - aws
  - elastic-ip
  - allocation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/aws-allocate-address]]'
  - '[[commands/aws-associate-address]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:10.929Z'
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
# Allocate-Reusable-AWS-Elastic-IP

## Summary

This procedure allocates a dangling AWS Elastic IP identified from a subdomain's DNS record, allowing control over the subdomain's resolution for takeover.

## Description

AWS Elastic IPs are reusable from a shared pool. If a subdomain like mta1a1.spmail.uber.com points to a released IP without proper disassociation, an attacker with an AWS account can allocate it. This leads to traffic redirection to the attacker's resources, enabling DNS zone takeover and access to subdomain-specific features like cookies and CORS.

## Requirements

1. AWS account with EC2 permissions (AllocateAddress, AssociateAddress)
2. AWS CLI installed and configured with access keys
3. Identified dangling IP from prior DNS resolution
4. An EC2 instance to associate the IP with

## Defense

Defensive measures and detection strategies:

- Disassociate and release Elastic IPs immediately after decommissioning
- Blacklist unused IPs in AWS or use customer-specific pools
- Monitor AWS API calls for unexpected allocations via CloudTrail

## Objectives

1. Claim the dangling IP from AWS pool
2. Associate it with attacker-controlled instance
3. Redirect subdomain traffic

## Instructions

### Step 1: Request IP Allocation

**Context**: Use AWS CLI to allocate the specific dangling IP.

**Command** ([[commands/aws-allocate-address]]):
```bash
aws ec2 allocate-address --domain vpc --address 52.XX.XX.XX
```

> Outputs allocation ID if successful; errors if IP is in use.

### Step 2: Associate with Instance

**Context**: Link the allocated IP to an EC2 instance for hosting content.

**Command** ([[commands/aws-associate-address]]):
```bash
aws ec2 associate-address --instance-id i-1234567890abcdef0 --allocation-id eipalloc-12345678 --allow-reassociation
```

> Confirms association; subdomain now resolves to the instance.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/aws-allocate-address]]
- [[commands/aws-associate-address]]

## Tools Used


## Tags

- [[aws]]
- [[elastic-ip]]
