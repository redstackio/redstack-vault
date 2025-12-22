---
id: proc-uuid-claim-subdomain
tags:
  - subdomain-takeover
  - discourse
  - phishing
  - exploitation
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
updated_at: '2025-12-14T04:38:49.611Z'
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
# Claim-Dangling-Subdomain-via-Discourse

## Summary

This procedure describes how an attacker with a Discourse account can claim a dangling subdomain like creatorforum.roblox.com to host arbitrary content, exploiting the trusted domain for phishing or clickjacking.

## Description

Discourse allows custom domain mapping for hosted instances. A dangling CNAME enables claiming the subdomain, granting full control to serve malicious pages, steal cookies via shared domain, or enable clickjacking under .roblox.com.

## Requirements

1. A registered Discourse account (free tier suffices)
2. Access to the Discourse admin panel for domain claiming
3. Knowledge of the target CNAME pointer

## Defense

Defensive measures and detection strategies:

- Monitor DNS changes and subdomain resolutions for anomalies
- Use certificate pinning or HSTS to limit subdomain trust
- Regularly reclaim or delete unused third-party service pointers

## Objectives

1. Take ownership of the dangling subdomain
2. Host malicious content leveraging domain trust
3. Enable attacks like phishing or session theft

## Instructions

### Step 1: Log into Discourse Account

**Context**: Prepare the account for domain claiming.

Sign up or log into a Discourse account at discourse.org if not already done.

**Expected Output**: Active user session in Discourse dashboard.

### Step 2: Navigate to Domain Mapping

**Context**: Locate the section for custom domains in Discourse settings.

In the admin panel, go to Settings > Domains and initiate a new custom domain setup.

### Step 3: Claim the Dangling CNAME

**Context**: Map the target subdomain to your Discourse instance.

Enter creatorforum.roblox.com as the custom domain. Discourse will verify the CNAME and grant control if unclaimed.

**Expected Output**: Subdomain now serves your Discourse content; confirm by visiting it.

### Step 4: Host Malicious Content

**Context**: Exploit the control for attack objectives.

Upload phishing pages or configure clickjacking iframes, leveraging .roblox.com cookies for potential theft.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[discourse]]
- [[Phishing]]
- [[exploitation]]
