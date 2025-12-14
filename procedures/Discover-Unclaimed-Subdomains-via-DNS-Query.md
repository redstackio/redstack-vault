---
tags:
  - dns
  - recon
  - subdomain-takeover
type: procedure
tools:
  - '[[tools/dig]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-query-svcgatewayloadus-starbucks-com-A]]'
  - '[[commands/dig-query-svcgatewaydevus-starbucks-com-A]]'
platforms:
  - Cloud
  - Web
techniques:
  - '[[Hardware]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 4d54c1d9-9a2b-4269-a207-fd21188d31db
created_at: '2025-12-14T04:51:26.615Z'
updated_at: '2025-12-14T04:51:26.615Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Discover-Unclaimed-Subdomains-via-DNS-Query

## Summary

This procedure uses DNS queries to identify subdomains with misconfigured CNAME records pointing to unclaimed cloud resources, such as Azure Traffic Manager endpoints, enabling subdomain takeover reconnaissance.

## Description

In this attack scenario, query A records for target subdomains like svcgatewayloadus.starbucks.com and svcgatewaydevus.starbucks.com. The responses reveal CNAMEs to unused Azure endpoints (e.g., s00197tmp0crdfulload0.trafficmanager.net), confirmed by NXDOMAIN status, indicating they are available for claiming. This is a key reconnaissance step for subdomain takeover vulnerabilities in cloud environments.

## Requirements

1. Access to DNS resolution tools like dig
2. Public internet access for querying external domains
3. Knowledge of target subdomains (e.g., via prior enumeration)

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using tools like dnsdumpster or Azure monitoring
- Implement DNSSEC to prevent unauthorized takeovers
- Monitor for NXDOMAIN responses on critical subdomains

## Objectives

1. Identify misconfigured subdomains pointing to unclaimed resources
2. Confirm availability for takeover
3. Gather endpoints for subsequent claiming

## Instructions

### Step 1: Query Load Subdomain

**Context**: Resolve the A record to uncover the CNAME to an unclaimed Azure endpoint.

**Command** ([[commands/dig-query-svcgatewayloadus-starbucks-com-A]]):
```bash
dig svcgatewayloadus.starbucks.com A
```

> This command queries the DNS A record, expecting a CNAME to s00197tmp0crdfulload0.trafficmanager.net with NXDOMAIN, indicating the resource is unclaimed.

### Step 2: Query Dev Subdomain

**Context**: Repeat for the development subdomain to find another vulnerable endpoint.

**Command** ([[commands/dig-query-svcgatewaydevus-starbucks-com-A]]):
```bash
dig svcgatewaydevus.starbucks.com A
```

> This reveals CNAME to s00197tmp0crdfuldev0.trafficmanager.net with NXDOMAIN.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used

- [[commands/dig-query-svcgatewayloadus-starbucks-com-A]]
- [[commands/dig-query-svcgatewaydevus-starbucks-com-A]]

## Tools Used

- [[tools/dig]]

## Tags

- [[DNS]]
- [[recon]]
- [[subdomain-takeover]]
