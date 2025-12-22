---
id: proc-dns-lookup-dangling
tags:
  - dns
  - reconnaissance
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-lookup-subdomain]]'
verified: false
platforms:
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:38:49.488Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# DNS-Lookup-to-Identify-Dangling-Subdomain

## Summary

This procedure performs a DNS lookup on a target subdomain to resolve its IP address and identify if it points to a dangling or unused resource, such as a deleted cloud instance, enabling potential subdomain takeover.

## Description

In a subdomain takeover attack, attackers scan for DNS records that point to decommissioned infrastructure without updating the DNS. This procedure uses a simple DNS query to reveal such misconfigurations, specifically targeting AWS EC2 IPs. The scenario involves querying a subdomain like v.zego.com, which resolved to 52.214.138.192—a deleted EC2 instance. Prerequisites include internet access and basic DNS tools; no target credentials are needed. Expected outcomes include identifying reclaimable IPs for further exploitation.

## Requirements

1. Internet connectivity for DNS resolution
2. Access to DNS query tools like dig (standard on Linux/macOS)
3. Knowledge of target subdomains (e.g., via prior recon or certificate transparency logs)

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling entries using tools like dnsdumpster or automated scripts
- Implement DNS monitoring with anomaly detection (e.g., via CloudWatch or Splunk) to alert on unresolved IPs
- Use subdomain management tools to automate cleanup of deleted resources

## Objectives

1. Resolve subdomain IP to detect dangling references
2. Verify IP availability for takeover potential
3. Gather intel for initial access via infrastructure compromise

## Instructions

### Step 1: Perform DNS Resolution

**Context**: Query the DNS A record for the target subdomain to obtain its IP address, checking if it's associated with active infrastructure.

**Command** ([[commands/dig-lookup-subdomain]]):
```bash
dig +short v.zego.com
```

> This command performs a concise DNS lookup, outputting only the IP address. Expected output is 52.214.138.192. Cross-verify the IP in AWS console or WHOIS to confirm it's unused (e.g., no active instance).

### Step 2: Validate Dangling Status

**Context**: Manually check the resolved IP for availability, ensuring it's not responding to the target organization's services.

**Command** (No direct command; use browser or ping):
```bash
ping -c 1 52.214.138.192
```

> If the IP is dangling, it may not respond or show as available in cloud provider dashboards. Success confirms potential for claiming.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domain

### Sub-Techniques

-

## Commands Used

- [[commands/dig-lookup-subdomain]]

## Tools Used

-

## Tags

- [[DNS]]
- [[Reconnaissance]]
- [[subdomain-takeover]]
