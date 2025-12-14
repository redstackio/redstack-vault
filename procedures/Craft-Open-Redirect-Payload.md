---
id: proc-craft-open-redirect-payload
name: Craft-Open-Redirect-Payload
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.280Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - open-redirect
  - payload-crafting
  - url-manipulation
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Craft-Open-Redirect-Payload

## Summary

This procedure crafts payloads exploiting tag stripping in Starbucks websites to enable open redirects to arbitrary external sites, such as using '<>//google.com' which becomes //google.com after '<>' removal, facilitating phishing attacks.

## Description

Targeting GET parameters and root URLs, the procedure leverages the application's stripping of '<>' tags, allowing protocol-relative redirects. This is applicable in scenarios where users are tricked into clicking malicious links, leading to external site navigation. Outcomes include successful redirection without authentication barriers.

## Requirements

1. Knowledge of target parameter names (e.g., prefn1, prefv1)
2. Web browser for testing
3. Target sites like shop.starbucks.de

## Defense

Defensive measures and detection strategies:

- Validate and whitelist allowed redirect domains
- Strip or block protocol-relative URLs in redirects
- Implement referrer checks for cross-origin navigation

## Objectives

1. Bypass input stripping to chain redirects
2. Redirect users to malicious external resources
3. Enable social engineering via phishing

## Instructions

### Step 1: Construct Basic Payload

**Context**: Build a payload that survives stripping to form a valid redirect.

Use structure '<>//google.com' in a GET parameter like ?prefv1=<>//google.com.

> Append to the target URL and load; after stripping, it redirects to google.com.

### Step 2: Test Chained Redirect

**Context**: Verify the payload triggers external navigation.

Observe the browser's location change.

> Success if it navigates away from the Starbucks domain to the external site.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[open-redirect]]
- [[payload-crafting]]
