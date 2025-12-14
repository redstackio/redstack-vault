---
id: proc-uuid-001
name: Discover-Dangling-DNS-Records-for-Subdomain-Takeover
tags:
  - dns-reconnaissance
  - subdomain-takeover
  - fastly
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-query-dns]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Determine Physical Locations]]'
updated_at: '2025-12-14T05:32:23.691Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Determine Physical Locations]]'
---
# Discover-Dangling-DNS-Records-for-Subdomain-Takeover

## Summary

This procedure involves enumerating DNS records of a target domain to identify subdomains with dangling references to unconfigured cloud services, such as Fastly, which could allow an attacker to claim the subdomain and perform a takeover for phishing, defacement, or further attacks.

## Description

In this scenario, reconnaissance reveals a DNS record for production.s3.rubygems.org pointing to Fastly infrastructure without an active service configured. Although RubyGems controls the domain preventing external takeover, the dangling record poses a risk if control lapses or provider bugs emerge. The procedure uses DNS queries to detect such misconfigurations, followed by validation via HTTP probes to confirm the absence of service. Prerequisites include public DNS access; outcomes include vulnerability reports for remediation, like removing the record.

## Requirements

1. Internet access for DNS queries.
2. DNS resolution tools installed (e.g., dig on Linux/macOS).
3. Target domain with publicly queryable DNS (e.g., rubygems.org).

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling entries using automated tools like DNSdumpster or custom scripts.
- Implement domain shadowing prevention by verifying all cloud service configurations match DNS.
- Monitor for anomalous HTTP responses on subdomains (e.g., provider error pages) via WAF logs.

## Objectives

1. Identify subdomains with unresolved cloud provider pointers.
2. Validate lack of service configuration to assess takeover risk.
3. Report findings to prevent exploitation.

## Instructions

### Step 1: Enumerate DNS Records

**Context**: Query the target subdomain's DNS to retrieve A, CNAME, or other records pointing to cloud providers.

**Command** ([[commands/dig-query-dns]]):
```bash
dig +short production.s3.rubygems.org
```

> This command resolves the subdomain and outputs IPs or CNAMEs. Look for Fastly-related responses (e.g., global.prod.fastly.net). Expected output: A list of IPs or CNAMEs indicating Fastly infrastructure.

### Step 2: Validate Service Configuration

**Context**: Access the subdomain via HTTP to check for provider-specific error pages indicating no active service.

**Command** ([[commands/curl-http-probe]]):
```bash
curl -I http://production.s3.rubygems.org/
```

> This sends a HEAD request and checks headers. Expected output: HTTP 404 or Fastly's "No service configured" message, confirming the dangling status.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Determine Physical Locations]]

### Sub-Techniques


## Commands Used

- [[commands/dig-query-dns]]
- [[commands/curl-http-probe]]

## Tools Used


## Tags

- [[dns-reconnaissance]]
- [[subdomain-takeover]]
