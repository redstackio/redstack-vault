---
id: proc-uuid-detect
name: Detect-Unclaimed-Webflow-Subdomain
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.517Z'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Gather Victim Host Information]]'
sub_techniques:
  - '[[Hardware]]'
tags:
  - reconnaissance
  - dns
  - subdomain-takeover
  - webflow
platforms:
  - Web
  - DNS
commands: []
tools: []
skill_level: intermediate
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---

# Detect-Unclaimed-Webflow-Subdomain

## Summary

This procedure outlines the reconnaissance steps to identify a subdomain takeover opportunity by checking for default error pages and DNS records pointing to unclaimed Webflow services, enabling early detection of vulnerable configurations.

## Description

In a subdomain takeover attack, attackers scan for subdomains with DNS records (e.g., CNAME) pointing to external services like Webflow that are no longer claimed by the owner. This procedure focuses on visiting the subdomain, verifying DNS, and checking the provider portal to confirm the unclaimed status. It targets web environments with misconfigured DNS and is commonly used in external reconnaissance to map attack surfaces. Prerequisites include internet access and basic knowledge of DNS queries. Expected outcomes: Confirmation of vulnerability, setting the stage for exploitation.

## Requirements

1. Web browser for accessing subdomains and portals
2. DNS resolution capability (browser or command-line tools like dig/nslookup)
3. Access to Webflow (free account for checking status)

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using tools like dnsdumpster or internal scripts
- Implement domain monitoring services (e.g., Certificate Transparency logs) to alert on unauthorized claims
- Use DNS security extensions (DNSSEC) to prevent unauthorized modifications, though not directly mitigating takeovers

## Objectives

1. Identify default service pages indicating abandonment
2. Verify DNS points to claimable services like Webflow
3. Confirm availability in the provider's dashboard for exploitation potential

## Instructions

### Step 1: Access the Target Subdomain

**Context**: Visit the subdomain to check for indicators of an unclaimed hosting service.

No specific command; use a browser to navigate to https://jet.acronis.com.

> Observe the page source and content for Webflow branding or 404 errors.

### Step 2: Query DNS Records

**Context**: Confirm the CNAME record to identify the service provider.

Use browser-based DNS tools or terminal:

```bash
# Example using dig (if available)
dig CNAME jet.acronis.com
```

> Expected output includes "jet.acronis.com. CNAME proxy-ssl.webflow.com."

### Step 3: Check Webflow Portal

**Context**: Log in to verify the domain's status directly.

Navigate to webflow.com, log in, and search for or attempt to add the domain in custom domains.

> Look for messages indicating the domain is unclaimed or expired.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- [[Hardware]] DNS

## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[DNS]]
- [[subdomain-takeover]]
- [[webflow]]
