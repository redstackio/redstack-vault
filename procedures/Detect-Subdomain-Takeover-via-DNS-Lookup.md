---
tags:
  - subdomain-takeover
  - dns-recon
  - misconfiguration
type: procedure
tools:
  - '[[tools/nslookup]]'
tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
commands:
  - '[[commands/nslookup-dns-query]]'
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:23.446Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: a8a3d3be-d980-4e0f-86bc-9ae1fac8bbbd
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Hardware]]'
  - '[[Exploit Public-Facing Application]]'
---
# Detect-Subdomain-Takeover-via-DNS-Lookup

## Summary

This procedure detects subdomain takeover vulnerabilities by querying DNS records for misconfigured CNAMEs pointing to unused external services, such as Tumblr's domains.tumblr.com, allowing attackers to claim the subdomain for malicious purposes like phishing.

## Description

In this attack scenario, a target's DNS entry for a subdomain (e.g., engineering.zomato.com) is misconfigured to point to an external service no longer in use. By performing a DNS lookup, the CNAME and IP resolutions reveal the vulnerability. If the subdomain is unclaimed on the external platform, an attacker can register it, gaining control under the trusted parent domain. This can lead to phishing sites, content spoofing, or information disclosure. The procedure requires only public DNS access and is effective against web-facing applications relying on subdomains for trust.

## Requirements

1. Internet connectivity for DNS resolution
2. Access to a DNS query tool like nslookup (available on most OS)
3. Knowledge of the target subdomain (e.g., from reconnaissance)

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using tools like dnsdumpster or automated scanners
- Implement DNS monitoring for changes and unused records
- Use subdomain management services to prevent takeovers on platforms like Tumblr or Heroku

## Objectives

1. Identify misconfigured DNS entries pointing to external services
2. Confirm availability for takeover on the external platform
3. Assess impact for phishing or spoofing risks

## Instructions

### Step 1: Perform DNS Lookup on Target Subdomain

**Context**: Query the DNS server to resolve the subdomain and retrieve CNAME and IP details, checking for pointers to unused services.

**Command** ([[commands/nslookup-dns-query]]):
```bash
nslookup engineering.zomato.com
```

> This command queries the DNS for the hostname, returning the CNAME (e.g., domains.tumblr.com) and A records (e.g., IPs 66.6.42.22 and 66.6.43.22). If the CNAME points to an external service like Tumblr, proceed to verify claimability by attempting to register the subdomain on Tumblr's platform.

### Step 2: Validate Takeover Feasibility

**Context**: Manually check the external service (Tumblr) to see if the subdomain is available for claiming, confirming the vulnerability.

**Command** (No specific command; manual verification):

> Visit Tumblr's subdomain creation page and attempt to claim 'engineering.zomato.com'. Success indicates the takeover is possible, enabling setup of malicious content.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]
- [[Initial Access]]

### Techniques

- [[Hardware]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/nslookup-dns-query]]

## Tools Used

- [[tools/nslookup]]

## Tags

- [[subdomain-takeover]]
- [[dns-recon]]
