---
id: proc-uuid-1
tags:
  - subdomain-enumeration
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:51:26.701Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Examine-Subdomains-for-Hosting-Services

## Summary

This procedure involves enumerating subdomains of a target domain to identify those hosted on third-party services like Desk.com, which may be vulnerable to takeover if accounts are expired.

## Description

In the context of subdomain takeover attacks, attackers first map the attack surface by discovering all subdomains. Tools or manual inspection reveal hosting on services such as Desk.com. For cloudup.com, help.cloudup.com was found pointing to Desk.com, setting up potential exploitation if the service account lapsed without DNS cleanup.

## Requirements

1. Public access to the target's DNS
2. Basic knowledge of subdomain enumeration techniques
3. Internet connectivity for queries

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs
- Monitor third-party service accounts for expiration and remove associated DNS entries
- Use automated tools like dnsdumpster or subfinder for internal recon

## Objectives

1. Discover subdomains hosted externally
2. Identify potential takeover candidates
3. Map third-party dependencies

## Instructions

### Step 1: Enumerate Subdomains

**Context**: Use online tools or scripts to list subdomains of the target, such as cloudup.com.

No specific command here; manual review or tools like Sublist3r can be used to identify help.cloudup.com as Desk.com hosted.

### Step 2: Check Hosting Service

**Context**: Inspect identified subdomains for external hosting indicators.

Review outputs to note Desk.com references.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-enumeration]]
- [[Reconnaissance]]
