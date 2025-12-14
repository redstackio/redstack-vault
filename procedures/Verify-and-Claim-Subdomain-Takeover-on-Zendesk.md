---
id: proc-verify-claim-zendesk-takeover
tags:
  - subdomain-takeover
  - zendesk
  - impersonation
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
updated_at: '2025-12-14T05:32:23.024Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-and-Claim-Subdomain-Takeover-on-Zendesk

## Summary

This procedure verifies a subdomain takeover vulnerability by recognizing the dangling DNS record's pointer to an unclaimed Zendesk instance and demonstrates claiming it via signup, allowing control for malicious purposes like phishing or defacement.

## Description

Subdomain takeovers occur when a DNS record remains active after a service is decommissioned, pointing to a claimable resource. For support.urbandictionary.com, the record targets Zendesk, enabling any user to register and claim it. This leads to high-impact scenarios such as hosting phishing pages impersonating Urban Dictionary support, eroding user trust. The procedure assumes the inspection step has confirmed the unclaimed status and focuses on verification and exploitation in a controlled manner.

## Requirements

1. Access to the service provider's signup page (e.g., Zendesk)
2. An email address for registration
3. Public DNS resolution to confirm the record

## Defense

Defensive measures and detection strategies:

- Use automated scanners like Subjack or Detectify to identify takeover risks
- Enforce strict DNS management policies to delete records promptly
- Monitor for unauthorized claims on third-party services

## Objectives

1. Confirm the DNS points to an unclaimed instance
2. Successfully claim the subdomain to demonstrate control
3. Highlight risks of brand impersonation and malicious content

## Instructions

### Step 1: Analyze DNS and Service Indicators

**Context**: Review the page and external resources to confirm the takeover vector.

Cross-reference the subdomain's DNS records (using tools like dig or nslookup if available) against known unclaimed service IPs or CNAMEs for Zendesk.

> Expected output: DNS resolves to Zendesk's template servers, matching patterns from takeover databases like Detectify labs.

### Step 2: Register and Claim the Subdomain

**Context**: Use the signup link from the unclaimed page to attempt takeover.

Navigate to the provided signup URL (e.g., http://www.zendesk.com/signup/) and enter the subdomain during the domain claim process.

> Successful execution shows the subdomain associated with the new account, allowing content upload to support.urbandictionary.com.

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
- [[impersonation]]
