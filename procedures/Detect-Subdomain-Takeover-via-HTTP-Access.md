---
tags:
  - subdomain-takeover
  - http
  - recon
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-http-access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:51:10.602Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: d7779311-b933-4d5b-ac4c-abadf41cda55
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Detect-Subdomain-Takeover-via-HTTP-Access

## Summary

This procedure involves accessing a suspected subdomain via HTTP to detect error responses from cloud providers like Fastly, indicating a dangling record that could be taken over by an attacker.

## Description

In subdomain takeover scenarios, a DNS record points to a third-party service (e.g., Fastly CDN) that is no longer active for that domain. Accessing the URL returns a provider-specific error page, such as Fastly's 'unknown domain' message. This confirms the subdomain is vulnerable to takeover, where an attacker could register the domain on the provider and host arbitrary content, potentially impersonating the parent domain (e.g., shopify.io). The procedure targets public-facing web subdomains and requires no authentication.

## Requirements

1. Internet access to query HTTP endpoints
2. A suspected subdomain (e.g., from prior reconnaissance)
3. Basic tools like curl or a web browser

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling entries using automated tools like dnsdumpster or subjack
- Monitor for provider error pages on subdomains via web scanners
- Implement DNS monitoring alerts for changes or unresolved records

## Objectives

1. Identify unregistered infrastructure via HTTP response
2. Confirm potential for subdomain hijacking
3. Gather evidence for reporting the vulnerability

## Instructions

### Step 1: Access the Subdomain URL

**Context**: Visit or query the subdomain to elicit a provider error, indicating it's not tied to an active service.

**Command** ([[commands/curl-http-access]]):
```bash
curl -i http://genghis-cdn.shopify.io/
```

> This command sends an HTTP HEAD request (or GET with -i for headers) to the target URL. Expected output includes a 404-like error from Fastly: 'Fastly error: unknown domain: genghis-cdn.shopify.io. Please check that this domain has been added to a service.' Success is indicated by the absence of legitimate content and presence of the provider's error template.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: DNS

### Sub-Techniques


## Commands Used

- [[commands/curl-http-access]]

## Tools Used


## Tags

- [[subdomain-takeover]]
- [[http]]
- [[recon]]
