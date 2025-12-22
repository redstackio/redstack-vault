---
tags:
  - whois
  - domain-recon
type: procedure
tools:
  - '[[tools/whois]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/whois-domain-ownership-check]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:38:39.987Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: b39e7f70-e77b-4b5b-88d6-a8e47f17a2ca
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Check-Domain-Ownership-with-WHOIS

## Summary

This procedure queries the WHOIS database to retrieve domain registration details, confirming ownership and relevance to a target organization during reconnaissance.

## Description

WHOIS lookups provide public registration info for domains, useful for validating if a vulnerable subdomain belongs to the intended target (e.g., linking crossinstall.com to Twitter, Inc.). In takeover scenarios, this ensures the finding is in-scope. The process involves piping output to filter organization fields; no credentials needed, but rate limits may apply. Expected outcomes: confirmation of ownership, aiding vulnerability prioritization.

## Requirements

1. WHOIS client installed
2. Target domain name (e.g., crossinstall.com)
3. Basic command-line access

## Defense

Defensive measures and detection strategies:

- Use privacy-protected registrations to obscure WHOIS data
- Monitor for unusual WHOIS queries on your domains
- Implement RDAP for more controlled info disclosure

## Objectives

1. Verify domain association with target entity
2. Establish report legitimacy
3. Identify potential expiration risks

## Instructions

### Step 1: Query WHOIS Database

**Context**: Retrieve full registration details and filter for organization info to confirm ownership.

**Command** ([[commands/whois-domain-ownership-check]]):
```bash
whois crossinstall.com | grep Org
```

> This pipes WHOIS output to grep, searching for 'Org' lines. Expected output: Registrant Organization: Twitter, Inc., etc., confirming target association.

### Step 2: Review Full Output if Needed

**Context**: If filtered results are insufficient, inspect complete WHOIS for additional context like admin contacts.

**Command** (Basic whois):
```bash
whois crossinstall.com
```

> Parse for expiration dates or other details to assess urgency.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques

- None

## Commands Used

- [[commands/whois-domain-ownership-check]]

## Tools Used

- [[tools/whois]]

## Tags

- [[domain-recon]]
- [[tools/whois]]
