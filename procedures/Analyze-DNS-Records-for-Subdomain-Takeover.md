---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - dns-recon
  - subdomain-takeover
  - azure
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - Azure
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:38:49.801Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Analyze DNS Records for Subdomain Takeover

## Summary

This procedure involves querying and analyzing DNS records of target subdomains to identify CNAME chains pointing to unclaimed or deleted cloud resources, such as Azure cloudapp.net domains, enabling subdomain takeover attacks.

## Description

In scenarios where organizations delete Azure resources but fail to update DNS, subdomains remain vulnerable. This procedure uses public DNS queries to trace CNAME records, revealing exploitable dangling pointers. It targets environments like Starbucks' svcgatewayus.starbucks.com, where the chain leads to an unregistered 1fd05821-7501-40de-9e44-17235e7ab48b.cloudapp.net, allowing attackers to claim control for malicious purposes like phishing or XSS.

## Requirements

1. Internet access for DNS queries
2. Tools like dig or online DNS lookup services
3. Knowledge of target subdomain (e.g., svcgatewayus.starbucks.com)

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using automated tools like dnsdumpster or Azure DNS monitoring
- Implement DNS TTL reductions and validation scripts to detect unclaimed resources
- Use Azure AD alerts for unregistered domain claims

## Objectives

1. Discover misconfigured DNS pointing to claimable cloud resources
2. Map the full CNAME chain for takeover feasibility
3. Identify high-impact subdomains for exploitation

## Instructions

### Step 1: Query CNAME Records

**Context**: Start by querying the target subdomain's CNAME to trace the DNS chain.

Use dig to fetch records:

```bash
dig CNAME svcgatewayus.starbucks.com +short
```

> This outputs the intermediate like s00197tmp0crdfulprod0.trafficmanager.net. Follow up by querying that.

### Step 2: Trace Full Chain

**Context**: Continue querying each hop until reaching the final cloud domain.

```bash
dig CNAME s00197tmp0crdfulprod0.trafficmanager.net +short
```

> Expected: 1fd05821-7501-40de-9e44-17235e7ab48b.cloudapp.net. Verify if it's unregistered by attempting access or Azure lookup.

### Step 3: Validate Unclaimed Status

**Context**: Confirm the final domain has no active Azure resource.

Attempt HTTP access:

```bash
curl -I http://1fd05821-7501-40de-9e44-17235e7ab48b.cloudapp.net
```

> Success if 404 or no response, indicating claimable.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[dns-recon]]
- [[subdomain-takeover]]
