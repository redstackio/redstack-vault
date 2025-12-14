---
tags:
  - subdomain-takeover
  - zendesk
  - claim
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:10.456Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 9a440a3d-85e1-4802-a542-3dd5fd12a7c5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim-Abandoned-Third-Party-Subdomain

## Summary

This procedure details registering and claiming control of an unused subdomain on a third-party platform like Zendesk, exploiting dangling DNS pointers for takeover.

## Description

When a CNAME points to an inactive service instance (e.g., scan.zendesk.com), attackers can sign up on the platform and associate the subdomain. This grants control over the resolution path. Target environment: SaaS platforms with subdomain customization. Prerequisites: Free account creation on the service. Expected outcomes: Full administrative control, enabling content hosting under the original domain.

## Requirements

1. Access to the third-party platform's signup page
2. Valid email for registration
3. No prior association with the subdomain on the service

## Defense

Defensive measures and detection strategies:

- Proactively claim and delete unused subdomains on third-party services
- Use domain monitoring services to alert on dangling records
- Implement strict DNS change controls and audits

## Objectives

1. Register an account on the third-party service
2. Configure the subdomain to point to the new instance
3. Validate control over the resolution

## Instructions

### Step 1: Register on Third-Party Platform

**Context**: Create a new account on Zendesk to access subdomain management.

**Command** (Manual):
No command; use web browser to visit zendesk.com/signup and complete registration.

> Provide email and verify. Expected: Account creation confirmation.

### Step 2: Claim the Subdomain

**Context**: In the Zendesk dashboard, add the dangling subdomain (scan.zendesk.com) to your instance.

**Command** (Manual dashboard action):
Navigate to Settings > Custom Domains and enter the subdomain.

> Zendesk will verify and assign if unused. Success: Subdomain linked to your account.

### Step 3: Verify Claim

**Context**: Test resolution to ensure the subdomain now points to your instance.

**Command** ([[commands/query-dns-cname]]):
```bash
dig scan.zendesk.com
```

> Confirm it resolves to your active instance.

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
- [[zendesk]]
