---
id: e9548831-cbde-474e-8f61-6e36b057fa1c
name: Identify-Vulnerable-Subdomain-Pointing-to-Unclaimed-Service
type: procedure
verified: false
submitted: true
created_at: '2025-12-14T04:38:39.760Z'
updated_at: '2025-12-14T04:38:39.760Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - subdomain-takeover
  - dns
  - recon
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Identify-Vulnerable-Subdomain-Pointing-to-Unclaimed-Service

## Summary

This procedure involves scanning and querying DNS records to identify subdomains that point to unclaimed external services, such as discontinued Shopify instances, setting the stage for a subdomain takeover attack.

## Description

In a subdomain takeover attack, attackers look for DNS misconfigurations where subdomains continue to resolve to external services (e.g., Shopify, AWS S3) that the organization no longer uses. This procedure focuses on the reconnaissance phase: enumerating subdomains and checking their DNS records for dangling pointers. The target environment is any web-facing domain with public DNS. Expected outcomes include a list of potentially vulnerable subdomains. Prerequisites include access to DNS query tools and knowledge of common third-party services.

## Requirements

1. Access to public DNS resolvers (e.g., via browser or command line)
2. List of target subdomains (from prior enumeration if available)
3. Basic understanding of DNS record types (CNAME, A)

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling entries using automated tools like DNSdumpster or internal scripts
- Implement DNS monitoring for changes and anomalies in subdomain resolutions
- Remove or redirect unused subdomains promptly after decommissioning services

## Objectives

1. Discover subdomains with DNS pointing to unused external services
2. Confirm the service is no longer managed by the organization
3. Prepare for verification of takeover feasibility

## Instructions

### Step 1: Enumerate Subdomains

**Context**: Start by listing potential subdomains of the target domain, such as through certificate transparency logs or brute-forcing common names.

Use online tools like crt.sh or securitytrails.com to query for subdomains associated with the target domain (e.g., example.com).

> Focus on subdomains that might relate to e-commerce or external integrations like 'shop.example.com'.

### Step 2: Query DNS Records

**Context**: For each subdomain, resolve its DNS to identify if it points to an external service like Shopify.

Use a DNS lookup tool (e.g., dig in terminal or online resolver) to check CNAME or A records:

For example, query the subdomain's CNAME:

```bash
dig shop.example.com CNAME
```

> Expected output: A CNAME pointing to something like 'shops.myshopify.com' or Shopify IPs, indicating a potential Shopify integration.

### Step 3: Cross-Reference Service Status

**Context**: Verify if the pointed service is active or discontinued.

Check the organization's documentation or Wayback Machine for historical use of the service. If discontinued, note it as a candidate.

> Success if DNS still points to the service but the subdomain loads no organization content.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[DNS]]
- [[recon]]
