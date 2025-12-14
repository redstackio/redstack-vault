---
tags:
  - dns
  - reconnaissance
  - subdomain-enumeration
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-lookup-cname]]'
verified: false
platforms:
  - Web
  - Azure
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:38:49.824Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 979625b6-0fd9-4575-a226-239a0ee8890c
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Identify Dangling Subdomain DNS Records

## Summary

This procedure involves enumerating target subdomains and querying their DNS records to identify dangling CNAMEs pointing to unclaimed cloud resources, such as Azure Traffic Manager profiles. It is the initial reconnaissance step in subdomain takeover attacks, revealing misconfigurations where DNS points to abandoned services.

## Description

In a typical attack scenario, attackers scan for subdomains using tools like subfinder or Amass, then use DNS lookup commands to check for CNAME records. A dangling record is one where the CNAME targets a cloud endpoint (e.g., *.trafficmanager.net) that no longer exists or is unclaimed. This exposes the subdomain to takeover, as anyone can register the cloud resource and inherit the DNS traffic. Prerequisites include public access to DNS queries; no authentication is needed. Expected outcomes: A list of vulnerable subdomains ready for further verification.

## Requirements

1. Access to DNS resolution tools (e.g., dig installed on Linux/macOS)
2. Target domain name (e.g., starbucks.com)
3. Optional: Subdomain enumeration tool like subfinder for broader discovery

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using automated scanners like dnsdumpster or custom scripts
- Implement DNS monitoring with tools like DNSSec or Cloudflare to alert on unresolved records
- Rotate or remove unused cloud resources promptly to prevent abandonment

## Objectives

1. Discover subdomains with potentially exploitable DNS configurations
2. Identify CNAMEs pointing to cloud services like Azure Traffic Manager
3. Flag records that may lead to subdomain takeover risks

## Instructions

### Step 1: Enumerate Subdomains

**Context**: First, generate a list of potential subdomains to check for DNS misconfigurations.

Use a tool like subfinder (not linked as command here) to list subdomains:

```bash
subfinder -d starbucks.com -o subdomains.txt
```

> This outputs a file with subdomains like mydailydev.starbucks.com.

### Step 2: Query DNS for CNAME Records

**Context**: For each subdomain, perform a DNS lookup to reveal CNAME targets.

**Command** ([[commands/dig-lookup-cname]]):
```bash
dig mydailydev.starbucks.com CNAME
```

> This command queries the authoritative DNS for the CNAME record. Expected output includes the target like "mydailydev.trafficmanager.net" if dangling. If no A/AAAA record resolves, it's likely unclaimed.

### Step 3: Validate Dangling Status

**Context**: Confirm the record is dangling by checking if the CNAME target resolves to nothing.

Follow up with a full dig:

```bash
dig mydailydev.trafficmanager.net
```

> Look for NXDOMAIN or no answer, indicating abandonment.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domain Name

### Sub-Techniques

-

## Commands Used

- [[commands/dig-lookup-cname]]

## Tools Used

-

## Tags

- [[DNS]]
- [[Reconnaissance]]
- [[subdomain-enumeration]]
