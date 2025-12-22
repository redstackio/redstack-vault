---
id: proc-uuid-3
tags:
  - account-claim
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:26.696Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim-Expired-Desk-com-Subdomain

## Summary

Register a new account on Desk.com using an expired subdomain identifier to hijack control of the associated DNS CNAME.

## Description

When a service like Desk.com account expires but DNS CNAME remains, attackers can recreate the account with the same identifier (e.g., cloudup.desk.com), gaining control over traffic routed there.

## Requirements

1. Access to desk.com registration
2. Knowledge of the expired identifier from CNAME
3. No existing claim on the identifier

## Defense

Defensive measures and detection strategies:

- Remove DNS records immediately upon service cancellation
- Monitor for unauthorized account creations on sub-identifiers
- Use reserved namespaces in third-party services

## Objectives

1. Secure the expired identifier
2. Gain dashboard access
3. Enable content configuration

## Instructions

### Step 1: Initiate Registration

**Context**: Go to desk.com and start a new account setup.

Enter cloudup as the subdomain identifier during signup.

### Step 2: Complete Setup

**Context**: Provide necessary details to finalize registration.

Success indicates the original account was expired, allowing claim.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-claim]]
- [[subdomain-takeover]]
