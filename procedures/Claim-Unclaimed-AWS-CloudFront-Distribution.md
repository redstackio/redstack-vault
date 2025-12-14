---
id: proc-claim-aws-cloudfront
tags:
  - subdomain-takeover
  - aws
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
  - '[[T1078.004]]'
updated_at: '2025-12-14T04:39:01.856Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1078.004]]'
---
# Claim Unclaimed AWS CloudFront Distribution

## Summary

This procedure claims control of a subdomain by creating an AWS CloudFront distribution and assigning the dangling hostname, allowing the attacker to serve arbitrary content on the legitimate-looking subdomain.

## Description

Following DNS discovery, the attacker logs into AWS, creates a distribution linked to a controlled origin, and adds saostatic.uber.com as an alternate domain name. This hijacks traffic to the subdomain, enabling phishing or further attacks. Propagation takes minutes, after which custom pages like subdomaintakeoverbyarneswinnen.html are accessible.

## Requirements

1. Valid AWS account with CloudFront permissions
2. Controlled origin server (e.g., S3 bucket)
3. Identified dangling CNAME from prior recon

## Defense

Defensive measures and detection strategies:

- Monitor AWS for unauthorized distribution creations using CloudTrail
- Delete unused DNS records and claim all cloud resources
- Enable MFA and least-privilege IAM policies for AWS consoles

## Objectives

1. Gain control over the subdomain
2. Serve malicious content with subdomain authority
3. Prepare for downstream exploits like phishing

## Instructions

### Step 1: Create CloudFront Distribution

**Context**: Set up a new distribution in the AWS console to host attacker content.

**Instructions**: Navigate to CloudFront dashboard, create distribution, select custom origin (attacker server), configure behaviors for HTTP/HTTPS, and enable.

> No CLI command; web console action. Expected: Distribution ID generated.

### Step 2: Assign Alternate Domain Name

**Context**: Link the distribution to the target subdomain to claim it.

**Instructions**: In distribution settings, add saostatic.uber.com under Alternate Domain Names (CNAMEs). Update if needed and deploy.

> Success: Subdomain resolves to attacker content after propagation (test with curl or browser).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1078.004]] Valid Accounts: Cloud Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/AWS-CloudFront-Console]]

## Tags

- subdomain-takeover
- aws
