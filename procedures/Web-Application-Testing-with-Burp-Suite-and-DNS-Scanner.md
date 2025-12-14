---
id: proc-burp-dns-zomato
tags:
  - web-testing
  - dns-enum
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/DNS-scanner]]'
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
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T03:46:32.266Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Web-Application-Testing-with-Burp-Suite-and-DNS-Scanner

## Summary

Intercept web traffic with Burp Suite and scan DNS for issues on Zomato targets, though results may not yield vulnerabilities.

## Description

Burp Suite proxies HTTP requests to test for web vulns, combined with DNS scanning for record enumeration. In this case, efforts on Zomato were not fruitful but part of standard recon.

## Requirements

1. Burp Suite running as proxy
2. Browser configured to use proxy
3. DNS scanner tool like dnsenum

## Defense

- Use WAF to block anomalous requests
- Secure DNS with DNSSEC

## Objectives

1. Intercept and analyze traffic
2. Enumerate DNS records
3. Identify config issues

## Instructions

### Step 1: Intercept Traffic

**Context**: Set up Burp to capture requests to target.

No specific command; configure proxy in browser.

### Step 2: Run DNS Scan

**Context**: Enumerate DNS for subdomains.

**Command** ([[commands/dns-scan-enum]]):
```bash
dnsenum zomato.com
```

> Outputs DNS records; limited results expected.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Active Scanning: Vulnerability Scanning

### Sub-Techniques


## Commands Used

- [[commands/dns-scan-enum]]

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/DNS-scanner]]

## Tags

- [[web-testing]]
- [[dns-enum]]
