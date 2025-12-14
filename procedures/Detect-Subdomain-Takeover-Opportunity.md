---
id: proc-detect-subdomain-takeover-opportunity
tags:
  - subdomain-takeover
  - dns
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-cname-lookup]]'
  - '[[commands/nslookup-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Software]]'
updated_at: '2025-12-14T04:51:10.595Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---
# Detect-Subdomain-Takeover-Opportunity

## Summary

This procedure involves reconnaissance to identify potential subdomain takeover vulnerabilities by examining DNS configurations for dangling records or unused domain spaces, as seen in the openapi.starbucks.com case where prior reports suggested risks without evidence.

## Description

Subdomain takeovers occur when a subdomain's DNS points to a third-party service that is no longer in use, allowing attackers to claim control. In this scenario, the target is a web subdomain like openapi.starbucks.com, suspected due to process flaws in domain approval. The procedure focuses on manual DNS investigation to confirm configurability issues without exploitation. Expected outcomes include evidence of takeover feasibility, enabling further reporting. Prerequisites include public DNS access and knowledge of common dangling services (e.g., AWS S3, Heroku).

## Requirements

1. Internet access for DNS queries.
2. Basic understanding of DNS records (CNAME, A).
3. Access to tools like dig or nslookup (standard on Linux/macOS).

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using automated scanners like dnsdumpster or subjack.
- Implement automated approval workflows to prevent human inconsistencies.
- Monitor for unauthorized content on subdomains via certificate transparency logs.

## Objectives

1. Confirm presence of unused or misconfigured subdomain resources.
2. Gather evidence for vulnerability reporting.
3. Assess potential impact like phishing enablement.

## Instructions

### Step 1: Query DNS Records

**Context**: Start by resolving the subdomain to identify CNAME or other records pointing to potentially claimable services.

**Command** ([[commands/dig-cname-lookup]]):
```bash
dig CNAME openapi.starbucks.com
```

> This command queries for CNAME records. Expected output: A record like "openapi.starbucks.com. 3600 IN CNAME dangling-service.aws.s3.com." indicating a potential takeover if the bucket is empty/unclaimed.

### Step 2: Verify Resolution with Alternative Tool

**Context**: Cross-verify with nslookup to confirm the configuration and check for active responses.

**Command** ([[commands/nslookup-query]]):
```bash
nslookup openapi.starbucks.com
```

> This provides IP resolution and server info. Expected output: Server responses showing unresolved or third-party pointers, with no active content on probed URLs.

### Step 3: Probe for Unused Paths

**Context**: Manually check HTTP responses on potential unused URLs to confirm lack of active services.

Use a browser or curl to access /test or similar; expect 404 or no response, indicating exploitability.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Software]] Domain Properties

### Sub-Techniques

- None

## Commands Used

- [[commands/dig-cname-lookup]]
- [[commands/nslookup-query]]

## Tools Used

- None

## Tags

- [[subdomain-takeover]]
- [[dns-recon]]
