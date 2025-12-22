---
id: proc-exness-redirect-dos
tags:
  - ssrf
  - dos
  - redirects
type: procedure
tools:
  - '[[tools/mandygreencps-com]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/get-check-redirect-chain]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T03:46:14.640Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Test-Redirect-Handling-for-DoS-Amplification

## Summary

This procedure tests the backend's redirect following (up to 30 via Python requests) using a custom redirect chain to amplify resource usage, enable DoS, and bypass protocol/port restrictions.

## Description

The /check endpoint follows redirects, allowing schema changes (HTTP to HTTPS) and port switches. A chain on mandygreencps.com demonstrates amplification potential before WAF rate-limiting. Applicable to SSRF in redirect-enabled backends.

## Requirements

1. SSRF confirmed
2. Custom redirect chain hosted (e.g., on mandygreencps.com)
3. curl

## Defense

Defensive measures and detection strategies:

- Limit max_redirects to 5-10 in HTTP clients
- Rate-limit requests to SSRF endpoints
- Block infinite redirect patterns via WAF rules

## Objectives

1. Confirm redirect amplification for DoS
2. Test protocol/port bypass
3. Assess resource exhaustion risk

## Instructions

### Step 1: Trigger Redirect Chain

**Context**: Send GET to /check with redirect URL to force multiple backend requests.

**Command** ([[commands/get-check-redirect-chain]]):

```bash
curl -X GET "https://my.exnessaffiliates.com/api/partner_integrations/template/check/?url=https://mandygreencps.com/redir1.html"
```

> Backend processes 30 redirects; monitor for quick completion and load.

### Step 2: Verify Bypass

**Context**: Check if schema/port changes succeed in chain.

Observe interactions on redirect host for protocol switches.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques


## Commands Used

- [[commands/get-check-redirect-chain]]

## Tools Used

- [[tools/mandygreencps-com]]

## Tags

- ssrf
- dos
- redirects
