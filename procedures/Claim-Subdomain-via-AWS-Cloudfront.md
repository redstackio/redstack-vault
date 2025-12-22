---
id: proc-claim-subdomain-cloudfront
tags:
  - subdomain-takeover
  - aws-cloudfront
type: procedure
tools:
  - '[[tools/AWS-Cloudfront]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - AWS
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:38:39.650Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim Subdomain via AWS Cloudfront

## Summary

This procedure claims control of a dangling subdomain by creating a Cloudfront distribution and registering the target hostname, allowing the attacker to route traffic to their server.

## Description

Exploiting the unclaimed CNAME in the Ubiquiti case, the attacker created a new Cloudfront distribution, linked it to a controlled origin, and added ping.ubnt.com as a CNAME. This grants full control over HTTPS traffic to the subdomain without altering DNS.

## Requirements

1. Valid AWS account with Cloudfront access
2. Attacker-controlled origin server (e.g., EC2 or on-prem web server)
3. Identified dangling CNAME from prior recon

## Defense

Defensive measures and detection strategies:

- Monitor Cloudfront distributions for unauthorized hostname additions via AWS CloudTrail logs
- Use subdomain monitoring tools to detect resolution changes to attacker IPs

## Objectives

1. Register the vulnerable hostname in Cloudfront
2. Route subdomain traffic to attacker origin
3. Verify control through successful content serving

## Instructions

### Step 1: Create Cloudfront Distribution

**Context**: Set up a new distribution to serve as the takeover vector.

**Instructions**: In AWS Console, navigate to Cloudfront > Create Distribution. Select your origin domain (attacker server), enable HTTPS, and proceed.

### Step 2: Add Alternate Domain Name

**Context**: Claim the subdomain by designating it as a CNAME in the distribution settings.

**Instructions**: Under 'Alternate Domain Names (CNAMEs)', enter 'ping.ubnt.com'. Update the distribution and wait for deployment (5-10 minutes). Use [[tools/nslookup]] to verify resolution.

### Step 3: Test Claim

**Context**: Confirm the subdomain now points to your content.

**Instructions**: Access https://ping.ubnt.com in a browser; it should serve your origin's default page instead of an error.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/AWS-Cloudfront]]

## Tags

- [[subdomain-takeover]]
- [[tools/AWS-Cloudfront]]
