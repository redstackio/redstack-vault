---
id: proc-check-vercel-subdomain
tags:
  - subdomain-takeover
  - vercel
  - dns
type: procedure
tools:
  - '[[tools/Vercel-Dashboard]]'
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
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T05:32:31.318Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Check-Subdomain-Availability-on-Vercel

## Summary

This procedure involves navigating to a Vercel project's domain settings to search for and assess the availability of a target subdomain, identifying potential takeover opportunities from dangling CNAME records.

## Description

Targeted at web platforms using Vercel for hosting, this procedure simulates reconnaissance in a subdomain takeover scenario, such as proxies.sifchain.finance. By inputting the subdomain, the dashboard reveals if it's unclaimed, indicating a misconfiguration where DNS points to Vercel without ownership. Expected outcomes include visibility into deployment status, enabling further exploitation attempts.

## Requirements

1. Active Vercel session from prior login
2. Target subdomain identified (e.g., via DNS tools showing CNAME to cname.vercel-dns.com)
3. Access to a Vercel project or team settings

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records against cloud provider ownership to remove dangling entries
- Implement Vercel domain verification with TXT records to lock subdomains
- Monitor Vercel API logs for unauthorized domain add attempts

## Objectives

1. Determine if subdomain is claimed or available
2. Identify DEPLOYMENT_NOT_FOUND indicators
3. Assess risk for malicious claiming

## Instructions

### Step 1: Access Project Settings

**Context**: From the Vercel dashboard, select or create a project to reach domain management.

Navigate to https://vercel.com/[YourUsername]/[ProjectName]/settings/domains.

> Expected output: Domains tab loads, showing current domains if any.

### Step 2: Search for Target Subdomain

**Context**: Input the subdomain to check its status.

Enter 'proxies.sifchain.finance' (or target) in the search/add domain field and submit.

> Expected output: Subdomain appears as 'Available' or unlinked, without ownership errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Vulnerability Scanning

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Vercel-Dashboard]]

## Tags

- subdomain-takeover
- availability-check
- vercel
