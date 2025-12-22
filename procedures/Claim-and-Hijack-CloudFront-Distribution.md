---
tags:
  - subdomain-takeover
  - cloudfront
  - hijacking
  - phishing
type: procedure
tools:
  - '[[tools/aws-cli]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Cloud
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:31.358Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 2fd90dd2-a778-4fe4-a973-156f5099dc15
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim-and-Hijack-CloudFront-Distribution

## Summary

This procedure claims an unowned AWS CloudFront distribution identified via dangling CNAME and reconfigures it to serve attacker-controlled content, hijacking the subdomain for phishing or data exfiltration.

## Description

Once a dangling CNAME is detected, attackers with an AWS account can claim the distribution by associating it with their account. CloudFront allows this because it doesn't validate DNS ownership. The hijacked subdomain can then serve malicious HTML/JS to steal cookies (including httpOnly and secure ones via SSL) or impersonate the legitimate service. SSL certificates from free CAs like Let's Encrypt enable trusted HTTPS connections.

## Requirements

1. AWS account with CloudFront access
2. Identified distribution ID from reconnaissance
3. Attacker-controlled origin (e.g., S3 bucket or web server)
4. Domain validation for SSL (via DNS or HTTP challenge)

## Defense

Defensive measures and detection strategies:

- Remove unused DNS CNAMEs immediately after decommissioning resources
- Monitor CloudFront distributions for unauthorized claims via AWS GuardDuty
- Implement certificate transparency monitoring for subdomains
- Use DNSSEC to prevent unauthorized resolutions

## Objectives

1. Gain control over the trusted subdomain
2. Serve arbitrary content for phishing or malware distribution
3. Exfiltrate user data via cookie theft under HTTPS

## Instructions

### Step 1: Claim the Distribution in AWS Console

**Context**: Log into AWS and associate the unclaimed distribution with your account.

**Instructions**: Navigate to CloudFront dashboard, search for distribution ID (e.g., du6drkqe7qw4g), select it, and update to add a custom origin pointing to your malicious server.

### Step 2: Configure Malicious Origin and SSL

**Context**: Update the distribution config to route traffic to attacker content and enable HTTPS.

**Command** (AWS CLI for update):
```bash
aws cloudfront update-distribution --id E123ABC --if-match E2ETAG123 --distribution-config file://updated-config.json
```

> The config.json file specifies a new origin domain (e.g., attacker-s3-bucket.s3.amazonaws.com) and enables HTTPS with custom SSL cert. Expected output: Success message with updated ETag. Wait for propagation (~5-15 min).

### Step 3: Validate Hijack

**Context**: Test resolution and content serving.

**Instructions**: Query DNS again and access https://cloudfront.ubnt.com to confirm it loads malicious content over HTTPS.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/aws-cli]]

## Tags

- subdomain-takeover
- cloudfront
- hijacking
- phishing
