---
id: p3c4d5e6-f7g8-9012-cdef-3456789012
tags:
  - domain-registration
  - takeover
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Cloud
  - Azure
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:26.524Z'
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
# Claim Unclaimed Domain for Takeover

## Summary

This procedure registers an unclaimed domain identified from a dangling CNAME to gain control over the associated subdomain.

## Description

For the Azure endpoint ████, register it via a public registrar to redirect or host content on the DoD subdomain. This grants full control for potential phishing or XSS.

## Requirements

1. Valid payment method for registration
2. Account on a domain registrar
3. Verified availability from prior step

## Defense

Defensive measures and detection strategies:

- Lock down cloud resource deletion to avoid dangling records
- Use Azure Sentinel for domain monitoring
- Implement CAA records to restrict subdomain issuance

## Objectives

1. Secure domain ownership
2. Demonstrate subdomain control
3. Prevent adversarial takeover

## Instructions

### Step 1: Initiate Registration

**Context**: Search and purchase the domain on a registrar.

No command; web-based:
- Go to registrar site (e.g., GoDaddy.com)
- Search for ████
- Add to cart, provide details, and complete purchase

### Step 2: Verify Ownership

**Context**: Confirm registration and DNS control.

Use [[commands/dig-dns-query]] post-registration:

```bash
dig +short NS ████
```

> Output shows your nameservers.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[domain-registration]]
- [[takeover]]
