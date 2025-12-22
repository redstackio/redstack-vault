---
tags:
  - subdomain-takeover
  - dns
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:51:10.537Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 52a037af-6dc6-40ba-82a5-d845ec9154f5
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Enumerate Subdomains for Dangling CNAMEs

## Summary

This procedure identifies subdomains with dangling CNAME records pointing to unclaimed external services, enabling subdomain takeover attacks. It focuses on passive and active DNS enumeration to spot misconfigurations without alerting the target.

## Description

In a subdomain takeover, attackers scan for subdomains whose CNAME records reference deleted or unclaimed resources on third-party platforms like Heroku or AWS S3. This procedure uses DNS queries to enumerate and validate such records, as seen in the Uber vulnerability where subdomains like translate.uber.com pointed to inactive services. Prerequisites include access to public DNS resolvers and knowledge of common third-party services.

## Requirements

1. Access to DNS resolution tools (e.g., dig or online resolvers)
2. List of target subdomains (from prior enumeration or certificate transparency logs)
3. Accounts on potential third-party services for later validation (optional for this step)

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using automated tools like DNS linter
- Monitor third-party service usage and revoke unused domains
- Implement DNS monitoring for unexpected resolutions

## Objectives

1. Discover subdomains with misconfigured CNAMEs
2. Validate if pointed services are unclaimed
3. Prepare for takeover without direct interaction

## Instructions

### Step 1: Enumerate Target Subdomains

**Context**: Obtain a list of subdomains for the target domain using passive sources.

No specific command; use tools like crt.sh or SecurityTrails to gather subdomains manually.

> Expected: A text file with subdomains like translate.uber.com, de.uber.com.

### Step 2: Query DNS for CNAME Records

**Context**: Resolve each subdomain to check for CNAMEs pointing to external services.

Execute a DNS query for each subdomain:

```bash
dig +short translate.uber.com CNAME
```

> This command queries the CNAME record. Expected output: A hostname like unclaimed-app.herokuapp.com if dangling.

### Step 3: Validate Service Status

**Context**: Check if the CNAME target is active or claimable.

Attempt HTTP access to the resolved hostname:

```bash
curl -I https://unclaimed-app.herokuapp.com
```

> Expected: 404 or service error indicating it's unclaimed.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: DNS

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-enumeration]]
- [[dns-query]]
