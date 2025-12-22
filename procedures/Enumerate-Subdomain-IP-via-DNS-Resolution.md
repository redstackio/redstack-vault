---
id: proc-enumerate-subdomain-dns
name: Enumerate Subdomain IP via DNS Resolution
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:49.599Z'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Hardware]]'
sub_techniques: []
tags:
  - dns
  - reconnaissance
  - subdomain-enumeration
commands:
  - '[[commands/dig-resolve-subdomain]]'
platforms:
  - AWS
  - Cloud
tools:
  - '[[tools/dig]]'
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---

# Enumerate Subdomain IP via DNS Resolution

## Summary

This procedure uses DNS lookup to resolve a subdomain's IP address, identifying potential orphaned resources for subdomain takeover attacks.

## Description

In scenarios where organizations decommission cloud instances without updating DNS, subdomains may point to unused IPs. This step queries the DNS to reveal such IPs, enabling attackers to claim them. The target environment is public DNS resolvable subdomains on cloud platforms like AWS.

## Requirements

1. Access to a system with DNS resolution tools (e.g., Linux terminal)
2. Knowledge of the target subdomain (e.g., fr1.vpn.zomans.com)
3. No authentication required for public DNS queries

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for stale entries using tools like DNSdumpster or automated scripts
- Implement DNS monitoring for unexpected resolutions
- Use CAA records to restrict certificate issuance on subdomains

## Objectives

1. Obtain the IP address associated with the subdomain
2. Identify if the IP is orphaned (non-responsive)
3. Prepare for IP claiming in takeover

## Instructions

### Step 1: Perform DNS Lookup

**Context**: Query the A record of the subdomain to get its IP.

**Command** ([[commands/dig-resolve-subdomain]]):
```bash
dig +short fr1.vpn.zomans.com
```

> This command performs a concise DNS A record lookup, outputting only the IP. Expected output: 52.47.57.107. Verify the IP by pinging or curling it; if unresponsive, it's likely orphaned.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: DNS

### Sub-Techniques


## Commands Used

- [[commands/dig-resolve-subdomain]]

## Tools Used

- [[tools/dig]]

## Tags

- [[DNS]]
- [[Reconnaissance]]
