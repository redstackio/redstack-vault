---
id: 123e4567-e89b-12d3-a456-426614174002
name: Test-Double-Bracket-Bypass-in-Domain-Validation
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:18.786Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - ssrf
  - bypass
  - domain-validation
commands: []
platforms:
  - Web
  - Proxy Service
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Test-Double-Bracket-Bypass-in-Domain-Validation

## Summary

This procedure tests the domain deny_list bypass in Smokescreen by crafting inputs with double brackets [[]] around forbidden domains, exploiting the incomplete stripping to pass validation.

## Description

Targeting Smokescreen-integrated applications, the attacker crafts malicious domain inputs to evade the filter. The environment requires access to the proxy endpoint. Outcomes include successful validation bypass, setting up SSRF exploitation.

## Requirements

1. Running Smokescreen proxy instance
2. List of denied domains (e.g., internal services)
3. HTTP client for sending test requests

## Defense

Defensive measures and detection strategies:

- Enhance bracket stripping to handle nested/multiple instances
- Log and alert on unusual domain formats in requests
- Use regex for comprehensive domain normalization

## Objectives

1. Craft inputs evading single-bracket strip
2. Confirm deny_list bypass
3. Validate potential for SSRF

## Instructions

### Step 1: Prepare Test Inputs

**Context**: Create domains with double brackets to test evasion.

Construct URLs like "http://[internal.denied.com]" but nested as "http://[[internal.denied.com]]".

> Expected output: List of test payloads ready for submission.

### Step 2: Submit Through Proxy

**Context**: Send requests via Smokescreen to check validation.

Use an HTTP client to proxy the crafted request and observe if it's forwarded without denial.

> For example, send a GET request to the proxy endpoint with the malformed domain. Expected output: No deny_list rejection; request processed.

### Step 3: Verify Bypass

**Context**: Confirm the nested brackets were not fully stripped.

Inspect proxy logs or responses to ensure the original domain reached the target.

> Expected output: Evidence of unfiltered domain access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[bypass]]
- [[domain-validation]]
