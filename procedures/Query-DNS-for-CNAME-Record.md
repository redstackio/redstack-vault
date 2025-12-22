---
tags:
  - dns
  - recon
  - cname
type: procedure
tools:
  - '[[tools/dig-DNS-Lookup]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-query-cname-record]]'
verified: false
platforms:
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:38:39.381Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques:
  - '[[Hardware]]'
id: 67f13447-49c1-4645-81bd-8da013d30d7d
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Query-DNS-for-CNAME-Record

## Summary

This procedure uses DNS query tools to inspect CNAME records for a target subdomain, identifying dangling pointers to third-party services like SendGrid that can be exploited for takeover.

## Description

After observing a 404 on a subdomain, querying its DNS records reveals if a CNAME exists without corresponding hosting. In this case, email.smule.com points to SendGrid, indicating an unused alias. This reconnaissance step confirms vulnerability to takeover, where an attacker can claim the subdomain. Requires DNS resolution; common on Linux/macOS with dig installed.

## Requirements

1. DNS lookup tool like dig
2. Network access for public DNS queries
3. Target domain (e.g., email.smule.com)

## Defense

Defensive measures and detection strategies:

- Periodically scan for dangling DNS records using scripts or services like Subdomain Takeover scanners
- Remove unused CNAMEs and monitor third-party service integrations
- Enable DNSSEC to prevent unauthorized claims

## Objectives

1. Retrieve CNAME record details
2. Confirm dangling reference to unused service
3. Validate takeover potential

## Instructions

### Step 1: Execute DNS Query

**Context**: Query the specific CNAME record type for the subdomain.

**Command** ([[commands/dig-query-cname-record]]):
```bash
dig email.smule.com CNAME
```

> This command sends a DNS query for the CNAME record. Expected output includes lines like "email.smule.com. 3600 IN CNAME something.sendgrid.net.", confirming the pointer.

### Step 2: Analyze Response

**Context**: Parse the output to identify the target service.

Review the ANSWER SECTION for CNAME targets.

> Look for services like sendgrid.net; cross-reference with known takeover vectors.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: DNS

### Sub-Techniques

- [[Hardware]] Gather Victim Host Information: DNS

## Commands Used

- [[commands/dig-query-cname-record]]

## Tools Used

- [[tools/dig-DNS-Lookup]]

## Tags

- [[DNS]]
- [[recon]]
- [[cname]]
