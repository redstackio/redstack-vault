---
id: proc-identify-param-domxss
tags:
  - xss
  - dom-xss
  - parameter-testing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:47:12.747Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Vulnerable URL Parameter for DOM XSS

## Summary

This procedure involves testing URL parameters on web product pages to identify those that are reflected unsanitized into DOM manipulations, specifically script source attributes, enabling DOM-based XSS attacks.

## Description

In the context of teavana.com, attackers examine product pages to find parameters like pr_zip_location that influence JavaScript file loading in full.js without proper validation. This step uncovers sinks where user input is directly concatenated into script URLs, allowing protocol-relative or external injections. Prerequisites include access to the target site and basic browser inspection tools. Expected outcomes are the pinpointing of vulnerable parameters for further exploitation.

## Requirements

1. Public access to the target website (teavana.com).
2. Browser with developer tools enabled.
3. Knowledge of common URL parameter testing techniques.

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) to restrict script sources.
- Sanitize and validate all URL parameters before DOM insertion.
- Monitor for anomalous script loading in web application firewalls (WAF).

## Objectives

1. Discover parameters affecting dynamic script construction.
2. Confirm lack of sanitization in JavaScript code.
3. Prepare for PoC development.

## Instructions

### Step 1: Navigate and Inspect Product Page

**Context**: Access a sample product page and review URL structure and loaded resources.

Open http://www.teavana.com/us/en/tea/green-tea/winterberry-tea-blend-32601.html in a browser. Use developer tools (F12) to inspect the Network tab while loading the page.

> Focus on JavaScript files like full.js and search for parameter usage.

### Step 2: Test Parameter Influence

**Context**: Manipulate parameters to observe changes in script loading behavior.

Append various parameters (e.g., ?pr_zip_location=test) to the URL and reload. Check the Sources tab for how the parameter is processed in full.js, looking for concatenations like varDR=Z(DS)+"/content/"+k(DQ)+"/contents.js".

> Verify if the parameter alters the script source without escaping.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[dom-xss]]
- [[parameter-testing]]
