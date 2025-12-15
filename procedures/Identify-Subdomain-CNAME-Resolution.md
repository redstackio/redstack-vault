---
id: p-identify-cname-resolution
tags:
  - dns
  - reconnaissance
  - cname
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
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:24:31.531Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Identify Subdomain CNAME Resolution

## Summary

This procedure involves performing DNS reconnaissance to identify if a target subdomain, such as 'events.hackerone.com', resolves via a CNAME to a third-party vendor service, revealing potential external dependencies that may introduce vulnerabilities.

## Description

In attack scenarios targeting web applications, subdomains often alias to third-party services for event handling or other functionalities. By querying DNS records, attackers can uncover these dependencies, which might expose misconfigurations like open redirects. This step requires no authentication and uses standard DNS tools to map the subdomain's resolution path. Expected outcomes include confirmation of external CNAMEs, setting the stage for further testing of the vendor's endpoints.

## Requirements

1. Access to DNS resolution tools (e.g., dig, nslookup)
2. Public internet connectivity
3. Target subdomain name (e.g., events.hackerone.com)

## Defense

Defensive measures and detection strategies:

- Monitor DNS queries for anomalous reconnaissance patterns
- Implement DNSSEC to prevent spoofing, though it doesn't hide CNAMEs
- Regularly audit third-party CNAME dependencies for security

## Objectives

1. Uncover third-party service integrations via DNS
2. Identify potential attack surface expansions
3. Validate subdomain resolution without direct access

## Instructions

### Step 1: Query DNS for CNAME Record

**Context**: Use a DNS lookup command to retrieve the CNAME record for the target subdomain, revealing any third-party pointers.

No specific command template, but execute a DNS query:

```bash
dig CNAME events.hackerone.com
```

> This command resolves the CNAME, showing if it points to a vendor domain. Expected output includes the alias target, e.g., 'events.hackerone.com is an alias for vendor-service.com'.

### Step 2: Verify Resolution Chain

**Context**: Follow up by resolving the full chain to confirm the external endpoint.

```bash
nslookup -type=CNAME events.hackerone.com
```

> Output confirms the third-party domain, indicating potential for inherited vulnerabilities.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[dns-recon]]
- [[cname-discovery]]
