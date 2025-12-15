---
id: proc-create-cloudfront-ubnt
tags:
  - aws
  - cloudfront
  - takeover
type: procedure
tools:
  - '[[tools/AWS-Cloudfront]]'
  - '[[tools/certbot]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1133.003]]'
updated_at: '2025-12-14T17:31:43.064Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1133.003]]'
---
# Create-AWS-Cloudfront-Distribution-for-Takeover

## Summary

Create a new AWS Cloudfront distribution and register the dangling hostname to redirect traffic to an attacker-controlled origin.

## Description

Using the AWS console, set up a distribution with the target subdomain as a CNAME alias, linking to a server hosting malicious content. Obtain SSL via Let's Encrypt if needed for HTTPS takeover.

## Requirements

1. AWS account with Cloudfront permissions
2. Attacker-controlled origin server (e.g., EC2 or VPS)
3. Domain ownership proof for SSL (via certbot)

## Defense

Defensive measures and detection strategies:

- Enable AWS GuardDuty for anomalous distribution creations
- Audit CNAMEs and remove dangling records promptly

## Objectives

1. Claim the unclaimed Cloudfront hostname
2. Route subdomain traffic to attacker origin
3. Enable HTTPS control

## Instructions

### Step 1: Configure Distribution

**Context**: In AWS Cloudfront console, create distribution and add CNAME.

No CLI command; use web UI: Select origin domain (attacker server IP/domain), add 'ping.ubnt.com' under Alternate Domain Names (CNAMEs), deploy.

### Step 2: SSL Setup

**Context**: Verify domain for certificate.

Use [[tools/certbot]]:
```bash
certbot certonly --webroot -w /var/www/html -d ping.ubnt.com
```

> Uploads verification file; expected: Certificate issued.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1133.003]] External Remote Services: Cloud Services

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/AWS-Cloudfront]]
- [[tools/certbot]]

## Tags

- aws
- cloudfront
