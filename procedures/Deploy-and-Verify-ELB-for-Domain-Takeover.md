---
id: proc-uuid-4
tags:
  - aws
  - elb-deployment
  - verification
  - domain-takeover
type: procedure
tools:
  - '[[tools/Automated-ELB-Creation-Script]]'
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:24.107Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1583.001]]'
  - '[[Exploit Public-Facing Application]]'
---
# Deploy-and-Verify-ELB-for-Domain-Takeover

## Summary

This procedure finalizes the ELB deployment and verifies the DNS match to confirm subdomain takeover, allowing the attacker to route traffic to malicious endpoints.

## Description

Deployment generates a DNS name with a random numeric suffix; matching the exact suffix (e.g., 557536140) from the dangling record enables takeover. Automation may be needed for retries, leading to control over the subdomain for phishing.

## Requirements

1. Configured ALB form ready for creation
2. Access to DNS query tools (e.g., dig) for verification
3. Optional: Script for suffix iteration

## Defense

Defensive measures and detection strategies:

- Regularly audit and remove dangling DNS records post-resource deletion
- Monitor DNS resolution changes for subdomains using tools like DNSdiff
- Set up alerts for new ELBs with suspicious names via CloudWatch

## Objectives

1. Successfully provision the ELB
2. Confirm DNS name alignment with CNAME
3. Validate subdomain resolution to attacker's resource

## Instructions

### Step 1: Complete and Deploy ALB

**Context**: Finalize minimal configuration to provision the resource.

Configure basic settings (e.g., VPC, availability zones with defaults), then click 'Create load balancer'.

> ELB status changes to 'Active'; note the generated DNS name in the details.

### Step 2: Verify DNS Match and Subdomain Takeover

**Context**: Check if the new ELB's DNS matches the dangling suffix.

Query the subdomain (e.g., dig traefik-livedemo.rocket.chat) and compare to the ELB DNS (e.g., a0e7eaaaa82f611e9b1cc0e9ccd15f3e-557536140.us-west-2.elb.amazonaws.com). If mismatch, delete and retry with [[tools/Automated-ELB-Creation-Script]] to brute-force suffixes.

> Successful match: Subdomain resolves to attacker's ELB; configure targets to host phishing site.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1583.001]] Domains
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Automated-ELB-Creation-Script]]

## Tags

- deployment
- dns-verification
- takeover-confirmation
