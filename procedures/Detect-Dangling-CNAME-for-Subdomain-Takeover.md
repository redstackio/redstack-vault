---
id: 123e4567-e89b-12d3-a456-426614174001
name: Detect-Dangling-CNAME-for-Subdomain-Takeover
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:26.650Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Gather Victim Host Information]]'
sub_techniques: []
tags:
  - dns-recon
  - subdomain-takeover
commands:
  - '[[commands/dig-cname-lookup]]'
platforms:
  - DNS
tools: []
skill_level: beginner
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---

# Detect-Dangling-CNAME-for-Subdomain-Takeover

## Summary

This procedure identifies dangling CNAME records in DNS configurations that point to third-party services like Wix.com without active site claims, enabling subdomain takeover vulnerabilities.

## Description

In this scenario, the target domain sifchain.finance has a CNAME record leftover from a previous Wix integration that was not properly removed. This misconfiguration allows anyone to detect the vulnerability through DNS queries and potentially claim the domain if unclaimed. The procedure focuses on reconnaissance to uncover such issues, which can lead to full control of the domain for phishing, malware distribution, or XSS attacks.

## Requirements

1. Access to DNS resolution tools like dig or nslookup
2. Public internet connectivity
3. Knowledge of target domain

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using automated tools like dnsrecon
- Implement DNS monitoring for unexpected changes
- Remove unused third-party service integrations promptly

## Objectives

1. Discover misconfigured CNAME records pointing to claimable services
2. Assess potential for subdomain takeover
3. Gather evidence for reporting or exploitation

## Instructions

### Step 1: Perform CNAME Lookup

**Context**: Query the DNS for the target's CNAME record to identify if it points to a service like Wix.

**Command** ([[commands/dig-cname-lookup]]):
```bash
dig CNAME sifchain.finance
```

> This command resolves the CNAME for the domain. Expected output includes the Wix-related alias if dangling.

### Step 2: Analyze Response

**Context**: Review the DNS response for indicators of a dangling record, such as a Wix endpoint without active A/AAAA records.

**Command** (Manual review):
No command needed; parse the dig output manually.

> Look for lines like "sifchain.finance. 3600 IN CNAME xxx.wixdns.net." confirming the misconfiguration.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used

- [[commands/dig-cname-lookup]]

## Tools Used


## Tags

- [[dns-recon]]
- [[subdomain-takeover]]
