---
tags:
  - subdomain-takeover
  - fastly
  - dns
type: procedure
tools:
  - '[[tools/Fastly]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - CDN
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:38:49.733Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: a56e8293-7d7b-446b-9d06-d385632593a6
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Perform Subdomain Takeover with Fastly

## Summary

This procedure claims a dangling DNS record for a subdomain like fastly.sc-cdn.net by creating a new Fastly service instance, granting control over the domain.

## Description

Exploiting the misconfiguration where a DNS CNAME persists after service cancellation, an attacker creates a matching Fastly service to hijack traffic. This allows routing to attacker-controlled backends. In the Snapchat case, it enables serving content via the CDN to clients.

## Requirements

1. Fastly account with service creation permissions.
2. The exact dangling CNAME (e.g., fastly.sc-cdn.net).
3. DNS propagation time allowance (up to 48 hours).

## Defense

Defensive measures and detection strategies:

- Automate DNS record cleanup on service deletion.
- Monitor for unauthorized Fastly services claiming records.
- Implement DNSSEC for integrity checks.

## Objectives

1. Gain control of the subdomain DNS resolution.
2. Route traffic to attacker infrastructure.
3. Prepare for content serving.

## Instructions

### Step 1: Create Fastly Service

**Context**: Log into Fastly and initiate a new service.

No command; use Fastly dashboard to create service.

> Configure the service to use the dangling global.fastly.net CNAME for fastly.sc-cdn.net.

### Step 2: Verify Claim

**Context**: Test DNS resolution post-creation.

**Command** (DNS Check):
```bash
dig fastly.sc-cdn.net
```

> Expected output: Resolution now points to the new Fastly instance.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None specific

## Tools Used

- [[tools/Fastly]]

## Tags

- [[subdomain-takeover]]
- [[tools/Fastly]]
- [[DNS]]
