---
tags:
  - recon
  - web
  - parameter-discovery
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-13T23:52:33.811Z'
sub_techniques: []
id: 0420bb83-6e03-40c6-92b9-b4a7071e2207
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Vulnerable Path Parameter Endpoints

## Summary

This procedure involves scouting Shopify support pages to identify endpoints using the 'path' parameter, which is intended for internal routing but lacks robust validation, setting the stage for open redirect and XSS exploits.

## Description

In the context of supporthiring.shopify.com, the /apps/locksmith/resource/pages/ endpoints process a 'path' parameter for navigation. By examining these pages, attackers can confirm the parameter's presence and test for validation weaknesses. This reconnaissance step is crucial before attempting bypasses, as it reveals the attack surface without triggering defenses. Expected outcomes include mapping vulnerable URLs for subsequent exploitation, with no authentication required due to public access.

## Requirements

1. Access to a web browser for manual navigation.
2. Knowledge of URL structure in web applications.
3. Target website publicly accessible (supporthiring.shopify.com).

## Defense

Defensive measures and detection strategies:

- Implement parameter logging to monitor unusual 'path' values.
- Use Web Application Firewalls (WAF) to flag reconnaissance patterns on admin-like endpoints.
- Regular vulnerability scanning of parameter handling in routing logic.

## Objectives

1. Locate and document endpoints with exposed 'path' parameters.
2. Assess initial input acceptance for bypass potential.
3. Prepare list of targets for exploitation testing.

## Instructions

### Step 1: Navigate to Suspected Endpoints

**Context**: Start by accessing known pages under the vulnerable directory to inspect for the 'path' parameter.

Visit URLs like https://supporthiring.shopify.com/apps/locksmith/resource/pages/gauntlet-challenge and check the address bar or page source for 'path=' in query strings.

> Manual browser navigation; no command required. Expected output: Visible 'path' parameter in URL.

### Step 2: Test Basic Input

**Context**: Append a simple test value to confirm parameter processing.

Modify the URL to include ?path=test and observe if the page attempts to route or reflects the input.

> Expected output: Page loads without error, indicating acceptance of arbitrary input.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[recon]]
- [[web]]
- [[parameter-discovery]]
