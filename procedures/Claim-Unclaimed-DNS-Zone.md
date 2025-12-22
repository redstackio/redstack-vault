---
id: 123e4567-e89b-12d3-a456-426614174002
name: Claim Unclaimed DNS Zone
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:49.334Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - dns
  - cloud
  - subdomain-takeover
commands:
  - '[[commands/dig-dns-query]]'
platforms:
  - Cloud
  - DNS
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Claim Unclaimed DNS Zone

## Summary

This procedure registers an unclaimed DNS zone identified from dangling NS records, granting the attacker control over the associated subdomain for further exploitation.

## Description

Following discovery of dangling NS records pointing to an unclaimed zone (e.g., in AWS Route 53), the attacker creates a new hosted zone in their account. This exploits the misconfiguration where the victim's subdomain delegates authority to the unclaimed zone. Once claimed, the attacker can configure arbitrary DNS records, leading to subdomain takeover. The target environment is cloud DNS services; expected outcomes include full resolution control, enabling phishing or content hosting.

## Requirements

1. Attacker account on the cloud DNS provider (e.g., AWS with billing enabled)
2. Identified unclaimed zone name from prior reconnaissance
3. Basic understanding of DNS zone creation

## Defense

Defensive measures and detection strategies:

- Delete or reconfigure dangling zones promptly after decommissioning
- Use cloud provider alerts for new zone creations matching known subdomains
- Implement domain shadowing prevention through regular NS audits

## Objectives

1. Secure control of the DNS zone
2. Redirect subdomain traffic to attacker infrastructure
3. Enable subsequent malicious actions

## Instructions

### Step 1: Create Hosted Zone

**Context**: Use the cloud provider's console to register the zone, which updates the authoritative nameservers.

**Command** (UI action; verify with CLI):

> In AWS Route 53 console, create a new public hosted zone for the domain (e.g., nagli.us-east4.37signals.com). Note the new NS records provided.

### Step 2: Verify Claim

**Context**: Confirm the victim's subdomain now resolves to the new zone.

**Command** ([[commands/dig-dns-query]]):
```bash
dig NS us-east4.37signals.com
```

> Expected output shows the attacker's NS records. If matched, the claim is successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/dig-dns-query]]

## Tools Used

- None specific

## Tags

- [[DNS]]
- [[cloud]]
- [[subdomain-takeover]]
