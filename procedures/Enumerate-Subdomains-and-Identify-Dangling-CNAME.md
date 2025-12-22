---
id: proc-enum-dangling-cname
tags:
  - dns-enumeration
  - subdomain
  - cname
type: procedure
tools:
  - '[[tools/subfinder]]'
  - '[[tools/dig]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/subfinder-enumerate]]'
  - '[[commands/dig-cname-query]]'
verified: false
platforms:
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T05:32:24.087Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques:
  - '[[Hardware]]'
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Enumerate Subdomains and Identify Dangling CNAME

## Summary

This procedure involves scanning a target domain for subdomains and querying their DNS records to identify dangling CNAME entries pointing to abandoned external services, such as unclaimed Zendesk instances, which can lead to subdomain takeover vulnerabilities.

## Description

In the context of the easycontactnow.com vulnerability, attackers perform DNS enumeration to uncover subdomains like support.easycontactnow.com. A dangling CNAME points to a now-abandoned Zendesk service, allowing potential hijacking. This reconnaissance step is crucial for mapping the attack surface and spotting misconfigurations without direct interaction with the target.

## Requirements

1. Access to public DNS resolvers
2. Installation of subdomain enumeration tools like subfinder
3. Basic knowledge of DNS record types (CNAME)

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling entries using automated tools like dnsrecon
- Monitor for unexpected CNAME changes via DNS logging
- Implement subdomain validation before pointing to third-party services

## Objectives

1. Generate a comprehensive list of subdomains
2. Identify CNAME records linked to external, potentially abandoned services
3. Flag high-risk configurations for further verification

## Instructions

### Step 1: Enumerate Subdomains

**Context**: Use passive and active enumeration to discover all subdomains associated with the target domain.

**Command** ([[commands/subfinder-enumerate]]):
```bash
subfinder -d easycontactnow.com -all -o subdomains.txt
```

> This command queries multiple sources (e.g., certificate transparency logs, search engines) to compile a list of subdomains. Expected output: A file subdomains.txt with entries like support.easycontactnow.com.

### Step 2: Query for CNAME Records

**Context**: For each subdomain, perform a DNS lookup to extract CNAME records and identify pointers to services like Zendesk.

**Command** ([[commands/dig-cname-query]]):
```bash
dig +short CNAME support.easycontactnow.com
```

> This queries the DNS for the CNAME of the specific subdomain. Expected output: Something like "censored.zendesk.com." indicating a potential dangling record.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- [[Hardware]] Domains

## Commands Used

- [[commands/subfinder-enumerate]]
- [[commands/dig-cname-query]]

## Tools Used

- [[tools/subfinder]]
- [[tools/dig]]

## Tags

- [[dns-enumeration]]
- [[subdomain-discovery]]
