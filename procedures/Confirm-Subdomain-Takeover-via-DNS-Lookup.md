---
tags:
  - subdomain-takeover
  - dns
  - recon
type: procedure
tools:
  - '[[tools/host]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/host-dns-lookup]]'
verified: false
platforms:
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:51:10.601Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 87c790ec-dd9e-4da2-b785-e1ede4863d92
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Confirm-Subdomain-Takeover-via-DNS-Lookup

## Summary

This procedure uses DNS queries to verify that a subdomain's record is dangling, pointing to a third-party provider like Fastly without an active service, confirming takeover vulnerability.

## Description

After observing an HTTP error, a DNS lookup reveals CNAME records aliasing to the provider's infrastructure (e.g., shopify-e.map.fastly.net). This misconfiguration allows an attacker to claim the subdomain on Fastly and redirect traffic, enabling phishing or malicious content hosting under the trusted domain. The procedure applies to any DNS-resolvable subdomain and assumes public query access.

## Requirements

1. Access to DNS resolution tools
2. The target subdomain name
3. Network connectivity for DNS queries (UDP/TCP port 53)

## Defense

Defensive measures and detection strategies:

- Use DNS auditing tools to scan for unused CNAMEs to providers
- Implement certificate transparency monitoring for subdomain changes
- Automate checks with tools like dnsrecon or subjack for takeover risks

## Objectives

1. Resolve the subdomain to identify provider aliases
2. Confirm the record is unregistered and dangling
3. Validate the path to potential exploitation

## Instructions

### Step 1: Perform DNS Resolution

**Context**: Query the DNS for the subdomain to retrieve CNAME chains and IP addresses, confirming linkage to vulnerable infrastructure.

**Command** ([[commands/host-dns-lookup]]):
```bash
host genghis-cdn.shopify.io
```

> This command performs a DNS lookup using the host utility. Expected output: 'genghis-cdn.shopify.io is an alias for shopify-e.map.fastly.net. shopify-e.map.fastly.net is an alias for prod.shopify-e.map.fastlylb.net. prod.shopify-e.map.fastlylb.net has address 151.101.60.108'. Success is shown by aliases to the provider without active service indicators.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: DNS

### Sub-Techniques


## Commands Used

- [[commands/host-dns-lookup]]

## Tools Used

- [[tools/host]]

## Tags

- [[subdomain-takeover]]
- [[DNS]]
- [[recon]]
