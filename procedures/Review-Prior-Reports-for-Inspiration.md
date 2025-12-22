---
id: proc-uuid-001
tags:
  - reconnaissance
  - subdomain-takeover
type: procedure
tools: []
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
  - '[[Software]]'
updated_at: '2025-12-14T04:38:39.505Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---
# Review-Prior-Reports-for-Inspiration

## Summary

This procedure involves analyzing previously disclosed vulnerability reports to gain inspiration for identifying similar subdomain takeover opportunities on a target domain's assets.

## Description

In a subdomain takeover attack, starting with reconnaissance is key. By reviewing public reports, such as those on HackerOne, attackers can identify patterns in DNS misconfigurations, like dangling CNAMEs, specific to the target's infrastructure. This step targets environments with public DNS records and helps prioritize subdomains for deeper inspection, leading to discovery of exploitable records pointing to unregistered TLDs.

## Requirements

1. Access to public vulnerability disclosure platforms (e.g., HackerOne)
2. Basic knowledge of DNS and subdomain vulnerabilities
3. Internet connectivity for report browsing

## Defense

Defensive measures and detection strategies:

- Regularly audit public vulnerability reports for patterns in your domain
- Implement internal monitoring for DNS changes and dangling records
- Use tools like DNS enumeration scanners to proactively identify issues

## Objectives

1. Identify subdomains or assets similar to past vulnerabilities
2. Inspire targeted enumeration on the current asset
3. Uncover potential DNS misconfigurations early

## Instructions

### Step 1: Search for Relevant Reports

**Context**: Locate reports on the target organization involving subdomain takeovers or DNS issues.

No specific command; manually search platforms like HackerOne for reports on the target domain (e.g., "affirm subdomain takeover").

> Focus on reports detailing DNS CNAME issues to extract subdomain names or patterns.

### Step 2: Analyze Report Details

**Context**: Extract technical details from the report to guide your enumeration.

Review the report's attack steps, such as subdomains tested and tools used, to replicate on your target.

> Expected outcome: A list of subdomains to test, inspired by report #1297689 in this case.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Software]] Gather Victim Host Information: DNS

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[subdomain-takeover]]
