---
id: proc-verify-dns-misconfig
tags:
  - dns-misconfiguration
  - verification
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/nslookup-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T05:32:31.428Z'
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
# Verify-DNS-Misconfiguration

## Summary

This procedure verifies if a subdomain's DNS configuration is vulnerable to takeover by checking for improper authentication or dangling records, as in the kiosk.owox.com case where misconfiguration allowed unauthorized claiming.

## Description

DNS misconfigurations, such as unclaimed CNAMEs to services like AWS S3 or GitHub Pages, enable subdomain takeovers. This procedure involves querying and analyzing DNS responses to confirm vulnerability without triggering alerts. In the OWOX scenario, this step would reveal the lack of authentication protecting the subdomain resource.

## Requirements

1. Access to DNS resolution tools.
2. Knowledge of common takeover providers (AWS, Heroku, etc.).
3. Specific subdomain target.

## Defense

Defensive measures and detection strategies:

- Use automated DNS monitoring tools to detect dangling records.
- Enforce strict authentication on all third-party DNS delegations.

## Objectives

1. Confirm dangling or misconfigured DNS records.
2. Identify the third-party service involved.
3. Assess takeover feasibility.

## Instructions

### Step 1: Query DNS Records

**Context**: Use nslookup to retrieve detailed DNS information for the subdomain.

**Command** ([[commands/nslookup-query]]):
```bash
nslookup kiosk.owox.com
```

> The command outputs server, address, and name records. Look for CNAMEs pointing to unowned services; successful output indicates potential vulnerability if no active auth is present.

### Step 2: Cross-Verify with Provider

**Context**: Manually check the resolved service (e.g., via browser) to see if it's claimable.

No command; access the provider's site with the subdomain's alias to confirm availability.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- None

## Commands Used

- [[commands/nslookup-query]]

## Tools Used

- None

## Tags

- [[dns-misconfiguration]]
- [[verification]]
