---
id: proc-verify-dyn-availability
tags:
  - dns
  - dyn
  - availability-check
type: procedure
tools:
  - '[[tools/Detectify-Labs-Blog]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T05:32:23.424Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Verify Subdomain Availability on DYN

## Summary

This procedure checks if a dangling subdomain is available for claiming on DYN's platform, confirming the takeover vulnerability.

## Description

Attackers visit DYN's DNS portal to search for the hostname. If unclaimed, it appears available for registration, allowing addition to a cart. This step validates the misconfiguration in a controlled manner, often with screenshots for proof. Target environment is DYN's web interface; expected outcome is confirmation of availability without purchase.

## Requirements

1. Web browser access to http://dyn.com/dns/
2. Target subdomain details from prior DNS checks
3. Account on DYN (optional for initial search)

## Defense

Defensive measures and detection strategies:

- Automate hostname claims immediately after DNS delegation
- Monitor third-party platforms for dangling assets
- Use certificate transparency logs to detect unauthorized takeovers

## Objectives

1. Search and confirm availability
2. Simulate claim without activation
3. Gather evidence of vulnerability

## Instructions

### Step 1: Access DYN Portal and Search

**Context**: Navigate to the DNS management section and input the subdomain.

No command-line command; use browser to visit http://dyn.com/dns/ and search for "web.mopub.com".

> Expected: Search results show the hostname as available.

### Step 2: Attempt Cart Addition

**Context**: Test registration by adding to cart.

In the browser, select and add the subdomain to the shopping cart.

> Expected output: Confirmation message like "DNS services are active but can be purchased." Remove from cart post-test.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Detectify-Labs-Blog]]

## Tags

- [[DNS]]
- [[dyn]]
- [[availability-check]]
