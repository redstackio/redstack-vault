---
id: proc-verify-unclaimed-service
name: Verify-Unclaimed-Third-Party-Service
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.658Z'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Hardware]]'
tags:
  - verification
  - third-party-service
platforms:
  - Web
  - DNS
tools: []
commands: []
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---

# Verify-Unclaimed-Third-Party-Service

## Summary

This procedure confirms that a third-party service, such as icn.bg's mail hosting, has not claimed or actively hosts the target subdomain, ensuring it's available for takeover.

## Description

After identifying a dangling record, verify the service provider's status for the subdomain. For icn.bg, check their web panel or API for domain registration status. If unclaimed, the subdomain can be registered. This step prevents false positives in takeover attempts and targets SaaS providers with self-service portals.

## Requirements

1. URL or access to the third-party service's control panel
2. Basic web browsing or API querying capabilities
3. Knowledge of the provider's claiming process

## Defense

Defensive measures and detection strategies:

- Providers should notify owners of dangling domains via email
- Organizations: Scan for own subdomains on third-party platforms
- Use domain monitoring services to alert on potential hijacks

## Objectives

1. Confirm lack of active ownership
2. Validate takeover feasibility
3. Document service details for claiming

## Instructions

### Step 1: Access Service Status Page

**Context**: Navigate to the third-party provider's domain management or mail service portal.

Browse to: https://icn.bg (or equivalent panel).

> Search for the subdomain. Expected output: No active profile found.

### Step 2: Attempt Domain Lookup

**Context**: Use provider-specific tools to check registration.

No command, but simulate a whois or panel search.

> Expected output: Domain listed as available.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[third-party-service]]
