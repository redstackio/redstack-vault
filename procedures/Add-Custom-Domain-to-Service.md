---
id: proc-uuid-3
tags:
  - subdomain-takeover
  - dns
  - domain-claim
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:23.544Z'
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
# Add-Custom-Domain-to-Service

## Summary

This procedure claims the vulnerable subdomain by adding it as a custom domain to the registered cloud service, hijacking DNS resolution due to the dangling CNAME.

## Description

With the Custom Domains interface open, the attacker inputs the exact subdomain (e.g., vulnerable.dod.gov) to associate it with their service. The platform handles DNS verification, and since the CNAME points to the unclaimed service (now claimed), resolution shifts to the attacker. This step is critical for takeover and can lead to immediate control, with impacts like serving malicious content to DoD users.

## Requirements

1. Access to Custom Domains settings from prior procedure
2. Exact subdomain name from DNS reconnaissance
3. Understanding of DNS propagation times (typically minutes)

## Defense

Defensive measures and detection strategies:

- Implement short TTLs on DNS records and monitor for anomalies
- Use subdomain takeover detection tools like dnstake or subjack in CI/CD
- Block unverified custom domains on cloud platforms

## Objectives

1. Bind the subdomain to the attacker's service
2. Hijack traffic from the original domain
3. Establish control for content serving

## Instructions

### Step 1: Enter Subdomain

**Context**: Provide the vulnerable domain for claiming.

In the Custom Domains field, type the full subdomain (e.g., affected-subdomain.dod.gov) and click 'Add' or 'Verify'.

### Step 2: Confirm and Wait for Propagation

**Context**: Allow the platform to validate and update DNS.

Submit the addition; the platform will check the CNAME match. Wait 5-10 minutes for DNS propagation, then test resolution.

> Expected output: Confirmation message and updated domain status as 'active'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[DNS]]
