---
tags:
  - subdomain-enumeration
  - dns-recon
  - shopify
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:38:39.442Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 04cce912-0c49-4cd5-8f3b-cf05bf65fed3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Vulnerable-Subdomain-for-Takeover

## Summary

This procedure involves enumerating and verifying subdomains of a target domain to identify those with DNS records pointing to unclaimed third-party services, such as Shopify instances, enabling potential takeover.

## Description

In a subdomain takeover attack, attackers scan for dangling DNS records that point to external services without corresponding active accounts. For Shopify, this means finding CNAME records directing to myshopify.com domains that return a default unclaimed store page. The procedure assumes public DNS access and uses manual or tool-assisted queries to pinpoint misconfigurations. Expected outcomes include a list of vulnerable subdomains ready for claiming, with risks of detection low due to passive reconnaissance.

## Requirements

1. Access to public DNS resolvers
2. Knowledge of target domain and common subdomain enumeration techniques
3. Web browser to verify unclaimed store status

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling entries using tools like DNSdumpster
- Implement domain verification in third-party services like Shopify
- Monitor for anomalous traffic to subdomains

## Objectives

1. Discover subdomains with misconfigured DNS to external services
2. Verify unclaimed status of pointed services
3. Prepare for takeover by documenting vulnerable points

## Instructions

### Step 1: Enumerate Subdomains

**Context**: Start by listing potential subdomains using passive sources or brute-forcing common names.

No specific command; manually query or use online tools to generate a list of subdomains for the target (e.g., shop.target.com).

> Focus on e-commerce related subdomains that might use Shopify.

### Step 2: Query DNS Records

**Context**: For each subdomain, check DNS to identify pointers to Shopify infrastructure.

Use a DNS tool like dig:

```bash
dig shop.target.com CNAME
```

> Expected output: CNAME record pointing to something like unclaimed-store.myshopify.com. If it resolves to Shopify but shows an unclaimed page on HTTP access, it's vulnerable.

### Step 3: Verify Unclaimed Status

**Context**: Access the subdomain URL to confirm it's an unclaimed Shopify instance.

Navigate to http://shop.target.com in a browser.

> Expected output: Default Shopify setup page prompting for store creation, indicating no ownership.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[dns-recon]]
