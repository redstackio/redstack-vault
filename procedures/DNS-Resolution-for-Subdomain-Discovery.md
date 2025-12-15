---
id: a501e38e-0da9-42ff-9ef0-ceb7752373c3
name: DNS-Resolution-for-Subdomain-Discovery
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.354Z'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Gather Victim Network Information]]'
sub_techniques:
  - '[[Domain Properties]]'
tags:
  - dns
  - recon
  - aws
commands:
  - '[[commands/dig-resolve-subdomain]]'
platforms:
  - AWS
tools: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Network Information]]'
---

# DNS-Resolution-for-Subdomain-Discovery

## Summary

This procedure resolves the DNS records for a target subdomain to identify associated IP addresses, particularly useful for detecting misconfigurations like pointers to deallocated or re-allocated cloud instances.

## Description

In scenarios involving cloud environments like AWS, subdomains may retain outdated DNS records pointing to previously owned resources. This procedure uses standard DNS lookup to reveal the IP, which can indicate re-allocation (e.g., EC2 instances). The target environment is public DNS resolvable subdomains. Expected outcomes include IP details for further probing, with no exploitation but potential for info disclosure chains.

## Requirements

1. Internet access for DNS queries
2. Target subdomain name (e.g., 27.prd.vine.co)
3. DNS resolver tool availability (e.g., dig on Linux/macOS)

## Defense

Defensive measures and detection strategies:

- Regularly audit and update DNS records for deallocated resources
- Monitor DNS queries for unusual subdomain resolutions
- Use DNSSEC to prevent spoofing, though not directly applicable here

## Objectives

1. Obtain IP address linked to the subdomain
2. Identify if the IP belongs to a cloud provider like AWS EC2
3. Enable subsequent access for vulnerability assessment

## Instructions

### Step 1: Perform DNS Lookup

**Context**: Query the authoritative DNS servers for the subdomain's A record to get the IP address.

**Command** ([[commands/dig-resolve-subdomain]]):
```bash
dig 27.prd.vine.co
```

> This command sends a DNS query and outputs the resolved IP. Look for the ANSWER SECTION showing the IP; cross-reference with AWS IP ranges to confirm EC2.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Network Information]] Gather Victim Network Information

### Sub-Techniques

- [[Domain Properties]] DNS

## Commands Used

- [[commands/dig-resolve-subdomain]]

## Tools Used


## Tags

- [[DNS]]
- [[recon]]
- [[aws]]
