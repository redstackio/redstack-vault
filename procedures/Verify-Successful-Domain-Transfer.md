---
id: g7h8i9j0-k1l2-3456-ghij-789012345678
tags:
  - verification
  - domain-hijack
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:42.858Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Successful-Domain-Transfer

## Summary

Confirm the domain has transferred to the victim's store, copying all DNS records, email forwarders, and subdomains for escalation.

## Description

Post-CSRF, the victim's Shopify admin will show the attacker's domain with intact configurations, allowing further attacks like phishing via email or DNS redirection to steal store/payment data.

## Requirements

1. Access to victim's store (post-transfer)
2. Original domain details for comparison
3. Test HTML for self-verification

## Defense

Defensive measures and detection strategies:

- Alerts for unauthorized domain additions
- Review transfer history regularly
- DNS change notifications

## Objectives

1. Check domain in victim admin
2. Validate copied configurations
3. Test for escalation potential

## Instructions

### Step 1: Inspect Victim Admin

**Context**: Log into victim's store to view domains.

Navigate to Settings > Domains; look for new domain with MX, A, NS records, forwarders, subdomains.

> Expected: Attacker's domain listed with configurations.

### Step 2: Test Redirect

**Context**: Use modified HTML on own store to confirm functionality.

Edit HTML to target own store, open, and observe redirect (e.g., h1-5142.com to your store).

> Expected: Successful transfer simulation.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[verification]]
- [[dns-hijack]]
