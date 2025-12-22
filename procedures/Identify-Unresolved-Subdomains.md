---
tags:
  - dns
  - reconnaissance
  - subdomain-enumeration
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-dns-lookup]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T03:16:20.693Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 764ed86a-8a24-4a96-8f99-e5ebc2cf1b19
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Identify-Unresolved-Subdomains

## Summary

This procedure detects subdomains that fail to resolve via DNS queries, highlighting potential dangling records vulnerable to takeover on web platforms.

## Description

In scenarios like the unresolved http://presentatie.werkenbijmcdonalds.nl/, attackers enumerate domains to find those without active hosting. This involves DNS queries to check for NXDOMAIN or no responses, indicating unused subdomains that could be claimed if pointed to external services. Prerequisites include public DNS access; outcomes enable further takeover assessment.

## Requirements

1. Access to DNS resolver (e.g., public internet)
2. Target domain name (e.g., werkenbijmcdonalds.nl)
3. Basic command-line tools like dig

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling entries
- Monitor for unexpected subdomain resolutions
- Use DNSSEC to prevent unauthorized claims

## Objectives

1. Discover unresolved subdomains
2. Confirm lack of active hosting
3. Identify candidates for takeover

## Instructions

### Step 1: Perform DNS Lookup

**Context**: Query the subdomain to check if it resolves to an IP or CNAME.

**Command** ([[commands/dig-dns-lookup]]):
```bash
dig presentatie.werkenbijmcdonalds.nl +short
```

> This command queries for A records. Expected output: empty or no response, indicating unresolved status. If CNAME exists but points to unused service, note it for next steps.

### Step 2: Verify Accessibility

**Context**: Attempt HTTP access to confirm failure.

**Command** ([[commands/curl-http-check]]):
```bash
curl -I http://presentatie.werkenbijmcdonalds.nl/
```

> Expect connection timeout or error. Success if no content served.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-lookup]]
- [[commands/curl-http-check]]

## Tools Used


## Tags

- [[DNS]]
- [[Reconnaissance]]
