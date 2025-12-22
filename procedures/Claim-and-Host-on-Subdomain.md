---
tags:
  - takeover
  - impersonation
  - hosting
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/dig-dns-lookup]]'
  - '[[commands/curl-http-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:23.232Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 14a6291c-9d2c-499f-8cdf-7c3946a20529
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim and Host on Subdomain

## Summary

This procedure claims control of a vulnerable subdomain by registering the dangling third-party service and hosting malicious content, enabling phishing or reputational damage as demonstrated in the OWOX subdomain takeover.

## Description

Once a dangling record is verified, create an account on the third-party service (e.g., if pointing to GitHub Pages, set up a repo with the exact name). Configure the service to serve attacker content, leading to DNS propagation. The subdomain then resolves to malicious material, impersonating the organization. Requires no target credentials but relies on public claimability; outcomes include full subdomain control for attacks like malware distribution.

## Requirements

1. Verified dangling service details from prior step
2. Attacker account on the third-party platform
3. Web server or static hosting for malicious content

## Defense

Defensive measures and detection strategies:

- Automate DNS record cleanup on service decommissioning
- Monitor for unauthorized content on subdomains via certificate pinning
- Use web application firewalls to detect anomalous traffic from trusted subdomains

## Objectives

1. Gain ownership of the subdomain
2. Deploy phishing or malware pages
3. Verify control and propagation

## Instructions

### Step 1: Register and Configure Service

**Context**: Claim the unused resource on the third-party service.

**Instructions**: Manually sign up and configure (e.g., for Heroku: heroku create exact-app-name). No command; browser-based.

> Expected: Service points to attacker content.

### Step 2: Verify DNS Propagation and Access

**Context**: Confirm the subdomain now resolves to attacker-hosted content.

**Command** ([[commands/dig-dns-lookup]]):
```bash
 dig CNAME blog.owox.com
```

> Checks resolution. Expected: Points to attacker service.

**Command** ([[commands/curl-http-test]]):
```bash
curl -I http://blog.owox.com
```

> Tests HTTP response. Expected: 200 OK with malicious page headers.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-lookup]]
- [[commands/curl-http-test]]

## Tools Used


## Tags

- [[takeover]]
- [[impersonation]]
