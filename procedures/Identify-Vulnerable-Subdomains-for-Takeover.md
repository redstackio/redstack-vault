---
tags:
  - subdomain-enumeration
  - dns-recon
  - takeover
type: procedure
tools:
  - '[[tools/Subjack]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/subfinder-enumerate]]'
  - '[[commands/subjack-check]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:38:49.510Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: edcb7582-9439-4a1a-801d-bdf5af09fec9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Vulnerable Subdomains for Takeover

## Summary

This procedure enumerates target subdomains and identifies those vulnerable to takeover due to unclaimed cloud instances, such as dangling CNAME records pointing to unused services like AWS Route 53 or Heroku.

## Description

In scenarios like the Starbucks report, attackers scan for subdomains (e.g., germany.openapi.starbucks.com) with weak DNS configurations allowing external claiming. The process involves passive reconnaissance to list subdomains, followed by fingerprinting to detect takeover opportunities. Prerequisites include public DNS access; outcomes enable initial access via domain control without authentication.

## Requirements

1. Internet access for DNS queries
2. Installed tools like Subfinder and Subjack
3. Target domain knowledge (e.g., starbucks.com)

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs
- Implement subdomain monitoring tools like DNSSEC or certificate transparency logs
- Use automated scanners to detect unclaimed services

## Objectives

1. Discover all subdomains of the target
2. Identify those with takeover fingerprints
3. Validate vulnerability without claiming

## Instructions

### Step 1: Enumerate Subdomains

**Context**: Use passive sources to list potential subdomains without alerting the target.

**Command** ([[commands/subfinder-enumerate]]):
```bash
subfinder -d starbucks.com -all -o subdomains.txt
```

> This command queries multiple passive sources to output a list of subdomains to subdomains.txt. Expected output: A file with entries like api.starbucks.com, openapi.starbucks.com.

### Step 2: Check for Takeover Vulnerabilities

**Context**: Scan enumerated subdomains for known takeover patterns in cloud services.

**Command** ([[commands/subjack-check]]):
```bash
subjack -w subdomains.txt -t 100 -o takeovers.txt -v
```

> This runs Subjack to fingerprint subdomains, outputting vulnerable ones to takeovers.txt. Expected output: Matches like 'germany.openapi.starbucks.com - AWS S3 Unclaimed'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/subfinder-enumerate]]
- [[commands/subjack-check]]

## Tools Used

- [[tools/Subjack]]

## Tags

- [[subdomain-takeover]]
- [[dns-enumeration]]
