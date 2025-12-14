---
tags:
  - subdomain-takeover
  - dns
  - shopify
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:51:10.849Z'
sub_techniques: []
id: 05da7a04-eae1-43ad-bb1b-990b3b680a80
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Discover-Unclaimed-Shopify-Subdomain

## Summary

This procedure identifies subdomains with dangling DNS records pointing to unclaimed Shopify infrastructure, enabling potential subdomain takeover by revealing misconfigurations where records were left after abandoned projects.

## Description

In scenarios where a company plans to host content on a third-party platform like Shopify but abandons the effort, DNS records may remain active, pointing to the provider's servers without an associated store. This procedure involves querying DNS for target subdomains (e.g., blog.example.com) and verifying if they resolve to Shopify's infrastructure (such as shops.myshopify.com CNAME) but return no active store, indicating an unclaimed state. The target environment is any domain using external services, with expected outcomes including a list of vulnerable subdomains ripe for takeover.

## Requirements

1. Internet access for DNS queries
2. Basic knowledge of DNS resolution and third-party services like Shopify
3. Tools for DNS lookup (e.g., browser-based DNS checkers or dig command)

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling entries using automated scanners like dnsdumpster or subjack
- Implement domain monitoring alerts for unclaimed third-party associations
- Remove unused DNS records promptly after project abandonment

## Objectives

1. Enumerate and confirm unclaimed subdomains pointing to Shopify
2. Assess potential for takeover without alerting the target
3. Gather evidence for reporting or exploitation

## Instructions

### Step 1: Enumerate Target Subdomains

**Context**: Start by identifying potential subdomains through common names like 'blog', 'shop', or 'store' associated with the target domain.

**Instructions**: Use online DNS lookup tools or command-line to query CNAME/A records for suspected subdomains.

For example, query blog.exchangemarketplace.com:

```bash
dig blog.exchangemarketplace.com CNAME
```

> This command resolves the CNAME; expect output showing a record like 'shops.myshopify.com' if dangling.

### Step 2: Verify Unclaimed Status

**Context**: Confirm the record points to Shopify but no store is active.

**Instructions**: Access the HTTPS URL of the subdomain in a browser and check for Shopify's unclaimed domain error page (e.g., 'This shop is unavailable' or 404).

Visit: https://blog.exchangemarketplace.com/

> Successful output: No valid store loads, confirming unclaimed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[DNS]]
- [[shopify]]
