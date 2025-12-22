---
tags:
  - csrf
  - recon
  - web
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/test-stock-alert-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:42.562Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 029aab6a-a53e-479a-841c-198308e79a4f
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-CSRF-Vulnerable-Stock-Alert-Endpoint

## Summary

This procedure identifies the CSRF-vulnerable stock alert endpoint on Lyst that allows adding items to a user's saved list via unprotected GET requests, enabling further exploitation for denial of service.

## Description

In the Lyst platform, the /email-capture/stock-alert/{product_id}/ endpoint processes GET requests to subscribe to stock alerts, which also automatically appends the product to the user's saved list if authenticated. Lacking CSRF tokens, it permits cross-origin forgery. This step involves reconnaissance to confirm the behavior, typically using browser tools or curl to test additions without user consent. Prerequisites include access to Lyst product IDs and a test authenticated session.

## Requirements

1. Access to Lyst website (www.lyst.com)
2. List of product IDs (e.g., from catalog scraping)
3. Authenticated victim session (for testing)
4. Tools like curl or browser dev tools

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Enforce POST for modifications instead of GET
- Monitor for anomalous saved list additions from unusual referers

## Objectives

1. Confirm endpoint adds items without protection
2. Validate no CSRF token enforcement
3. Gather product IDs for chaining

## Instructions

### Step 1: Inspect Endpoint Behavior

**Context**: Use network inspection to observe the stock alert flow and test a single addition.

**Command** ([[commands/test-stock-alert-endpoint]]):
```bash
curl -X GET "https://www.lyst.com/email-capture/stock-alert/93543518/" -v
```

> This sends a GET to the endpoint with a sample product ID. Expected output includes a 200 OK or 302 redirect, and the item appears in the saved list upon login check. No CSRF token is sent or required.

### Step 2: Verify Addition

**Context**: Log in to Lyst and check the saved list to confirm unauthorized addition.

**Command** (Manual check):
```bash
# No command; use browser to navigate to saved list
```

> Manually inspect the user's saved items page. Success if the product ID is listed without prior interaction.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/test-stock-alert-endpoint]]

## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[recon]]
