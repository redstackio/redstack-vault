---
id: proc-uuid-1
tags:
  - subdomain-enumeration
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-dns-lookup]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:51:10.839Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Identify-Vulnerable-Event-Subdomains

## Summary

This procedure involves enumerating and identifying subdomains associated with target events that may be vulnerable to takeover due to legacy or abandoned infrastructure, such as Khan Academy's hackathon and hackweek subdomains.

## Description

In scenarios where organizations host temporary event sites on cloud services, subdomains like healthyhackathon.khanacademy.org may persist in DNS after decommissioning. This step focuses on manual or tool-assisted discovery of such subdomains to build the attack surface map. The target environment is public web domains with potential cloud backends. Expected outcomes include a list of candidate subdomains for further probing.

## Requirements

1. Access to public DNS resolvers
2. Knowledge of target events (e.g., via web searches for 'Khan Academy hackathon')
3. Basic networking tools like dig or nslookup

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for orphaned entries
- Implement DNS monitoring tools like DNSSec or anomaly detection
- Use subdomain management tools to track and expire event subdomains

## Objectives

1. Discover event-related subdomains
2. Confirm their existence via DNS resolution
3. Prioritize those likely tied to cloud services

## Instructions

### Step 1: Research Target Events

**Context**: Gather intelligence on past events to hypothesize subdomain names.

Search for events like 'healthy hackathon Khan Academy' to identify subdomains such as healthyhackathon.khanacademy.org and hackweek.khanacademy.org.

### Step 2: Enumerate Subdomains

**Context**: Verify subdomain existence using DNS queries.

**Command** ([[commands/dig-dns-lookup]]):
```bash
 dig healthyhackathon.khanacademy.org
```

> This command queries DNS for the subdomain, returning A or CNAME records if it exists. Expected output includes IP addresses or CNAMEs confirming the subdomain is active in DNS.

Repeat for hackweek.khanacademy.org.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-lookup]]

## Tools Used


## Tags

- [[subdomain-enumeration]]
- [[Reconnaissance]]
