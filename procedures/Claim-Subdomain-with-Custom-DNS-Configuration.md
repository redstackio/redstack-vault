---
tags:
  - dns-configuration
  - ssl-provisioning
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:26.543Z'
sub_techniques: []
id: cb2202f2-c664-456e-8377-e9fb6c01c4ae
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim-Subdomain-with-Custom-DNS-Configuration

## Summary

This procedure configures a custom DNS record in Ghost Pro to claim the target subdomain, exploiting the existing CNAME for validation and automatically provisioning a valid SSL certificate.

## Description

Ghost.io's validation process checks for the presence of a CNAME record pointing to their service, without verifying ownership. By adding the custom domain (e.g., engineering.udemy.com) to a matching publication, the system passes validation and takes control, serving content and issuing SSL. This targets web/DNS environments and results in full subdomain hijacking.

## Requirements

1. Ghost Pro account with matching publication
2. Knowledge of target subdomain from prior recon
3. Access to Ghost dashboard

## Defense

Defensive measures and detection strategies:

- Implement CNAME flattening or wildcard DNS to obscure subdomains
- Use certificate transparency logs to monitor unexpected SSL issuances
- Conduct regular subdomain enumeration and cleanup

## Objectives

1. Validate and claim the subdomain via existing DNS
2. Provision SSL for secure impersonation
3. Enable arbitrary content delivery

## Instructions

### Step 1: Access Domain Settings

**Context**: Enter the custom domain in the publication's settings.

No command; in dashboard, go to Settings > Domains > Add Custom Domain, enter 'engineering.udemy.com'.

> Ghost will prompt for DNS verification.

### Step 2: Complete Validation

**Context**: Leverage the pre-existing CNAME to pass Ghost's check.

No command; save configuration—Ghost detects the CNAME and validates automatically.

> Expected: Success message, SSL provisioning starts (may take minutes).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[dns-configuration]]
- [[ssl-provisioning]]
- [[subdomain-takeover]]
