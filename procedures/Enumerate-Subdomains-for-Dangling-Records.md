---
tags:
  - subdomain-enumeration
  - reconnaissance
  - dns
type: procedure
tools:
  - '[[tools/c99-Subdomain-Finder]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:51:10.507Z'
sub_techniques: []
id: 367e573c-2661-4a82-94f7-d20196ef9852
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Enumerate Subdomains for Dangling Records

## Summary

This procedure uses online tools to scan a target domain for subdomains, identifying those with dangling or unclaimed DNS records that point to third-party verification services, such as Squarespace, enabling potential subdomain takeovers.

## Description

In a subdomain takeover attack, the first step is reconnaissance to discover unused subdomains with outdated DNS entries. For Imgur, scanning revealed '8ybhy85kld9zp9xf84x6.imgur.com' with a CNAME to verify.squarespace.com from an old verification process. This procedure outlines using a web-based scanner to enumerate and flag such vulnerabilities, targeting web and DNS environments without requiring authentication.

## Requirements

1. Internet access to online scanning tools
2. Target domain (e.g., imgur.com)
3. Basic understanding of DNS records

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using tools like dnsdumpster or internal scanners
- Implement automated subdomain monitoring and cleanup policies
- Use DNS security extensions (DNSSEC) to prevent unauthorized claims

## Objectives

1. Discover all subdomains of the target
2. Identify dangling records vulnerable to takeover
3. Gather evidence for reporting or exploitation

## Instructions

### Step 1: Access Subdomain Scanner

**Context**: Launch a web-based tool to enumerate subdomains without installing software.

**Command** (No CLI; web UI):

Visit https://subdomainfinder.c99.nl/ and enter the target domain.

> The tool queries public sources for subdomains and displays results, including DNS details.

### Step 2: Analyze Results for Dangling Records

**Context**: Review the output for subdomains with unresolved or third-party CNAMEs.

**Command** (Follow-up DNS check with [[commands/dig-dns-lookup-for-subdomain-resolution]]):

```bash
dig 8ybhy85kld9zp9xf84x6.imgur.com
```

> Expected: CNAME to verify.squarespace.com, indicating a dangling record.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/c99-Subdomain-Finder]]

## Tags

- [[subdomain-enumeration]]
- [[Reconnaissance]]
