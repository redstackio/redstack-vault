---
tags:
  - initial-access
  - subdomain-takeover
  - squarespace
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:09.398Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e19803e1-30da-45a0-9908-cbd4d6929b01
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim Subdomain with Squarespace

## Summary

This procedure demonstrates claiming control of a dangling subdomain by creating a Squarespace account and associating the unclaimed domain, enabling the attacker to host arbitrary content for phishing or other exploits.

## Description

Once a subdomain like www.codefi.consensys.net is verified as unclaimed on Squarespace, register a free account, set up a site, and claim the domain via the dashboard. This grants full control, bypassing main domain securities for attacks like XSS or cookie theft.

## Requirements

1. Free Squarespace account
2. Identified unclaimed subdomain
3. Browser access to Squarespace dashboard

## Defense

Defensive measures and detection strategies:

- Monitor third-party hosting dashboards for unauthorized claims
- Implement DNS monitoring alerts for CNAME changes
- Use subdomain takeover detection tools like Subjack or DNSDumpster

## Objectives

1. Secure control over the subdomain
2. Host malicious payloads
3. Enable impacts like phishing and CSP bypass

## Instructions

### Step 1: Create Squarespace Account and Site

**Context**: Set up the hosting environment.

No command; visit squarespace.com, register a new account, and create a basic website template.

> Choose a free trial or basic plan to proceed.

### Step 2: Claim the Subdomain

**Context**: Associate the dangling domain with your site.

No command; In the Squarespace dashboard, navigate to Settings > Domains > Use a domain I own, enter www.codefi.consensys.net, and follow prompts to claim.

> Upon success, upload custom HTML/JS to the site; verify by accessing the subdomain.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[initial-access]]
- [[subdomain-takeover]]
- [[squarespace]]
