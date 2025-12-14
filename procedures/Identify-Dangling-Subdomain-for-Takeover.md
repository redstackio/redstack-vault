---
tags:
  - subdomain-takeover
  - dns
  - recon
type: procedure
tools:
  - '[[tools/Censys]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - CDN
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:38:49.750Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: ad49aaa5-432b-42d1-a43c-30fc738d76cc
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Identify Dangling Subdomain for Takeover

## Summary

This procedure involves reconnaissance to identify unused subdomains with dangling DNS records, such as those left after cancelling a CDN service like Fastly, enabling potential subdomain takeover attacks.

## Description

In the context of targeting CDN domains like Snapchat's, attackers scan for subdomains (e.g., fastly.sc-cdn.net) that resolve but lack active backing services. This misconfiguration allows anyone to claim the record via the provider's service creation process. The procedure focuses on manual or tool-assisted discovery of such vulnerabilities, confirming they are claimable without alerting the target.

## Requirements

1. Access to DNS lookup tools or search engines for subdomain enumeration.
2. Knowledge of the target's CDN providers (e.g., Fastly).
3. Public internet access for querying domain records.

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling entries post-service cancellation.
- Implement DNS monitoring tools to alert on unauthorized claims.
- Use certificate transparency logs to track subdomain usage.

## Objectives

1. Discover vulnerable subdomains tied to the target's infrastructure.
2. Validate the dangling status for takeover feasibility.
3. Prepare for subsequent confirmation and exploitation steps.

## Instructions

### Step 1: Enumerate Potential Subdomains

**Context**: Search for CDN-related subdomains associated with the target, focusing on known providers like Fastly.

**Command** (Manual Query):
No specific command; use browser or DNS tools to query fastly.sc-cdn.net and check resolution.

> Query the subdomain to see if it resolves to a non-existent or error page, indicating a dangling record from a cancelled Fastly instance.

### Step 2: Verify Dangling Status

**Context**: Confirm the record points to a claimable CNAME without active service.

**Command** (DNS Lookup):
```bash
dig fastly.sc-cdn.net
```

> Expected output shows a CNAME to a Fastly endpoint that is inactive, confirming vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques

- None

## Commands Used

- None specific

## Tools Used

- [[tools/Censys]]

## Tags

- [[subdomain-takeover]]
- [[DNS]]
- [[recon]]
