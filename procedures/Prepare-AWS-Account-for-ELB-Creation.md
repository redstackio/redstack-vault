---
id: proc-uuid-1
tags:
  - aws
  - account-setup
  - domain-takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1583.001]]'
updated_at: '2025-12-14T05:32:24.135Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1583.001]]'
---
# Prepare-AWS-Account-for-ELB-Creation

## Summary

This procedure sets up an AWS account and configures the us-west-2 region to prepare for recreating a dangling ELB resource, enabling subdomain takeover via a misconfigured CNAME record.

## Description

In a domain takeover attack, the first step is ensuring access to the AWS environment where the deleted ELB was hosted. By logging into AWS and selecting the correct region (us-west-2), an attacker positions themselves to create resources that match the dangling DNS reference, such as a0e7eaaaa82f611e9b1cc0e9ccd15f3e-557536140.us-west-2.elb.amazonaws.com. This is a low-risk setup step assuming the attacker has or creates a standard AWS account.

## Requirements

1. Internet access to AWS Management Console
2. AWS credentials (email and password for signup if needed)
3. Basic familiarity with AWS regions

## Defense

Defensive measures and detection strategies:

- Monitor for unusual ELB creations in us-west-2 via AWS CloudTrail logs
- Implement DNS monitoring tools to alert on NXDomain responses for subdomains

## Objectives

1. Gain authenticated access to AWS console
2. Configure environment for ELB operations
3. Verify regional targeting for the dangling resource

## Instructions

### Step 1: Log In or Register AWS Account

**Context**: Authenticate to AWS to access resource creation features.

Access the AWS Management Console at https://console.aws.amazon.com and log in with existing credentials or register a new account using a valid email.

> Upon successful login, the default region dashboard appears.

### Step 2: Set Region to us-west-2

**Context**: Ensure operations target the region of the deleted ELB to match the dangling CNAME.

In the top-right corner of the console, click the region selector and choose 'US West (Oregon) - us-west-2'.

> The console refreshes to show services in us-west-2; confirm by checking the region indicator.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1583.001]] Domains

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- aws-setup
- region-config
