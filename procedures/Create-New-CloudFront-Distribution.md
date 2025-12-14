---
id: proc-cloudfront-create-001
tags:
  - aws-cloudfront
  - subdomain-takeover
  - initial-access
type: procedure
tools:
  - '[[tools/AWS-CloudFront-Console]]'
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
updated_at: '2025-12-14T04:38:39.694Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create New CloudFront Distribution

## Summary

This procedure creates a new AWS CloudFront distribution configured with a custom origin and adds a dangling subdomain as an alternate domain name, exploiting the lack of ownership validation to claim the domain.

## Description

AWS CloudFront allows adding custom CNAMEs without verifying domain control, enabling attackers to hijack dangling records. This targets AWS environments with public DNS misconfigurations, resulting in traffic redirection to attacker-controlled content for phishing.

## Requirements

1. AWS account with CloudFront create permissions
2. Identified dangling subdomain from prior recon
3. S3 bucket or custom origin for hosting content

## Defense

Defensive measures and detection strategies:

- Remove unused DNS records promptly after decommissioning
- Use AWS Config rules to monitor for unexpected CNAME additions
- Enable CloudFront access logs to detect anomalous traffic

## Objectives

1. Establish a claimable distribution
2. Add target subdomain as CNAME
3. Prepare for traffic routing

## Instructions

### Step 1: Access CloudFront Console

**Context**: Log in to AWS and navigate to CloudFront to initiate distribution creation.

Open [[tools/AWS-CloudFront-Console]] and click 'Create Distribution'.

### Step 2: Configure Origin and CNAME

**Context**: Set up the distribution with an origin and add the subdomain.

Select 'Web' delivery, enter S3 bucket as origin domain, then in 'Alternate Domain Names (CNAMEs)', add 'partners.ubnt.com'.

> No command; console-based. Save and deploy.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/AWS-CloudFront-Console]]

## Tags

- [[aws-cloudfront]]
- [[subdomain-takeover]]
