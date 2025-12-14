---
id: proc-detect-subdomain-takeover
tags:
  - subdomain-takeover
  - dns
  - cname
  - recon
type: procedure
tools:
  - '[[tools/host]]'
tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
commands:
  - '[[commands/host-dns-lookup]]'
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:24.157Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Hardware]]'
  - '[[Exploit Public-Facing Application]]'
---
# Detect-and-Confirm-Subdomain-Takeover

## Summary

This procedure outlines the steps to detect a subdomain takeover vulnerability by first observing web-based error messages indicative of misconfigured domain mapping and then confirming the issue through DNS resolution, focusing on dangling CNAME records pointing to abandoned services like WordPress.com subdomains.

## Description

Subdomain takeover occurs when a subdomain's DNS records point to a third-party service that is no longer in use or claimed by the owner, allowing an attacker to register the service and gain control over the subdomain. In this scenario, targeting code.wordpress.net, the procedure involves accessing the URL to see a domain mapping error and using DNS tools to trace the CNAME chain to an unclaimed WordPress.com alias. This enables potential impersonation or malicious content hosting. Prerequisites include internet access and basic command-line knowledge; no special privileges are needed.

## Requirements

1. Web browser for initial URL access
2. Command-line environment with DNS resolution tools like 'host'
3. Public internet connectivity to query DNS and access HTTP endpoints

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using automated tools like dnsdumpster or subjack
- Implement domain monitoring services to alert on unclaimed subdomains
- Enforce strict DNS cleanup policies when decommissioning services
- Use certificate transparency logs to monitor subdomain claims

## Objectives

1. Identify signs of subdomain abandonment via web errors
2. Verify misconfiguration through DNS tracing
3. Assess takeover potential for impact evaluation

## Instructions

### Step 1: Access Target Subdomain

**Context**: Navigate to the suspected subdomain to check for error messages signaling unclaimed service mapping.

**Instructions**: Open http://code.wordpress.net in a web browser and note the error.

> This reveals the domain is not properly mapped, pointing to an abandoned setup.

### Step 2: Perform DNS Lookup

**Context**: Use DNS resolution to confirm the CNAME chain and identify dangling records.

**Command** ([[commands/host-dns-lookup]]):
```bash
host code.wordpress.net
```

> This command queries DNS for the target's aliases and IPs, expecting output showing the chain to wpprojects.wordpress.com and lb.wordpress.com IPs (192.0.78.13, 192.0.78.12), confirming the vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/host-dns-lookup]]

## Tools Used

- [[tools/host]]

## Tags

- [[subdomain-takeover]]
- [[DNS]]
- [[cname]]
