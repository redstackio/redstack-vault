---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Enumerate-Subdomains-for-Takeover
tags:
  - subdomain-enumeration
  - reconnaissance
  - dns
type: procedure
tools:
  - '[[tools/Subfinder]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/subfinder-enumerate]]'
  - '[[commands/grep-heroku-pattern]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:30:18.258Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Enumerate-Subdomains-for-Takeover

## Summary

This procedure uses passive and active DNS enumeration to identify subdomains of a target domain that may point to third-party cloud services, focusing on those vulnerable to takeover such as dangling Heroku records.

## Description

In the context of subdomain takeover attacks, enumeration reveals misconfigurations where DNS records point to deleted cloud apps. For Uber, this uncovered a subdomain like 'dangling.uber.com' CNAME to a deleted Heroku app. Prerequisites include a Linux environment with DNS tools installed and public access to the target's DNS.

## Requirements

1. Network access to perform DNS queries
2. Installed tools like Subfinder and grep
3. Target domain resolved publicly

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using tools like dnsrecon
- Implement DNS monitoring with services like Cloudflare or Route 53 alerts
- Use subdomain takeover scanners like subjack in CI/CD pipelines

## Objectives

1. Discover all subdomains associated with the target
2. Identify cloud-provider specific subdomains (e.g., Heroku, AWS S3)
3. Flag potential takeover candidates for further verification

## Instructions

### Step 1: Run Subdomain Enumeration

**Context**: Use Subfinder to gather subdomains from multiple sources including passive DNS databases.

**Command** ([[commands/subfinder-enumerate]]):
```bash
subfinder -d uber.com -all -o subdomains.txt
```

> This command queries APIs and passive sources to output a list of subdomains to subdomains.txt. Expected output: A file with entries like 'api.uber.com', 'dangling.uber.com'.

### Step 2: Filter for Cloud Patterns

**Context**: Grep the results for known cloud provider patterns to narrow down takeover risks.

**Command** ([[commands/grep-heroku-pattern]]):
```bash
grep -i heroku subdomains.txt > heroku_subs.txt
```

> Filters for Heroku-related subdomains. Expected output: A focused list like 'dangling.uber.com' if vulnerable.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/subfinder-enumerate]]
- [[commands/grep-heroku-pattern]]

## Tools Used

- [[tools/Subfinder]]

## Tags

- [[subdomain-enumeration]]
- [[Reconnaissance]]
