---
tags:
  - dns
  - reconnaissance
  - subdomain-takeover
type: procedure
tools:
  - '[[tools/dig]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-dns-lookup]]'
verified: false
platforms:
  - Cloud
  - Azure
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:38:49.704Z'
sub_techniques: []
id: 85beafa2-4bfc-40c7-8ed3-f25a9315cfa4
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Discover-Subdomain-DNS-Misconfiguration

## Summary

This procedure identifies dangling DNS records, such as CNAMEs pointing to unclaimed cloud resources, enabling subdomain takeover attacks by revealing misconfigurations in domain resolution.

## Description

In this scenario, the procedure targets subdomains like usclsapipma.cv.ford.com to uncover CNAME chains leading to deregistered Azure resources. By querying DNS, attackers confirm unclaimed endpoints, setting the stage for claiming them. Prerequisites include public DNS access; outcomes include proof of misconfiguration via NXDOMAIN responses, allowing progression to resource verification.

## Requirements

1. Access to DNS resolution tools like dig
2. Target domain knowledge (e.g., ford.com subdomains)
3. Network connectivity to public DNS servers

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using tools like dnsdumpster or Azure DNS analytics
- Implement DNS monitoring for NXDOMAIN queries and automate alerts on unclaimed cloud pointers
- Use Azure AD for resource locking and periodic sweeps of available VMs

## Objectives

1. Uncover misconfigured DNS records pointing to external cloud services
2. Confirm chain to unclaimed resources like Azure Cloud Apps
3. Provide evidence for takeover feasibility

## Instructions

### Step 1: Query Subdomain DNS Records

**Context**: Perform a DNS lookup to reveal the CNAME configuration and any resolution issues.

**Command** ([[commands/dig-dns-lookup]]):
```bash
dig usclsapipma.cv.ford.com
```

> This command queries the authoritative DNS servers for the subdomain, displaying the CNAME to usclsapipma.trafficmanager.net and further to feuscspma3fcvapi.eastus.cloudapp.azure.com. Expected output includes an NXDOMAIN for the final Azure endpoint, indicating it's dangling and unclaimed.

### Step 2: Analyze Response for Dangling Indicators

**Context**: Review the dig output for chains to cloud providers and unresolvable records.

No specific command; manually inspect for Azure cloudapp.azure.com patterns and NXDOMAIN.

> Look for responses showing partial resolution but failure at the cloud endpoint, confirming the vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- None

## Commands Used

- [[commands/dig-dns-lookup]]

## Tools Used

- [[tools/dig]]

## Tags

- [[DNS]]
- [[Reconnaissance]]
- [[subdomain-takeover]]
