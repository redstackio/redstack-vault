---
id: uuid-for-proc1
tags:
  - dns
  - recon
  - subdomain-takeover
type: procedure
tools:
  - '[[tools/dig]]'
  - '[[tools/nslookup]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-cname-lookup]]'
  - '[[commands/nslookup-query]]'
verified: false
platforms:
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:38:49.429Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Dangling-DNS-CNAME-Records

## Summary

This procedure involves querying public DNS records to identify CNAME entries pointing to third-party services that may be unclaimed or expired, a common precursor to subdomain takeover attacks.

## Description

In scenarios like the Uber signup.uber.com vulnerability, attackers scan for dangling DNS records where a subdomain's CNAME points to a decommissioned or unmonitored hosting provider domain (e.g., Netlify). This allows reconnaissance of potential takeover vectors without direct access to the target's infrastructure. The process relies on standard DNS tools and public resolvers, targeting misconfigurations from service migrations or lapsed monitoring.

## Requirements

1. Public internet access for DNS queries
2. Installation of DNS tools like dig or nslookup
3. Target subdomain name (e.g., signup.uber.com)

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using automated tools like DNS linter
- Implement monitoring for subdomain resolutions and alerts on unclaimed third-party points
- Use CAA records to restrict certificate issuance on subdomains

## Objectives

1. Discover misconfigured DNS entries
2. Identify potential takeover targets
3. Map attack surface via public DNS

## Instructions

### Step 1: Query CNAME Record

**Context**: Perform a DNS lookup to retrieve the CNAME for the target subdomain, checking if it points to a third-party service.

**Command** ([[commands/dig-cname-lookup]]):
```bash
dig signup.uber.com CNAME
```

> This command queries the authoritative DNS server for the CNAME record. Expected output includes lines like "signup.uber.com. 300 IN CNAME unclaimed-site.netlify.app.", indicating a potential dangling record if the Netlify site is inactive.

### Step 2: Alternative Verification with Nslookup

**Context**: Cross-verify the CNAME using an alternative tool for confirmation.

**Command** ([[commands/nslookup-query]]):
```bash
nslookup -type=CNAME signup.uber.com
```

> Output shows the server responding with the CNAME target. Success if it matches a known hosting provider like Netlify without active resolution.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- None

## Commands Used

- [[commands/dig-cname-lookup]]
- [[commands/nslookup-query]]

## Tools Used

- [[tools/dig]]
- [[tools/nslookup]]

## Tags

- [[DNS]]
- [[recon]]
- [[subdomain-takeover]]
