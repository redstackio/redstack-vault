---
id: 123e4567-e89b-12d3-a456-426614174002
name: Claim-Unclaimed-AWS-CloudFront-Distribution
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.887Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - subdomain-takeover
  - aws-cloudfront
commands: []
platforms:
  - AWS
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Claim-Unclaimed-AWS-CloudFront-Distribution

## Summary

This procedure involves creating an AWS CloudFront distribution and associating it with a dangling subdomain's CNAME to gain control over the legitimate domain, allowing hosting of arbitrary content as if it were official.

## Description

Following discovery of an unclaimed CloudFront hostname via DNS lookup, the attacker logs into AWS, creates a new distribution pointing to a controlled origin (e.g., an EC2 instance or S3 bucket), and adds the target subdomain (saostatic.uber.com) as an alternate domain name. Once propagated, the subdomain resolves to the attacker's content. This targets cloud-reliant web apps; prerequisites include an AWS account. Outcomes: Full subdomain control for phishing or malware distribution.

## Requirements

1. Valid AWS account with CloudFront permissions
2. Identified unclaimed CloudFront CNAME from recon
3. Controlled origin server ready

## Defense

Defensive measures and detection strategies:

- Monitor AWS for unauthorized distribution creations linked to owned domains
- Use AWS Config rules to alert on new CloudFront associations
- Regularly scan for dangling DNS records with tools like dnsrecon

## Objectives

1. Associate attacker-controlled distribution with victim subdomain
2. Achieve resolution hijacking
3. Enable content serving on legitimate domain

## Instructions

### Step 1: Create New CloudFront Distribution

**Context**: Set up the distribution in AWS Console or CLI to prepare for CNAME association.

**Command** (AWS CLI example):
```bash
aws cloudfront create-distribution --distribution-config file://config.json
```

> The config.json specifies origin domain (e.g., attacker-server.com), default cache behavior, and enables HTTPS. Expected: Distribution ID returned, status 'InProgress'.

### Step 2: Add Alternate Domain Name

**Context**: Link the victim subdomain to the distribution.

**Command** (AWS Console):
```bash
# In Console: Edit Distribution > Alternate Domain Names > Add saostatic.uber.com
```

> Validate domain ownership if required (not always for unclaimed). Wait for deployment (5-15 min). Test by curling the subdomain.

### Step 3: Verify Control

**Context**: Confirm takeover by accessing the subdomain.

**Command** (Test):
```bash
curl -I https://saostatic.uber.com
```

> Expected: 200 OK from attacker origin, not CloudFront error.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None specific

## Tools Used

- AWS CLI/Console

## Tags

- [[subdomain-takeover]]
- [[aws-cloudfront]]
