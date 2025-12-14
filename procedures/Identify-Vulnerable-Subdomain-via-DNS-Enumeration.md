---
id: proc-uuid-1
tags:
  - dns-enumeration
  - subdomain-takeover
  - recon
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/nslookup-cname-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:51:26.634Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Identify-Vulnerable-Subdomain-via-DNS-Enumeration

## Summary

This procedure enumerates DNS records to identify vulnerable subdomains with dangling CNAMEs pointing to unclaimed third-party services like Netlify, setting the stage for subdomain takeover attacks.

## Description

In this attack scenario, attackers scan for subdomains on the target domain (e.g., a DoD site) to find CNAME records that point to unused resources on platforms like Netlify. An unclaimed record allows anyone to register and control the subdomain, leading to risks such as serving malicious content under the trusted domain. The target environment is public DNS with web services; prerequisites include access to DNS query tools and knowledge of common takeover services.

## Requirements

1. Network access to public DNS resolvers
2. Tools for DNS enumeration (e.g., nslookup or dig)
3. List of target domains or subdomains to query

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using automated scanners like dnsdumpster or subjack
- Implement DNS monitoring for changes and claim all referenced third-party resources
- Use strict Host header validation on web servers to prevent injection

## Objectives

1. Discover unclaimed CNAME records for takeover potential
2. Verify the absence of active content on pointed endpoints
3. Assess risk to domain reputation and security

## Instructions

### Step 1: Query DNS for CNAME Records

**Context**: Start by enumerating the target's DNS to find subdomains with CNAMEs pointing to external services.

**Command** ([[commands/nslookup-cname-query]]):
```bash
nslookup -type=CNAME www.target.gov
```

> This command queries the CNAME record for the subdomain. Expected output includes the target like "www.target.gov canonical name = example.netlify.app." If unclaimed, proceed to verification.

### Step 2: Verify Unclaimed Status

**Context**: Check if the Netlify endpoint is active or claimable by attempting direct access.

**Command** ([[commands/curl-direct-access]]):
```bash
curl -sk https://example.netlify.app
```

> This sends a request to the Netlify URL. Expected output: 404 or empty response indicating unclaimed status, confirming takeover vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used

- [[commands/nslookup-cname-query]]
- [[commands/curl-direct-access]]

## Tools Used

- [[tools/curl]]

## Tags

- [[dns-enumeration]]
- [[subdomain-takeover]]
