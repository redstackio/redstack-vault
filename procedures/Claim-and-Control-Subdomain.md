---
id: proc-claim-subdomain
tags:
  - subdomain-takeover
  - initial-access
  - exploitation
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
updated_at: '2025-12-14T05:32:31.422Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim-and-Control-Subdomain

## Summary

This procedure outlines claiming control of a vulnerable subdomain like kiosk.owox.com by registering the dangling resource on the third-party provider, enabling the attacker to host malicious content.

## Description

Once a misconfiguration is verified, the attacker claims the unowned service (e.g., an unused S3 bucket) associated with the DNS record. In the OWOX case, improper authentication allowed this, granting full control for phishing or malware distribution. The process is typically manual via provider dashboards, with outcomes including subdomain redirection to attacker servers.

## Requirements

1. Account on the third-party provider (e.g., AWS, GitHub).
2. Verified vulnerability from prior steps.
3. Browser access for dashboard interaction.

## Defense

Defensive measures and detection strategies:

- Monitor provider dashboards for unauthorized claims.
- Use DNSSEC and regular audits to prevent dangling records.

## Objectives

1. Claim the unowned resource.
2. Redirect subdomain to malicious content.
3. Achieve persistent control for exploitation.

## Instructions

### Step 1: Access Provider Dashboard

**Context**: Log into the inferred provider (from DNS) and search for the dangling resource.

No command; use a web browser to navigate to the provider's claim interface (e.g., GitHub Pages setup).

### Step 2: Claim and Configure

**Context**: Register ownership and update settings to point to attacker-controlled hosting.

No command; follow provider-specific steps to claim and upload content. Verify by accessing http://kiosk.owox.com/ to see controlled page.

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
- [[exploitation]]
