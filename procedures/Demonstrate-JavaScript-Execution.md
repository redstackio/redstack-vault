---
tags:
  - xss
  - execution
  - poc-demo
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
detection_risk: low
sub_techniques: []
id: 5c748ada-9409-4be9-b3dd-841468680813
created_at: '2025-12-14T03:46:38.196Z'
updated_at: '2025-12-14T03:46:38.196Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Demonstrate-JavaScript-Execution

## Summary

This procedure validates the XSS vulnerability by accessing PoC URLs on live Atavis theme sites, triggering JavaScript alerts to prove arbitrary code execution in the victim's browser.

## Description

Using the crafted SVG payload, load specific URLs on domains like magazine.atavist.com and docs.atavist.com. The reflection executes onload handlers immediately, simulating real attacks. This step confirms impact across instances and highlights client-side risks without server interaction.

## Requirements

1. Publicly accessible target domains
2. Validated payload from prior procedure
3. Browser without XSS protections disabled for accurate testing

## Defense

Defensive measures and detection strategies:

- Deploy strict CSP headers blocking inline scripts and SVG
- Use WAF rules to strip script tags and onload attributes
- Monitor for alert() calls or unusual JS errors in client logs

## Objectives

1. Execute PoC on multiple sites
2. Capture evidence of JS runtime
3. Assess exploit reliability

## Instructions

### Step 1: Target Specific Domains

**Context**: Select vulnerable instances for demonstration.

Choose sites like https://magazine.atavist.com/category/[payload].

> Ensure the domain uses Atavis theme.

### Step 2: Load and Verify Execution

**Context**: Trigger the payload and confirm alert.

Enter the full PoC URL and press enter; watch for alert('XSS').

> Expected: Immediate popup, no user interaction needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]

