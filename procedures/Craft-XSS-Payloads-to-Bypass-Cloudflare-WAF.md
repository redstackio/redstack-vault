---
id: proc-uuid-002
tags:
  - xss
  - waf-bypass
  - payload-crafting
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:21.117Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Craft-XSS-Payloads-to-Bypass-Cloudflare-WAF

## Summary

This procedure focuses on creating and testing obfuscated XSS payloads that evade Cloudflare WAF detection by using URL encoding, mixed casing, and HTML attributes like IMG SRC or A HREF to inject scripts or load external resources.

## Description

Attackers target Cloudflare-protected inputs where standard XSS is filtered but crafted variants slip through due to incomplete rule coverage. The approach involves encoding parts of the payload (e.g., URL-encoding tags) and using event handlers or external links to trigger execution. Prerequisites: A confirmed reflective input from prior recon. Outcomes: WAF accepts the payload, allowing reflection and potential execution. This is common in web apps with partial sanitization.

## Requirements

1. Knowledge of URL encoding and HTML attributes.
2. Access to the vulnerable input endpoint.
3. Attacker-controlled external domain for payload verification.

## Defense

Defensive measures and detection strategies:

- Update WAF rules to detect encoded payloads and attribute-based injections.
- Employ client-side escaping libraries like DOMPurify.
- Log and alert on external resource loads from user inputs.

## Objectives

1. Generate payloads that avoid WAF signature matches.
2. Test for acceptance and reflection.
3. Enable external resource loading as a bypass indicator.

## Instructions

### Step 1: Encode Basic Payload Components

**Context**: Break down XSS tags into encoded fragments to obscure from WAF scanners.

Create a payload like `Mega7%3EXSS%3CIMG/SRC=https://www.notebookcheck.net/fileadmin/Notebooks/News/_nc3/hacker21.jpg` (decodes to Mega7>XSS<IMG SRC=external).

> Submit to input; check if WAF passes it (no block).

### Step 2: Test Non-Encoded Attribute Variants

**Context**: Use unencoded tags with attributes that trigger on load or click.

Try `Mega7>XSS<A/href=https://evil.com>` in the input, focusing on HREF for redirects.

> Expected: Reflection without stripping; click to test redirect.

### Step 3: Iterate and Refine Payloads

**Context**: Adjust casing (e.g., <ImG SrC=...) or add whitespace to evade rules.

Resubmit variations until WAF accepts; use dev tools to decode and verify structure.

> Success: Payload reflected intact, ready for execution test.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[waf-bypass]]
- [[payload-crafting]]
