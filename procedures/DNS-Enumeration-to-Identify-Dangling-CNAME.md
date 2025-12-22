---
id: proc-dns-enum-dangling-cname
tags:
  - dns
  - enumeration
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
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T04:38:49.777Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# DNS-Enumeration-to-Identify-Dangling-CNAME

## Summary

This procedure uses DNS lookup tools to enumerate subdomains and detect dangling CNAME records pointing to unclaimed cloud services, such as Azure's .cloudapp.net, which can lead to subdomain takeover vulnerabilities.

## Description

In this attack scenario, the target is a production subdomain like d02-1-ag.productioncontroller.starbucks.com. The procedure involves querying DNS to reveal an NXDOMAIN response with a CNAME to a deleted but claimable Azure service (e.g., 3edbac0a-5c43-428a-b451-a5eb268f888b.cloudapp.net). This identifies opportunities for infrastructure hijacking. Prerequisites include public DNS access and basic networking knowledge. Expected outcomes include confirmation of the dangling record, enabling subsequent takeover steps.

## Requirements

1. Access to a DNS resolver tool like dig (available on Linux/macOS or via online tools)
2. Target domain/subdomain to enumerate
3. Network connectivity for DNS queries

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using automated tools like dnsdumpster or subjack
- Implement DNS monitoring for NXDOMAIN responses on critical subdomains
- Use cloud provider tools to verify and reclaim deleted resources promptly

## Objectives

1. Discover vulnerable DNS configurations for subdomain takeover
2. Gather technical details like CNAME targets for exploitation planning
3. Validate the record's claimability before proceeding to infrastructure acquisition

## Instructions

### Step 1: Perform DNS Lookup

**Context**: Query the target subdomain to check resolution and extract CNAME details, identifying if it's dangling.

**Command** ([[commands/dig-dns-lookup]]):
```bash
dig d02-1-ag.productioncontroller.starbucks.com
```

> This command performs a DNS query, returning authoritative answers. Look for NXDOMAIN in the status and a CNAME record in the ANSWER section pointing to a .cloudapp.net domain, indicating a dangling Azure service.

### Step 2: Analyze Response

**Context**: Parse the output to confirm vulnerability.

**Instructions**: Review the dig output for the CNAME value. If it points to an unclaimed service (verifiable by attempting to access it directly, which should fail), proceed to claiming.

> No additional command needed; manual inspection suffices.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Vulnerability Scanning

### Sub-Techniques

- None

## Commands Used

- [[commands/dig-dns-lookup]]

## Tools Used

- [[tools/dig]]

## Tags

- [[DNS]]
- [[enumeration]]
- [[subdomain-takeover]]
