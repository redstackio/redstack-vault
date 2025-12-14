---
tags:
  - csp-bypass
  - xss
  - twitter
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 68229072-8cad-4d85-a520-e04e8c102400
created_at: '2025-12-13T23:56:20.414Z'
updated_at: '2025-12-13T23:56:20.414Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Bypass CSP for JS Execution

## Summary

This procedure bypasses Twitter's Content Security Policy using the syndication endpoint to enable arbitrary JavaScript execution.

## Description

By injecting script tags that source from allowed domains like *.twimg.com via JSONP callbacks, attackers manipulate the policy to execute code despite restrictions.

## Requirements

1. Injected XSS from prior steps
2. Knowledge of CSP allowances
3. Access to syndication.twimg.com

## Defense

Defensive measures and detection strategies:

- Tighten CSP to disallow unsafe sources
- Validate JSONP callbacks strictly

## Objectives

1. Inject bypassing script
2. Execute arbitrary JS
3. Escalate to full control

## Instructions

### Step 1: Craft Bypassing Payload

**Context**: Inject script sourcing from syndication endpoint.

Use payload injecting <script src="https://syndication.twimg.com/timeline/profile?callback=__twttr..."></script>.

> This leverages CSP allowance for *.twimg.com.

### Step 2: Manipulate Callback

**Context**: Bypass prefix restrictions.

Inject element IDs like '__twttr' to match callback requirements.

> Enables script execution in twitter.com context.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- csp-bypass
- xss
