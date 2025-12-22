---
id: proc-uuid-3
tags:
  - whois-query
  - registration-check
type: procedure
tools:
  - '[[tools/whois]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/whois-domain-query]]'
verified: false
platforms:
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:38:39.831Z'
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
# Query-WHOIS-for-Domain-Registration-Status

## Summary

This procedure queries the WHOIS database to confirm a domain's registration status, ensuring the dangling CNAME points to an truly available domain for takeover.

## Description

WHOIS provides authoritative registration data. For .us TLDs, it queries IANA and nic.us. This step validates registrar findings and checks for any overlooked registrations. Useful in subdomain takeover scenarios involving government domains. Prerequisites: whois client installed. Expected outcomes: "No Data Found" confirming availability, or registrant details if registered.

## Requirements

1. whois command-line tool installed
2. Internet access for WHOIS servers
3. Target domain name

## Defense

Defensive measures and detection strategies:

- Integrate WHOIS monitoring into DNS management workflows
- Use rate-limiting on WHOIS queries to detect reconnaissance
- Register defensive domains for all CNAME targets

## Objectives

1. Retrieve domain ownership and registration details
2. Confirm unregistered status
3. Identify TLD-specific info (e.g., .us SOA)

## Instructions

### Step 1: Execute WHOIS Query

**Context**: Query the WHOIS server for the domain to retrieve or confirm lack of registration data.

**Command** ([[commands/whois-domain-query]]):
```bash
whois example-domain.us
```

> Output starts with IANA WHOIS for .us, including contacts, then nic.us response with "No match for domain" or similar, indicating unregistered status.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques


## Commands Used

- [[commands/whois-domain-query]]

## Tools Used

- [[tools/whois]]

## Tags

- [[tools/whois]]
- [[domain-recon]]
