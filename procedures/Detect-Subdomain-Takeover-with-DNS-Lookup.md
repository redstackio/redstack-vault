---
id: proc-uuid-001
tags:
  - subdomain-takeover
  - dns
  - reconnaissance
  - cname
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/host-dns-lookup-for-subdomain]]'
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T05:32:24.002Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Detect Subdomain Takeover with DNS Lookup

## Summary

This procedure uses a basic DNS lookup to detect subdomain takeover vulnerabilities by identifying dangling CNAME records that point to unused or abandoned third-party services, such as an Odoo staging instance. It is primarily used in reconnaissance phases to uncover misconfigurations that could allow attackers to claim control of subdomains for phishing or hosting malicious content.

## Description

Subdomain takeovers occur when a company's DNS records reference external services (e.g., Odoo, Heroku, GitHub Pages) that are no longer in use, leaving the records 'dangling.' An attacker can claim the unused service and take over the subdomain. This procedure focuses on querying DNS for CNAME records on target subdomains like odoo-staging.exness.io, which aliased to exness-stg.odoo.com (IP 141.95.172.222), indicating an abandoned Odoo staging setup. Prerequisites include access to a system with DNS resolution tools and public internet connectivity. Expected outcomes include revealing aliases that can be further verified for takeover potential by checking service availability.

## Requirements

1. Network access to public DNS resolvers (no firewall blocks on port 53)
2. Command-line interface with 'host' utility (available on Linux/macOS; use 'nslookup' on Windows)
3. Target subdomain name (e.g., odoo-staging.exness.io)

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using automated tools like dnsrecon or Subjack
- Implement DNS monitoring alerts for changes in third-party service associations
- Use certificate transparency logs and services like SecurityTrails to track subdomain changes

## Objectives

1. Identify CNAME records pointing to potentially claimable services
2. Confirm if the aliased service is active or abandoned
3. Assess risk of subdomain takeover for phishing or impersonation

## Instructions

### Step 1: Perform DNS Lookup on Target Subdomain

**Context**: Query the DNS records for the subdomain to reveal CNAME aliases, IP addresses, and other details that indicate a potential takeover vulnerability.

**Command** ([[commands/host-dns-lookup-for-subdomain]]):
```bash
host odoo-staging.exness.io
```

> The 'host' command performs a DNS lookup, showing if the subdomain is an alias (CNAME) for another domain. In this case, it reveals odoo-staging.exness.io as an alias for exness-stg.odoo.com, with IP 141.95.172.222 and MX handling by eu123a.odoo.com. If the aliased domain (exness-stg.odoo.com) is unused, it can be claimed on Odoo's platform.

### Step 2: Verify Service Availability

**Context**: Follow up by checking if the CNAME target is active; an inactive service confirms the dangling record.

**Command** ([[commands/host-dns-lookup-for-subdomain]]):
```bash
host exness-stg.odoo.com
```

> This resolves the target domain. If it returns an IP but the service (e.g., Odoo staging) is not responding on HTTP/HTTPS, or if the Odoo account is deletable, takeover is possible. Expected output mirrors the alias resolution, but manual verification (e.g., browsing to the URL) shows if it's claimable.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used

- [[commands/host-dns-lookup-for-subdomain]]

## Tools Used


## Tags

- [[subdomain-takeover]]
- [[DNS]]
- [[Reconnaissance]]
