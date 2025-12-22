---
id: proc-identify-dangling-subdomain
tags:
  - subdomain-takeover
  - dns
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-resolve-subdomain]]'
  - '[[commands/dig-dns-lookup]]'
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:23.282Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-and-Verify-Dangling-Subdomain

## Summary

This procedure outlines the reconnaissance and verification steps to identify subdomains with dangling DNS records pointing to expired third-party services, such as FreshDesk, enabling potential subdomain takeover attacks.

## Description

In scenarios like the KIWI.KI vulnerability, organizations trial SaaS tools like FreshDesk and leave DNS records (e.g., CNAME for service.kiwi.ki) pointing to the provider after expiration. Attackers scan for such misconfigurations to claim control. This procedure involves DNS resolution, HTTP probing, and service status checks to confirm vulnerability without exploiting it. Prerequisites include basic DNS knowledge and access to resolution tools; expected outcomes are confirmation of claimable subdomains leading to phishing risks.

## Requirements

1. Internet access for DNS queries and HTTP requests
2. Domain enumeration list or known subdomain (e.g., service.kiwi.ki)
3. Knowledge of third-party service claiming processes (e.g., FreshDesk documentation)

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling entries using automated scanners like dnsdumpster or subjack
- Monitor third-party service expirations and remove associated DNS records promptly
- Implement DNS monitoring alerts for unresolved or hijacked subdomains

## Objectives

1. Discover subdomains pointing to inactive SaaS providers
2. Verify expiration status to assess takeover risk
3. Document findings for reporting or exploitation

## Instructions

### Step 1: Enumerate and Resolve Subdomain

**Context**: Begin by resolving the target subdomain to identify if it points to a third-party service.

**Command** ([[commands/dig-dns-lookup]]):
```bash
dig service.kiwi.ki
```

> This command queries DNS for the subdomain's records, revealing CNAME or A records pointing to providers like freshdesk.com. Expected output includes authority sections showing the dangling pointer.

### Step 2: Probe HTTP Response

**Context**: Visit or curl the subdomain to check for service-specific responses indicating expiration.

**Command** ([[commands/curl-resolve-subdomain]]):
```bash
curl -I http://service.kiwi.ki/
```

> The curl command fetches headers; look for FreshDesk indicators (e.g., Server: nginx/1.14.0, or error pages mentioning expired accounts). Successful output shows resolution but inactive service status.

### Step 3: Confirm Service Expiration

**Context**: Manually verify the third-party account status via public checks or documentation.

No command needed; search for the domain in the provider's system or check expiration dates. Expected: Confirmation that the service is claimable by new users.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-lookup]]
- [[commands/curl-resolve-subdomain]]

## Tools Used


## Tags

- [[subdomain-takeover]]
- [[dns-recon]]
