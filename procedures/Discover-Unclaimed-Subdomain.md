---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - subdomain-takeover
  - dns
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-cname-lookup]]'
verified: false
platforms:
  - DNS
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:51:10.429Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Discover-Unclaimed-Subdomain

## Summary

This procedure identifies subdomains vulnerable to takeover by checking DNS records for pointers to external services like statuspage.io that lack active claims, allowing reconnaissance of hijackable assets.

## Description

In scenarios like the Vimeo incident, attackers scan for subdomains with CNAME records to third-party services (e.g., hosted.statuspage.io) where no page is configured. Accessing the subdomain reveals an unclaimed status, enabling anyone to register and hijack it. This exposes the domain to phishing or malware hosting under a trusted name, exploiting trust in the parent domain.

## Requirements

1. Access to DNS resolution tools
2. Internet connectivity to query public DNS and access web endpoints
3. Basic knowledge of HTTP responses and DNS records

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using automated tools like dnsdumpster or subjack
- Monitor third-party service dashboards for unclaimed pages linked to your domains
- Implement DNSSEC and strict subdomain policies to prevent hijacks

## Objectives

1. Enumerate and verify DNS misconfigurations pointing to unclaimed resources
2. Assess potential for subdomain control and associated risks
3. Document proof-of-concept for reporting or remediation

## Instructions

### Step 1: Perform DNS CNAME Lookup

**Context**: Query the target's DNS to identify if the subdomain points to an external service.

**Command** ([[commands/dig-cname-lookup]]):
```bash
dig status.vimeo.com CNAME
```

> This command resolves the CNAME record. Expected output includes "status.vimeo.com. 300 IN CNAME hosted.statuspage.io." indicating a pointer to an external host.

### Step 2: Access and Inspect Subdomain

**Context**: Visit the subdomain to check for unclaimed status, confirming takeover potential.

**Command** (using curl for HTTP head):
```bash
curl -I http://status.vimeo.com
```

> Look for a 200 OK with content suggesting an unclaimed page, such as redirects to statuspage.io claim interface. Successful output shows headers without custom Vimeo content.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used

- [[commands/dig-cname-lookup]]

## Tools Used


## Tags

- [[subdomain-takeover]]
- [[DNS]]
- [[Reconnaissance]]
