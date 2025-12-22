---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567895
tags:
  - verification
  - http-probe
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Azure
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Web Protocols]]'
updated_at: '2025-12-14T04:38:49.788Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Web Protocols]]'
---
# Verify Control of Hijacked Subdomain

## Summary

This procedure tests access to the original subdomain to confirm it now serves the deployed attacker-controlled content, validating the takeover.

## Description

Post-deployment, HTTP requests to the subdomain should resolve via DNS to the Azure service and return custom app responses. For svcgatewayus.starbucks.com, this shows the PoC page instead of original content, confirming impact for abuses like malware distribution or SSL cert issuance.

## Requirements

1. Deployed application on Azure
2. DNS propagation time (up to 5-10 min)
3. HTTP client like curl or browser

## Defense

Defensive measures and detection strategies:

- Set up subdomain monitoring with uptime tools
- Alert on content changes via hash comparisons
- Use DNSSEC to prevent hijacks

## Objectives

1. Confirm traffic redirection to attacker resource
2. Validate content serving
3. Assess potential for further exploitation

## Instructions

### Step 1: Wait for DNS Propagation

**Context**: Allow time for changes to propagate.

Monitor with:

```bash
dig A svcgatewayus.starbucks.com
```

> Expected: IP points to Azure endpoints.

### Step 2: Send Test Request

**Context**: Access the subdomain to check response.

```bash
curl http://svcgatewayus.starbucks.com
```

> Expected: HTML from ASP.NET app, e.g., 'Subdomain takeover PoC'.

### Step 3: Validate Full Control

**Context**: Test HTTPS or additional paths if applicable.

Browse to https://svcgatewayus.starbucks.com or curl specific endpoints.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Web Protocols]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[subdomain-takeover]]
