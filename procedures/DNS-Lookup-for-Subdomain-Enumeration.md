---
id: proc-dns-lookup-subdomain
tags:
  - dns
  - reconnaissance
  - subdomain-enumeration
type: procedure
tools:
  - '[[tools/host]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/host-dns-lookup]]'
verified: false
platforms:
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:51:26.577Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# DNS-Lookup-for-Subdomain-Enumeration

## Summary

This procedure uses DNS lookup tools to enumerate subdomains and identify CNAME records pointing to third-party services, revealing potential subdomain takeover vulnerabilities like dangling DNS entries.

## Description

In the context of reconnaissance against web applications, perform a DNS query on target subdomains to resolve their records. This uncovers aliases to services such as Hubspot, where expired accounts leave subdomains vulnerable to takeover. The procedure targets environments with public DNS exposure and is a foundational step in attack chains exploiting misconfigurations in DNS propagation and third-party integrations.

## Requirements

1. Command-line access to a system with DNS resolution capabilities (e.g., Linux terminal)
2. Network connectivity to public DNS servers (port 53 UDP/TCP)
3. Target subdomain like blog.greenhouse.io

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using automated tools like dnsdumpster or internal scripts
- Implement DNS monitoring with services like Cloudflare or Route 53 to alert on unresolved or expired third-party pointers
- Enforce removal of DNS entries upon service cancellation in third-party platforms

## Objectives

1. Discover CNAME aliases pointing to external services
2. Identify potential takeover targets via inactive resolutions
3. Gather evidence for vulnerability reporting

## Instructions

### Step 1: Execute DNS Lookup

**Context**: Query the target subdomain to reveal its DNS resolution chain, including any CNAME aliases to services like Hubspot's Akamai edge.

**Command** ([[commands/host-dns-lookup]]):
```bash
host blog.greenhouse.io
```

> This command performs a DNS lookup using the system's resolver, outputting the hostname's IP addresses and any aliases. Expected output includes CNAME chains like "blog.greenhouse.io is an alias for san.secure001.hubspot.com.edgekey.net", indicating a Hubspot integration.

### Step 2: Analyze Output for Vulnerabilities

**Context**: Review the resolution to check for third-party service pointers without active content, signaling expired accounts.

**Command** (No specific command; manual analysis):

> Parse the output for Akamai or service-specific domains. If the subdomain resolves but serves no content, it confirms claimability.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used

- [[commands/host-dns-lookup]]

## Tools Used

- [[tools/host]]

## Tags

- [[DNS]]
- [[Reconnaissance]]
