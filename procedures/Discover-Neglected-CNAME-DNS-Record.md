---
tags:
  - dns-recon
  - cname
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/dig-lookup-cname]]'
verified: false
platforms:
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:51:10.585Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 545dbb09-3250-464c-a3e3-dc485dd1dba6
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Discover Neglected CNAME DNS Record

## Summary

This procedure involves querying DNS records to identify CNAME entries pointing to inactive or abandoned third-party services, a common precursor to subdomain takeover attacks.

## Description

In the context of the Screenhero subdomain, attackers inspect DNS for feedback.screenhero.com to find a CNAME to screenhero.uservoice.com. This misconfiguration arises from incomplete cleanup after service deactivation, allowing potential hijacking. The procedure requires public DNS access and basic query tools.

## Requirements

1. Access to a DNS resolver (e.g., public internet)
2. Target domain knowledge (e.g., screenhero.com subdomains)
3. No special credentials needed

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using automated scanners
- Implement DNS monitoring for changes and inactive service pointers
- Verify third-party services before decommissioning and update DNS accordingly

## Objectives

1. Uncover misconfigured DNS records enabling takeover
2. Map the attack surface of acquired domains
3. Prepare for verification of service status

## Instructions

### Step 1: Query CNAME Record

**Context**: Use DNS lookup to retrieve the CNAME for the target subdomain, revealing pointers to external services.

**Command** ([[commands/dig-lookup-cname]]):
```bash
dig feedback.screenhero.com CNAME
```

> This command queries the authoritative DNS for the CNAME record. Expected output includes "feedback.screenhero.com. 3600 IN CNAME screenhero.uservoice.com.", confirming the pointer.

### Step 2: Analyze Record

**Context**: Review the output to identify if the pointed service (e.g., UserVoice) is likely inactive based on domain patterns.

No command needed; manually note the target hostname for further checks.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used

- [[commands/dig-lookup-cname]]

## Tools Used


## Tags

- [[dns-recon]]
- [[subdomain-takeover]]
