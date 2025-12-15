---
id: proc-uuid-003
tags:
  - subdomain-enumeration
  - bruteforce
type: procedure
tools:
  - '[[tools/gobuster]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:24:44.658Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Perform-Subdomain-Bruteforce-on-Target-Domain

## Summary

This procedure uses DNS bruteforcing to discover hidden subdomains of a target domain, identifying those where specific credentials may apply, such as development environments.

## Description

Subdomain enumeration expands the attack surface by revealing non-public endpoints. In this case, bruteforcing zomato.com uncovered a subdomain where hardcoded creds from the app granted access to an admin panel clone. Tools query DNS for common subdomain names, filtering for HTTP-responsive ones that match the credential context (e.g., initial 503 errors).

## Requirements

1. Target domain (e.g., zomato.com)
2. Wordlist of common subdomains (e.g., SecLists)
3. DNS resolution access (no firewall blocks)
4. Brute-force tool like gobuster

## Defense

Defensive measures and detection strategies:

- Implement DNS rate limiting and monitoring for enumeration queries
- Use wildcard DNS sparingly; certificate transparency logs for subdomain discovery
- Regularly audit and remove unused subdomains

## Objectives

1. Discover non-obvious subdomains
2. Identify auth-protected endpoints
3. Enable credential testing on findings

## Instructions

### Step 1: Prepare Wordlist

**Context**: Gather subdomain names for bruteforcing.

Download a standard wordlist focused on dev/admin terms.

### Step 2: Run DNS Bruteforce

**Context**: Enumerate subdomains via DNS queries.

Use gobuster in DNS mode against the target.

**Command** (gobuster-dns):
```bash
gobuster dns -d zomato.com -w subdomains.txt -t 50 -o results.txt
```

> This outputs discovered subdomains like 'dev-admin.zomato.com'. Filter for those returning 503 on initial probes.

### Step 3: Probe for HTTP Response

**Context**: Test subdomains for web presence.

Use curl to check HTTP status.

**Command** (curl-probe):
```bash
curl -I http://suspected-subdomain.zomato.com/
```

> Look for 401/503 indicating auth requirement.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domain

### Sub-Techniques

- None

## Commands Used

- None specific

## Tools Used

- [[tools/gobuster]]

## Tags

- [[subdomain-enumeration]]
- [[bruteforce]]
