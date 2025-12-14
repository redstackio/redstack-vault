---
id: proc-uuid-recon-subdomains
tags:
  - reconnaissance
  - subdomains
  - manifest
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
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:26:17.693Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Reconnaissance-on-Out-of-Scope-Subdomains

## Summary

This procedure involves scanning and examining out-of-scope subdomains of a target domain to uncover hidden resources, such as manifest files that reference vulnerable components like outdated SWF files.

## Description

In the context of web vulnerability hunting, reconnaissance on subdomains helps map the attack surface beyond the main domain. By accessing and parsing files like motd2.manifest on subdomains (e.g., templ4d2.pinion.gg), attackers can identify embedded assets vulnerable to exploitation, such as Flash SWF files. This step requires no special tools beyond a web browser or basic HTTP client, but focuses on manual inspection for efficiency in bug bounty scenarios.

## Requirements

1. Public access to target domain subdomains (e.g., pinion.gg)
2. Web browser or HTTP client like curl
3. Knowledge of common file types (e.g., .manifest)

## Defense

Defensive measures and detection strategies:

- Implement subdomain takeover prevention and monitoring
- Use web application firewalls (WAF) to log unusual manifest accesses
- Regularly audit out-of-scope assets for exposure

## Objectives

1. Identify resources on subdomains for vulnerability scouting
2. Locate references to potentially outdated components
3. Build a list of endpoints for further testing

## Instructions

### Step 1: Enumerate and Access Subdomains

**Context**: Manually or semi-automatically discover subdomains and access key files to inspect contents.

Browse to http://templ4d2.pinion.gg/motd2.manifest and download the file.

> Parse the manifest for SWF references, such as http://bin.pinion.gg/bin/flowplayer.commercial-3.2.15.swf.

### Step 2: Document Findings

**Context**: Note all relevant resources for the next steps in the chain.

Record URLs and versions observed.

> Expected: List of assets like SWF files ready for vulnerability checks.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[subdomains]]
