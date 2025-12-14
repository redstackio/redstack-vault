---
tags:
  - reconnaissance
  - subdomains
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - DNS
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:51:10.740Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 1158c6fb-5447-4087-9802-1701b45cec42
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Enumerate-Target-Subdomains

## Summary

This procedure involves manually or systematically enumerating subdomains of a target domain like slack-core.com to identify potential vulnerabilities in infrastructure such as podcast or call services.

## Description

In the context of subdomain takeover attacks, enumeration helps uncover subdomains that may have misconfigured DNS records. For Slack's infrastructure, focusing on domains used for non-core services like podcasts reveals opportunities for dangling records. The target environment includes public DNS resolvers and web services on port 80.

## Requirements

1. Access to DNS enumeration tools or manual research
2. Knowledge of target infrastructure (e.g., slack-core.com for Slack services)
3. Network connectivity for subdomain queries

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using tools like dnsdumpster or internal scanners
- Implement monitoring for third-party service claims on custom domains
- Use DNSSEC to prevent unauthorized takeovers

## Objectives

1. Discover subdomains associated with third-party services
2. Identify potential misconfigurations
3. Map the attack surface for further exploitation

## Instructions

### Step 1: Research Target Infrastructure

**Context**: Identify domains like slack-core.com used for ancillary services such as calls or podcasts.

No specific command; perform manual reconnaissance via public sources or prior knowledge.

> Expected: Noted usage for podcast infrastructure.

### Step 2: List Potential Subdomains

**Context**: Generate a list of subdomains to investigate, focusing on podcast-related ones.

No command; use tools like Sublist3r or manual checks if available.

> Expected: Subdomains like podcasts.slack-core.com identified.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[subdomains]]
