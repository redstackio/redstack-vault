---
tags:
  - subdomain-takeover
  - poc
  - cloud-exploit
type: procedure
tools:
  - '[[tools/Subjack]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/dig-lookup]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:38:49.507Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e2bd40c0-0aae-462a-bec4-8dde83cc6b34
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Perform Non-Destructive Subdomain Takeover POC

## Summary

This procedure demonstrates claiming an unclaimed cloud instance for a vulnerable subdomain and serving custom content to prove control, as in the Starbucks unclaimed instances case, without disrupting legitimate services.

## Description

Exploiting weak process flows in cloud providers allows claiming unused subdomain space (e.g., psv.openapi.starbucks.com). The attacker registers the dangling record on the provider, uploads benign content, and verifies access. This targets web environments with misconfigured DNS; expected outcome is domain hijacking for phishing potential.

## Requirements

1. Identified vulnerable subdomain from prior enumeration
2. Account on the target cloud provider (e.g., AWS)
3. Basic web server setup for POC content

## Defense

Defensive measures and detection strategies:

- Monitor for unexpected DNS changes via tools like DNSSec
- Implement strict subdomain registration policies
- Regularly claim and secure unused instances

## Objectives

1. Claim the unclaimed instance
2. Serve and verify custom content
3. Confirm no operational disruption

## Instructions

### Step 1: Verify DNS Resolution

**Context**: Confirm the subdomain points to an unclaimed service before claiming.

**Command** ([[commands/dig-lookup]]):
```bash
dig +short germany.openapi.starbucks.com
```

> This queries DNS for the subdomain's IP or CNAME. Expected output: A record pointing to an unused cloud endpoint like s3.amazonaws.com bucketname.

### Step 2: Claim Instance and Serve Content

**Context**: Register the unclaimed resource on the provider and upload a test page.

**Instructions**: Log into the cloud console (e.g., AWS), create the missing resource (bucket/app), update DNS if needed, and upload an index.html with custom content. Access via browser to verify.

> No direct command; use provider CLI like `aws s3 mb s3://bucketname` if applicable. Expected output: Custom page loads at the subdomain URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/dig-lookup]]

## Tools Used

- [[tools/Subjack]]

## Tags

- [[subdomain-takeover]]
- [[proof-of-concept]]
