---
id: proc-discover-dangling-subdomains
tags:
  - dns
  - enumeration
  - reconnaissance
type: procedure
tools:
  - '[[tools/dig]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:51:26.684Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Discover Dangling Subdomains via DNS Enumeration

## Summary

This procedure involves enumerating a target's DNS records to identify subdomains with dangling CNAME entries pointing to unused third-party services, setting the stage for potential subdomain takeovers.

## Description

In a typical attack scenario, attackers scan for subdomains using tools or manual queries to find misconfigurations where a CNAME record exists but the referenced service (e.g., UptimeRobot's stats domain) is not actively used. This allows discovery of takeover opportunities. The target environment is public DNS, with outcomes including identification of vulnerable subdomains like status0.stripo.email pointing to stats.uptimerobot.com. Prerequisites include internet access and basic DNS knowledge.

## Requirements

1. Access to DNS resolution tools or online inspectors
2. Target domain name for enumeration
3. No credentials needed; external only

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using automated scanners
- Monitor third-party service integrations and remove unused configurations
- Implement DNS monitoring alerts for changes or unresolved records

## Objectives

1. Identify misconfigured subdomains
2. Confirm dangling status for takeover potential
3. Gather evidence of vulnerability

## Instructions

### Step 1: Query DNS Records

**Context**: Use DNS lookup to inspect CNAME records for the target subdomain.

**Command** (dig-cname-query):
```bash
dig status0.stripo.email CNAME
```

> This command queries the CNAME record, revealing if it points to an external service like stats.uptimerobot.com. Expected output includes the authoritative response showing the dangling alias.

### Step 2: Verify Resolution

**Context**: Check if the subdomain resolves but lacks active content.

**Command** (curl-head-request):
```bash
curl -I https://status0.stripo.email
```

> This performs a HEAD request to see if the domain resolves without serving content, indicating it's dangling. Expected output: Connection timeout or no response body.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- None

## Commands Used

- [[dig-cname-query]]
- [[curl-head-request]]

## Tools Used

- [[tools/dig]]

## Tags

- [[DNS]]
- [[Reconnaissance]]
