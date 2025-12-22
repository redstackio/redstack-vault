---
id: proc-claim-dangling-resource
tags:
  - cloud-misconfiguration
  - subdomain-takeover
  - aws
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - AWS
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:38:39.354Z'
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
# Claim Dangling Cloud Resource

## Summary

This procedure details registering an unused cloud resource (e.g., AWS S3 bucket) referenced by a dangling DNS CNAME to gain control over a subdomain, enabling subdomain takeover. It is used after identifying a vulnerable record to redirect traffic to attacker infrastructure.

## Description

Once a dangling CNAME is found (e.g., pointing to 'dangling-bucket.s3.amazonaws.com'), the attacker creates the exact resource name in their cloud account. DNS propagation (typically minutes) then routes the subdomain to the new resource. This exploits cleanup failures in cloud environments like AWS. Prerequisites: AWS account with permissions to create the resource type. Outcomes: Full subdomain control for hosting content.

## Requirements

1. Identified dangling CNAME target (e.g., S3 bucket name)
2. AWS credentials with create permissions for the service
3. Awareness of DNS TTL for propagation delays

## Defense

Defensive measures and detection strategies:

- Automate DNS record deletion upon cloud resource termination
- Monitor for new resource creations matching known dangling names
- Use domain shadowing prevention tools to lock unused subdomains

## Objectives

1. Register the precise cloud resource name
2. Verify subdomain resolution to the new resource
3. Establish initial access via misconfiguration

## Instructions

### Step 1: Access Cloud Provider Console

**Context**: Log into the cloud provider (AWS) and navigate to the service matching the CNAME (e.g., S3 for .s3.amazonaws.com).

No command; use web interface to create bucket named exactly as in CNAME (e.g., 'dangling-bucket').

> Expected: Success message for bucket creation. Avoid public access initially for stealth.

### Step 2: Configure Resource for Web Serving

**Context**: Enable static website hosting if needed for HTTP access.

Via AWS CLI or console: Set bucket policy for public read and enable website endpoint.

> Expected: Resource ready; test access at http://dangling-bucket.s3.amazonaws.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[cloud-misconfiguration]]
- [[subdomain-takeover]]
