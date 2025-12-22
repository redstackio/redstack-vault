---
tags:
  - subdomain-takeover
  - dns-hijacking
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/dig-lookup]]'
platforms:
  - Web
  - DNS
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: e41d52a7-b888-4566-853b-ac46e113e29c
created_at: '2025-12-14T04:38:39.337Z'
updated_at: '2025-12-14T04:38:39.337Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim External Service for Takeover

## Summary

This procedure details registering an external service (e.g., GitHub Pages) linked to a dangling DNS CNAME record, allowing the attacker to hijack resolution of the target subdomain like vulnerable-sub.mozaws.net.

## Description

Once a dangling record is identified, the attacker claims the corresponding external resource, which was previously used but abandoned by the target. This redirects all traffic for the subdomain to the attacker's control without altering the target's DNS. Prerequisites include a free account on the provider. Outcome: Full control over the subdomain's content serving.

## Requirements

1. Identified dangling CNAME from prior enumeration
2. Account on the external provider (e.g., GitHub)
3. Ability to verify DNS propagation

## Defense

Defensive measures and detection strategies:

- Monitor external service usage tied to DNS records and revoke access for unused ones
- Use certificate transparency logs to detect unauthorized subdomains
- Implement short TTLs on DNS records and regular sweeps for orphans

## Objectives

1. Secure control of the external service matching the dangling record
2. Redirect subdomain traffic to attacker infrastructure
3. Validate takeover without target awareness

## Instructions

### Step 1: Register the Service

**Context**: Manually create the exact resource name on the provider to match the dangling CNAME.

**Command** (No specific command; manual process):

> Log into the provider (e.g., github.com), create a new repository or user named exactly as in the CNAME (e.g., "mozaws-vulnerable"). Enable Pages if applicable. Expected output: Confirmation page for the new resource.

### Step 2: Verify DNS Resolution

**Context**: Confirm the subdomain now points to your claimed service.

**Command** ([[commands/dig-lookup]]):
```bash
dig vulnerable-sub.mozaws.net CNAME +short
```

> This checks if the CNAME resolves to your service endpoint. Expected output: Your GitHub Pages URL or similar.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/dig-lookup]]

## Tools Used


## Tags

- [[subdomain-takeover]]
- [[dns-hijacking]]
