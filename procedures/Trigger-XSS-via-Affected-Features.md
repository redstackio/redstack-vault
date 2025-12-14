---
tags:
  - xss-trigger
  - feature-interaction
  - grammarly
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: a75bc0a6-4a0d-4a73-909c-ce148eea77b4
created_at: '2025-12-13T23:56:20.272Z'
updated_at: '2025-12-13T23:56:20.272Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger XSS via Affected Features

## Summary

This procedure involves interacting with application features to execute the injected XSS payloads from crafted config overrides.

## Description

After injecting malicious configs, triggering occurs by navigating to affected areas like subscription menus or upgrade links, leading to javascript: URI execution in the browser. This enables reflected XSS in Grammarly's context.

## Requirements

1. Loaded PoC URL in browser
2. User interaction capabilities
3. Debugging tools to confirm execution

## Defense

Defensive measures and detection strategies:

- Escape and validate all dynamic URLs
- Use Content Security Policy (CSP) to block inline scripts

## Objectives

1. Execute injected script
2. Confirm XSS vulnerability
3. Assess impact like session theft

## Instructions

### Step 1: Interact with Subscription Features

**Context**: Access subscription or upgrade elements.

Navigate to the subscription menu or click upgrade links, causing redirection to the injected javascript:alert(document.domain).

> Observe the alert popup confirming execution.

### Step 2: Verify Execution in Other Features

**Context**: Test additional injected properties.

Access office add-in info or download links to trigger any remaining payloads.

> Ensure all injected URIs execute as expected.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[xss-trigger]]
- [[feature-interaction]]
