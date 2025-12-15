---
id: proc-burp-dns-testing-927413
tags:
  - web-testing
  - dns-enum
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/DNS-Scanner]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dns-scan-enum]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:27:35.673Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Web-Application-Testing-with-Burp-Suite-and-DNS-Scanner

## Summary

This procedure uses Burp Suite for request interception and a DNS scanner for subdomain enum on Zomato's web apps, though results were limited in this case.

## Description

Burp Suite acts as a proxy to test web vulns, while DNS scanning reveals subdomains. Applied to Zomato, it attempts to uncover web issues but yields non-fruitful results, serving as a foundational step before deeper analysis.

## Requirements

1. Burp Suite installed and configured as proxy
2. Browser with proxy settings
3. Target domain

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS and HSTS to limit interception
- Log anomalous DNS queries

## Objectives

1. Intercept and modify web requests
2. Enumerate DNS records
3. Identify potential web entry points

## Instructions

### Step 1: DNS Enumeration

**Context**: Scan for subdomains using DNS tools.

**Command** ([[commands/dns-scan-enum]]):
```bash
dnsenum zomato.com
```

> Generates list of DNS records and potential subdomains for further testing.

### Step 2: Intercept with Burp

**Context**: Route traffic through Burp to test apps.

Configure browser proxy to 127.0.0.1:8080 and browse zomato.com.

> Burp captures requests; inspect for vulns like XSS/CSRF.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used

- [[commands/dns-scan-enum]]

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/DNS-Scanner]]

## Tags

- [[web-testing]]
- [[dns-enum]]
