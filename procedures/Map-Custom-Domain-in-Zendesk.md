---
id: proc-uuid-3
tags:
  - zendesk
  - domain-mapping
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:23.598Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Map Custom Domain in Zendesk

## Summary

This procedure maps an external vulnerable subdomain to a Zendesk instance, redirecting traffic to attacker-controlled content.

## Description

Once a Zendesk account is claimed, add the original subdomain (e.g., help.tictail.com) as a custom host mapping. This exploits the dangling CNAME to route traffic through Zendesk, enabling impersonation in web environments.

## Requirements

1. Active Zendesk trial account with claimed subdomain
2. Admin access to Zendesk settings
3. Target subdomain's DNS pointing to the service

## Defense

Defensive measures and detection strategies:

- Validate and monitor custom domain mappings in SaaS platforms
- Use DNSSEC to prevent unauthorized CNAME exploits
- Scan for unexpected traffic to subdomains

## Objectives

1. Redirect subdomain traffic to controlled Zendesk
2. Enable full takeover of the domain
3. Avoid default subdomain exposure

## Instructions

### Step 1: Access Host Mapping Settings

**Context**: Log in and navigate to domain configuration.

In Zendesk admin, go to Settings > Account > Host mapping.

> Expected: Interface for adding custom domains.

### Step 2: Add Custom Domain

**Context**: Input and save the vulnerable subdomain.

Add 'help.tictail.com' as the custom domain and save.

> Expected: Domain added without errors, traffic now routes via Zendesk.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[zendesk]]
- [[domain-mapping]]
- [[subdomain-takeover]]
