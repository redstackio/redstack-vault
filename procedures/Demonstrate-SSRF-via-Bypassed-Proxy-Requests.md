---
id: 123e4567-e89b-12d3-a456-426614174003
name: Demonstrate-SSRF-via-Bypassed-Proxy-Requests
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:18.783Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - ssrf
  - exploitation
  - internal-access
commands: []
platforms:
  - Web
  - Proxy Service
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Demonstrate-SSRF-via-Bypassed-Proxy-Requests

## Summary

This procedure exploits the double bracket bypass in Smokescreen to perform server-side request forgery, forwarding unauthorized requests to internal or restricted domains.

## Description

In a live Smokescreen deployment, the attacker uses the validated bypass to target internal services. The scenario assumes proxy access in an application. Expected outcomes: Access to denied resources, demonstrating SSRF impact on users of the library.

## Requirements

1. Confirmed bypass from prior testing
2. Knowledge of target internal domains
3. Ability to craft and send proxied requests

## Defense

Defensive measures and detection strategies:

- Deploy comprehensive input sanitization beyond simple stripping
- Monitor proxy logs for SSRF patterns (e.g., internal IP requests)
- Use network segmentation to limit proxy reach

## Objectives

1. Forward requests to denied internal domains
2. Retrieve responses from restricted services
3. Highlight SSRF risks for Smokescreen users

## Instructions

### Step 1: Craft Exploitative Request

**Context**: Build a request using the bypass to target internals.

Use double brackets in the domain, e.g., request to "http://[[169.254.169.254/latest/meta-data/]]" for AWS metadata.

> Expected output: Payload ready for proxy submission.

### Step 2: Proxy the Request

**Context**: Send via Smokescreen to confirm forwarding.

Submit the request through the application's proxy endpoint.

> Expected output: Proxy accepts and forwards to internal endpoint.

### Step 3: Observe Impact

**Context**: Capture and analyze the unauthorized response.

Review the returned data to verify access to restricted content.

> Expected output: Internal service response, e.g., metadata or API data.

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
- [[exploitation]]
- [[internal-access]]
