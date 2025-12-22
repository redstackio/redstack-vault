---
tags:
  - dns
  - cname
  - recon
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-13T23:52:49.574Z'
sub_techniques: []
id: f5c88f21-59f2-46ef-9c0e-83bcfa30094f
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Identify-CNAME-Delegation-to-Third-Party-Vendor

## Summary

This procedure involves querying DNS records to identify CNAME delegations from a target subdomain to a third-party vendor's domain, revealing potential vulnerability inheritance through service integrations.

## Description

In scenarios where subdomains are delegated via CNAME to external services, vulnerabilities in the third-party can affect the parent domain. This reconnaissance step uses DNS resolution to map the delegation, setting the stage for testing inherited flaws like XSS in authenticated endpoints. The target environment is web-based with public DNS access, and outcomes include confirmation of external control for targeted exploitation.

## Requirements

1. Access to DNS resolution tools (e.g., dig, nslookup).
2. Knowledge of the target subdomain (e.g., events.hackerone.com).
3. No authentication required for this reconnaissance.

## Defense

Defensive measures and detection strategies:

- Monitor DNS records for unexpected CNAME changes.
- Implement subdomain isolation and strict CSP to limit inheritance risks.
- Regularly audit third-party integrations for vulnerabilities.

## Objectives

1. Confirm CNAME pointing to third-party domain.
2. Identify potential attack surface expansion.
3. Enable targeted testing of inherited vulnerabilities.

## Instructions

### Step 1: Query DNS for CNAME Record

**Context**: Use a DNS lookup tool to resolve the CNAME for the target subdomain, revealing the delegated vendor domain.

No specific command required; use browser or terminal:

```bash
dig CNAME events.hackerone.com
```

> This command outputs the CNAME record, e.g., events.hackerone.com is an alias for vendor.example.com, indicating external control.

### Step 2: Verify Delegation Implications

**Context**: Analyze the output to understand subdomain inheritance, preparing for endpoint testing.

Review the response for the authoritative name server and alias details.

**Expected Output**: Confirmation of CNAME delegation.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[DNS]]
- [[recon]]
