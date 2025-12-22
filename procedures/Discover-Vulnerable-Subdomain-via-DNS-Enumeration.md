---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - dns
  - subdomain-enumeration
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-dns-query]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Scanning IP Blocks]]'
updated_at: '2025-12-14T04:51:26.529Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Scanning IP Blocks]]'
---
# Discover Vulnerable Subdomain via DNS Enumeration

## Summary

This procedure involves enumerating subdomains of a target domain and inspecting their DNS records to identify CNAMEs pointing to unclaimed cloud endpoints, such as outdated Azure services, which can lead to subdomain takeover vulnerabilities.

## Description

In this scenario, a subdomain like vulnerable-sub.dod.gov has a CNAME record pointing to an unclaimed Azure endpoint (█████ --> ████). Attackers scan for such misconfigurations to register the dangling record and hijack the subdomain for malicious purposes. Prerequisites include access to DNS resolution tools and knowledge of common cloud dangling records.

## Requirements

1. Internet access for DNS queries
2. DNS enumeration tools or manual query capabilities
3. Target domain with public DNS records

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using tools like DNSdumpster or Azure AD audit logs
- Implement DNS monitoring for changes and automate alerts on unclaimed targets
- Use subdomain takeover detection services like SecurityTrails or Cloudflare

## Objectives

1. Identify subdomains vulnerable to takeover
2. Extract CNAME targets for further verification
3. Map potential attack surface

## Instructions

### Step 1: Enumerate Subdomains

**Context**: Start by listing potential subdomains using passive sources or brute-forcing.

**Command** ([[commands/dig-dns-query]]):
```bash
dig +short CNAME vulnerable-sub.dod.gov
```

> This queries the CNAME record. Expected output: "█████." indicating an Azure endpoint.

### Step 2: Resolve and Analyze Target

**Context**: Follow the CNAME to check if it's a live or dangling service.

**Command** ([[commands/dig-dns-query]]):
```bash
dig +short vulnerable-sub.dod.gov
```

> Output shows the resolved IP or further CNAME. If it points to an unclaimed domain, proceed to verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Scanning IP Blocks]] Active Scanning: Scanning IP Blocks

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-query]]

## Tools Used


## Tags

- [[DNS]]
- [[subdomain-enumeration]]
