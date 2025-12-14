---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567892
tags:
  - dns-enumeration
  - cname
  - recon
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - DNS
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:39:01.947Z'
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
# Enumerate-Target-DNS-for-Dangling-CNAMEs

## Summary

This procedure involves querying a target's DNS records to identify subdomains with CNAMEs pointing to vulnerable third-party services, such as Instapage, that may be dangling and exploitable for takeover.

## Description

The attack targets misconfigurations where subdomains like www.hacker.one have CNAME records to services like Instapage but are not actively managed. In a web/DNS environment, this reconnaissance step uncovers opportunities for hijacking. Expected outcomes include listing vulnerable records, with prerequisites being public DNS access and basic query tools.

## Requirements

1. Public DNS resolver access.
2. Target domain name (e.g., hacker.one).
3. Tools like dig or online DNS lookup services.

## Defense

Defensive measures and detection strategies:

- Use DNS monitoring tools to alert on unresolved or dangling records.
- Implement short TTLs on CNAMEs and automate cleanup of unused subdomains.
- Conduct regular subdomain audits with tools like dnsdumpster or subfinder.

## Objectives

1. Locate CNAME records pointing to third-party services.
2. Identify if the subdomain is actively claimed or dangling.
3. Prepare for potential takeover if vulnerable.

## Instructions

### Step 1: Query Subdomain DNS Records

**Context**: Perform a CNAME lookup on the target subdomain.

Use a DNS tool to query:

No formalized command; example manual query with dig:

```bash
dig CNAME www.hacker.one
```

> This reveals the CNAME target (e.g., to Instapage). Expected: CNAME to a service like pages.instapage.com.

### Step 2: Check for Active Claim

**Context**: Verify if the CNAME leads to an active, claimed page or error.

Browse to the subdomain or query further.

> Expected output: 404 or unclaimed page on the third-party service, indicating dangling status.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[dns-enumeration]]
- [[recon]]
