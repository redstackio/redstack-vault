---
tags:
  - subdomain-enumeration
  - reconnaissance
  - dns
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
updated_at: '2025-12-14T04:39:02.025Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: e9d32c80-371f-48cf-a616-e16a32fc75b6
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Enumerate Subdomains of Target Domain

## Summary

This procedure discovers subdomains associated with a target domain like starbucks.com using passive and active DNS enumeration techniques, identifying potential attack surfaces such as datacafe-cert.starbucks.com.

## Description

In a subdomain takeover attack, the first step is to map the target's DNS footprint. This involves querying public DNS resolvers and using wordlists or brute-forcing to uncover hidden subdomains. The goal is to find subdomains that may have misconfigurations, like dangling CNAMEs. This procedure assumes access to standard DNS tools and focuses on efficiency to avoid rate-limiting.

## Requirements

1. Internet access for DNS queries
2. DNS resolution tools installed (e.g., dig or online services)
3. Target domain name (e.g., starbucks.com)

## Defense

Defensive measures and detection strategies:

- Monitor DNS logs for unusual enumeration queries
- Use DNS security extensions (DNSSEC) to validate records
- Regularly audit subdomain registrations

## Objectives

1. Compile a comprehensive list of subdomains
2. Identify active and potentially vulnerable ones
3. Prepare for further DNS analysis

## Instructions

### Step 1: Passive Subdomain Discovery

**Context**: Use certificate transparency logs or public databases to passively gather subdomains without direct queries to the target.

**Command** (Manual or tool-based query):

No specific command; use services like crt.sh or SecurityTrails API to search for *.starbucks.com.

> This yields subdomains like datacafe-cert.starbucks.com without alerting the target.

### Step 2: Active Brute-Force Enumeration

**Context**: Brute-force common subdomain names against the target to uncover more entries.

**Command** (Using a tool like dnsrecon):

```bash
dnsrecon -d starbucks.com -t brt -D /path/to/wordlist.txt
```

> Outputs discovered subdomains; filter for unique entries.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- None

## Commands Used

- None specific

## Tools Used

- None specific

## Tags

- [[subdomain-enumeration]]
- [[Reconnaissance]]
