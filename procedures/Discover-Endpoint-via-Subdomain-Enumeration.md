---
id: p-discover-endpoint-subdomain
tags:
  - recon
  - subdomain-enum
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
updated_at: '2025-12-14T03:15:10.326Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Discover Endpoint via Subdomain Enumeration

## Summary

This procedure involves enumerating subdomains of a target to uncover hidden web services, such as an XML-processing endpoint mistaken for a file upload form in a Microsoft Dynamics AX integration.

## Description

In the attack on the Starbucks web service, subdomain enumeration revealed an endpoint that initially appeared as a simple HTML file upload but processed XML for enterprise accounting. This step expands the attack surface by identifying non-obvious services. Prerequisites include public access to the target domain and basic reconnaissance tools.

## Requirements

1. Network access to target domain
2. Recon tools like subfinder or Amass
3. No credentials needed

## Defense

Defensive measures and detection strategies:

- Implement DNS logging to detect enumeration patterns
- Use certificate transparency logs to monitor subdomains

## Objectives

1. Identify hidden endpoints
2. Map attack surface
3. Discover XML-processing services

## Instructions

### Step 1: Enumerate Subdomains

**Context**: Use passive and active DNS enumeration to list all subdomains.

**Command** ([[commands/subfinder-enumerate]]):
```bash
subfinder -d starbucks.com -o subdomains.txt
```

> This command queries multiple sources for subdomains and outputs to a file. Expected output: A list of subdomains including the vulnerable one.

### Step 2: Probe for Live Hosts

**Context**: Verify which subdomains are active and accessible.

**Command** ([[commands/httpx-probe]]):
```bash
cat subdomains.txt | httpx -o alive.txt
```

> Probes HTTP/HTTPS on subdomains; expected output: List of live endpoints with status codes.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used

- [[commands/subfinder-enumerate]]
- [[commands/httpx-probe]]

## Tools Used


## Tags

- recon
- subdomain
