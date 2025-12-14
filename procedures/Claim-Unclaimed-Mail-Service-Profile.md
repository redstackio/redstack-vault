---
id: proc-claim-mail-profile
name: Claim-Unclaimed-Mail-Service-Profile
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.656Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
tags:
  - takeover
  - initial-access
platforms:
  - Web
tools: []
commands: []
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

# Claim-Unclaimed-Mail-Service-Profile

## Summary

This procedure registers and claims ownership of an unclaimed mail service profile on a third-party platform like icn.bg, linked to the dangling DNS record for mail.starbucks.bg, granting control over the subdomain.

## Description

Subdomain takeover involves registering the unclaimed profile on the provider's self-service portal. For icn.bg, create a new account or profile associating the subdomain with your credentials. This exploits the dangling record, as DNS still points to the service. Targets email providers where verification is DNS-based.

## Requirements

1. Access to the provider's web registration portal
2. Valid email or account for registration
3. The subdomain must resolve to the provider

## Defense

Defensive measures and detection strategies:

- Remove dangling DNS records promptly
- Monitor third-party provider logs for new claims on your domains
- Implement domain shadowing or parking for unused subdomains

## Objectives

1. Secure ownership of the service profile
2. Enable further configuration for exploitation
3. Establish initial control over subdomain resources

## Instructions

### Step 1: Register on Provider Platform

**Context**: Create an account on icn.bg if needed, then initiate subdomain registration.

Browse to registration form and submit mail.starbucks.bg.

> Expected output: Confirmation email or dashboard access.

### Step 2: Associate DNS Record

**Context**: Link the profile to the existing DNS pointer.

No command; complete in panel.

> Expected output: Profile active, DNS propagation in progress.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[takeover]]
- [[initial-access]]
