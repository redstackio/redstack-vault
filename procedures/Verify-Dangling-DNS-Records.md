---
id: proc-verify-dangling-dns
tags:
  - dns-verification
  - dangling-records
  - takeover-check
type: procedure
tools:
  - '[[tools/Dig]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-lookup]]'
verified: false
platforms:
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:38:39.897Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Verify-Dangling-DNS-Records

## Summary

This procedure inspects DNS records of enumerated subdomains to detect dangling pointers to inactive third-party services, such as the Freshdesk CNAME for fddkim.zomato.com.

## Description

Dangling DNS records occur when a subdomain points to a decommissioned service without removing the record, allowing takeovers. Here, fddkim.zomato.com's TXT/CNAME to Freshdesk was inactive, confirmed by failed HTTP access. Prerequisites: DNS query tools. Outcomes: Identification of claimable subdomains for exploitation.

## Requirements

1. Access to DNS resolver (e.g., public DNS)
2. List of subdomains from enumeration
3. Browser for service verification

## Defense

Defensive measures and detection strategies:

- Automate DNS audits with scripts checking CNAME validity
- Use monitoring tools like DNSDumpster for external scans
- Promptly remove unused DNS entries post-service decommissioning

## Objectives

1. Query specific subdomain DNS records
2. Confirm pointer to unclaimed service
3. Validate inactivity via HTTP probe

## Instructions

### Step 1: DNS Record Lookup

**Context**: Retrieve TXT or CNAME records to identify service pointers.

**Command** ([[commands/dig-lookup]]):
```bash
dig fddkim.zomato.com TXT +short
```

> Outputs records like "v=spf1 include:freshdesk.com". Expected: Pointer to Freshdesk.

### Step 2: Service Accessibility Check

**Context**: Attempt to access the resolved endpoint to confirm dangling status.

**Command** ([[commands/curl-probe]]):
```bash
curl -I https://fddkim.freshdesk.com
```

> Returns 404 or unclaimed message. Expected: No active site, indicating takeover potential.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques

- None

## Commands Used

- [[commands/dig-lookup]]
- [[commands/curl-probe]]

## Tools Used

- [[tools/Dig]]

## Tags

- [[dns-verification]]
- [[dangling-records]]
