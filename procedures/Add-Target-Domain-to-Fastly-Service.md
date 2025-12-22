---
id: p-add-target-domain-fastly
tags:
  - domain-takeover
  - subdomain-claim
type: procedure
tools:
  - '[[tools/Fastly-Management-Dashboard]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Compromise Infrastructure]]'
updated_at: '2025-12-14T04:51:10.675Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Compromise Infrastructure]]'
---
# Add-Target-Domain-to-Fastly-Service

## Summary

This procedure details adding the vulnerable domain to a Fastly service, triggering automatic TLS provisioning and effectively taking over the subdomain.

## Description

By adding 'gl-canary.global.ssl.fastly.net' to a service, Fastly's system provisions 'gl-canary.freetls.fastly.net' under the free TLS umbrella. Since this subdomain is hardcoded in GitLab's CSP whitelist, the attacker now controls a trusted domain. This misconfiguration allows serving arbitrary content, bypassing CSP to load scripts. The process is instantaneous upon domain addition. Expected outcome: Subdomain under attacker control, verifiable via DNS resolution.

## Requirements

1. Existing Fastly service
2. Knowledge of the target subdomain pattern
3. Dashboard access for domain management

## Defense

Defensive measures and detection strategies:

- Remove or rotate whitelisted domains in CSP that use public CDN free tiers
- Use DNS monitoring services to detect unauthorized claims on subdomains
- Implement certificate transparency logs to alert on new TLS issuances for sensitive domains

## Objectives

1. Attach the takeover target to the service
2. Provision TLS for the subdomain
3. Achieve control over CSP-trusted resources

## Instructions

### Step 1: Enter Domain Section

**Context**: Locate the domain addition interface.

In the service settings, navigate to the 'Domains' or 'Origins' tab.

### Step 2: Add and Provision

**Context**: Input the target and let Fastly handle TLS.

Enter 'gl-canary.global.ssl.fastly.net' as the domain and save. Fastly will auto-provision the freetls variant.

**Expected Output**: Domain listed as active with TLS status 'provisioned'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Compromise Infrastructure]] Compromise Infrastructure

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Fastly-Management-Dashboard]]

## Tags

- [[domain-takeover]]
- [[subdomain-claim]]
