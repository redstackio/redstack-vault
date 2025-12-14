---
id: proc-dns-enum-dangling-001
tags:
  - dns-enumeration
  - subdomain-takeover
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:38:39.696Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Identify Dangling Subdomain via DNS Enumeration

## Summary

This procedure involves querying DNS records to identify subdomains with dangling CNAMEs pointing to unclaimed cloud services like AWS CloudFront, setting the stage for subdomain takeover attacks.

## Description

In scenarios where organizations decommission services without removing DNS records, subdomains may point to unused cloud resources. This procedure uses DNS enumeration to detect such misconfigurations, specifically targeting CNAME records resolving to inactive CloudFront distributions. The target environment is public DNS infrastructure, with outcomes including identification of takeover candidates for phishing or impersonation.

## Requirements

1. Access to DNS resolution tools (e.g., dig, nslookup)
2. Knowledge of target domain (e.g., ubnt.com)
3. No special privileges; public DNS queries suffice

## Defense

Defensive measures and detection strategies:

- Regularly audit and remove dangling DNS records using tools like DNSdumpster or automated scripts
- Implement domain validation in cloud services (though AWS CloudFront lacks this)
- Monitor for unexpected traffic to subdomains via DNS logs or cloud provider alerts

## Objectives

1. Discover vulnerable subdomains with unclaimed CNAMEs
2. Verify inactivity of pointed resources
3. Prepare for domain claiming

## Instructions

### Step 1: Query CNAME Records

**Context**: Enumerate DNS records for potential subdomains to find CNAMEs pointing to cloud services.

Use dig to query:

```bash
dig CNAME partners.ubnt.com
```

> This command resolves the CNAME and shows if it points to a CloudFront endpoint like d123456789.cloudfront.net.

### Step 2: Verify Inactivity

**Context**: Confirm the CloudFront distribution is unclaimed by accessing it directly.

Visit the resolved CloudFront URL in a browser or use curl:

```bash
curl -I https://d123456789.cloudfront.net
```

> Expect a 403 Forbidden or no content, indicating no active origin.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[dns-enumeration]]
- [[subdomain-takeover]]
