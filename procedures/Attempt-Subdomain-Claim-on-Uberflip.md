---
tags:
  - subdomain-takeover
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:38:49.527Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 39bfebcc-433e-485d-beb5-6792e84e8354
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Attempt-Subdomain-Claim-on-Uberflip

## Summary

This procedure attempts to sign up for Uberflip and claim an unowned subdomain by adding it as a custom domain during hub setup, gaining control over the DNS-pointed resource.

## Description

After verifying a dangling CNAME, attackers create an Uberflip account and input the target subdomain during configuration. If unclaimed, it activates under attacker control. This targets content management services with open registration, in web environments. Potential issues like signup restrictions may block, but success enables full subdomain hijack. Outcome: Ownership transfer for content hosting.

## Requirements

1. Valid email for Uberflip signup
2. Access to Uberflip website
3. Target subdomain details

## Defense

Defensive measures and detection strategies:

- Claim subdomains immediately in third-party services
- Use domain validation during signup (e.g., TXT records)
- Monitor service logs for unauthorized claims

## Objectives

1. Register an Uberflip account
2. Successfully add and activate the target subdomain
3. Verify control via content updates

## Instructions

### Step 1: Sign Up for Uberflip

**Context**: Create a new account to access hub creation features.

Navigate to uberflip.com/signup and complete registration with email and details. No command; manual web form.

### Step 2: Create Hub and Add Custom Domain

**Context**: During hub setup, enter the target subdomain as custom domain.

In the dashboard, select custom domain option and input 'resources.hackerone.com'. If unclaimed, it verifies DNS and activates. Expected: Confirmation message without ownership errors.

### Step 3: Test Activation

**Context**: Verify claim by accessing the subdomain post-setup.

Use browser to visit https://resources.hackerone.com/; should now serve Uberflip hub placeholder.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[subdomain-takeover]]
- [[claim]]
