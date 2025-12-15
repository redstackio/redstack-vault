---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - reconnaissance
  - certificates
  - censys
type: procedure
tools:
  - '[[tools/Censys]]'
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:23:32.733Z'
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
# Search-for-IRCCloud-Related-Certificates-Using-Censys

## Summary

This procedure uses Censys.io to search for certificates associated with IRCCloud, revealing exposed servers like an nginx instance at IP 54.153.101.52 with a self-signed certificate, as part of reconnaissance in a bug bounty hunt.

## Description

In the context of targeting IRCCloud infrastructure, this reconnaissance step leverages public certificate transparency data to map out associated hosts. By querying for IRCCloud-related certificates, attackers can identify hidden or misconfigured servers without direct interaction, uncovering potential entry points for further exploitation. Expected outcomes include IP addresses and certificate details that point to vulnerable services.

## Requirements

1. Access to internet-wide search engine like Censys.io (free account sufficient)
2. Knowledge of target domain (e.g., IRCCloud) for query construction
3. Web browser for interface navigation

## Defense

Defensive measures and detection strategies:

- Monitor certificate issuance via tools like Certificate Transparency logs
- Use services like Censys or Shodan defensively to audit own exposure
- Implement proper certificate management to avoid self-signed certs in production

## Objectives

1. Discover exposed IPs linked to target organization
2. Identify self-signed or misconfigured certificates
3. Establish initial attack surface mapping

## Instructions

### Step 1: Query Censys for Certificates

**Context**: Initiate search to find certificates containing IRCCloud references, focusing on host IPs.

No specific command; use web interface:

Navigate to https://censys.io and search in the "Certificates" section with query: "IRCCloud" or parsed subjects like "*.irccloud.com".

> This returns a list of certificates; filter for self-signed ones and note associated IPv4 addresses like 54.153.101.52.

### Step 2: Review Results for Exposed Hosts

**Context**: Analyze search output to pinpoint potentially vulnerable servers.

Export or screenshot results showing IP, certificate details, and any associated services.

> Expected output includes IP 54.153.101.52 with self-signed cert, indicating an exposed nginx server.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Censys]]

## Tags

- [[Reconnaissance]]
- [[certificates]]
