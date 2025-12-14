---
tags:
  - subdomain-takeover
  - dns
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-resolve-subdomain]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T05:32:23.890Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: e8c948c9-df22-43d9-baf3-a9645a2d78bb
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Discover Dangling Subdomain DNS Record

## Summary

This procedure identifies subdomains with DNS records pointing to unused third-party services like Webflow, enabling detection of subdomain takeover vulnerabilities that could lead to domain impersonation.

## Description

In this attack scenario, attackers resolve DNS records of target subdomains to find pointers to IPs associated with hosting proxies (e.g., Webflow's 151.101.16.229). An unused site results in a 404 error, indicating a dangling configuration. The target environment is any web application with public DNS. Prerequisites include DNS resolution access. Expected outcomes: Confirmation of takeover potential, allowing further exploitation like claiming the site for malicious hosting.

## Requirements

1. Access to DNS resolution tools (e.g., dig or nslookup)
2. Knowledge of target domain and suspected subdomains
3. Ability to make HTTP requests to verify site status

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling entries using automated scanners
- Implement CNAME flattening or monitoring for unused third-party integrations
- Use services like DNS monitoring tools to alert on 404s from proxies

## Objectives

1. Discover misconfigured DNS records pointing to reclaimable services
2. Verify site inactivity to confirm takeover feasibility
3. Assess impact on brand reputation and phishing risks

## Instructions

### Step 1: Resolve Subdomain DNS

**Context**: Query the DNS to obtain the IP or CNAME for the subdomain, identifying if it points to a known third-party proxy.

**Command** ([[commands/dig-resolve-subdomain]]):
```bash
dig +short sales.mixmax.com
```

> This command resolves the subdomain to its IP (e.g., 151.101.16.229). Cross-reference the IP with known service ranges like Webflow's edge network to confirm association.

### Step 2: Verify Site Status

**Context**: Check the HTTP response to determine if the pointed site is active or unused.

**Command** (using curl for HTTP HEAD):
```bash
curl -I https://sales.mixmax.com
```

> Expect a 404 Not Found response or Webflow-specific error, indicating the site is unclaimed and dangling.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques


## Commands Used

- [[commands/dig-resolve-subdomain]]
- curl (for HTTP verification)

## Tools Used


## Tags

- [[subdomain-takeover]]
- [[dns-recon]]
