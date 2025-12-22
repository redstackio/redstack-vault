---
tags:
  - reconnaissance
  - subdomain-enumeration
type: procedure
tools:
  - '[[tools/Subfinder]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/subfinder-enumerate-subdomains]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:39:09.427Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 9a485be6-36ce-4cbd-b826-0b9dbbe12185
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Enumerate Subdomains with Subfinder

## Summary

This procedure uses the Subfinder tool to passively and actively enumerate subdomains of a target domain, providing an initial reconnaissance step for identifying potential vulnerabilities like subdomain takeovers.

## Description

In the context of subdomain takeover attacks, enumerating subdomains reveals hidden or forgotten records that may point to deprovisioned services. Subfinder leverages sources like Certificate Transparency logs, search engines, and DNS bruteforcing to compile a comprehensive list. This is crucial for targets like consensys.net where subdomains such as www.codefi.consensys.net may be dangling.

## Requirements

1. Installed Subfinder tool
2. Internet access for querying public sources
3. Target domain name (e.g., consensys.net)

## Defense

Defensive measures and detection strategies:

- Monitor DNS queries for unusual subdomain enumerations using tools like DNS firewall
- Regularly audit and clean up unused subdomains with automated DNS scanners
- Implement certificate transparency monitoring to detect unauthorized subdomain usage

## Objectives

1. Compile a list of all resolvable subdomains
2. Identify potential entry points for further exploitation
3. Enable mapping of the attack surface

## Instructions

### Step 1: Run Subdomain Enumeration

**Context**: Initiate the scan to discover subdomains using multiple sources.

**Command** ([[commands/subfinder-enumerate-subdomains]]):
```bash
subfinder -d consensys.net -o subdomains.txt
```

> This command queries passive sources and outputs unique subdomains to subdomains.txt. Expected output includes lines like "www.codefi.consensys.net".

### Step 2: Review Output

**Context**: Inspect the generated file for relevant subdomains.

No command needed; manually review subdomains.txt for targets to probe further.

> Look for subdomains that might be legacy or unused.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques


## Commands Used

- [[commands/subfinder-enumerate-subdomains]]

## Tools Used

- [[tools/Subfinder]]

## Tags

- [[Reconnaissance]]
- [[subdomain-enumeration]]
