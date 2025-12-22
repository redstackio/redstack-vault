---
id: proc-sub-port-zomato
tags:
  - port-scan
  - subdomain
type: procedure
tools:
  - '[[tools/nmap]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/nmap-port-scan]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:46:32.252Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Subdomain-and-Port-Information-Discovery

## Summary

Discover subdomains like auth.zomato.com and confirm ports (e.g., 443 TCP) for brute-force potential.

## Description

Brute-force and scan specific subdomains to identify exposed services on standard HTTPS ports.

## Requirements

1. Subdomain list
2. nmap for port confirmation

## Defense

- Close unnecessary ports
- Implement brute-force protection

## Objectives

1. Confirm subdomain services
2. Assess brute-force risks
3. Map port exposures

## Instructions

### Step 1: Scan Port on Subdomain

**Context**: Target auth.zomato.com port 443.

**Command** ([[commands/nmap-port-scan]]):
```bash
nmap -p 443 auth.zomato.com
```

> Confirms open HTTPS service, brute-forcible.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/nmap-port-scan]]

## Tools Used

- [[tools/nmap]]

## Tags

- [[port-scan]]
- [[subdomain]]
