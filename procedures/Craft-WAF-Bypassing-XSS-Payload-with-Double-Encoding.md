---
tags:
  - xss
  - waf-bypass
  - encoding
type: procedure
tools:
  - '[[tools/PortSwigger-XSS-Cheat-Sheet]]'
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:38.437Z'
sub_techniques: []
id: 43901eae-d2f8-4e34-bd05-fc8defa018d1
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-WAF-Bypassing-XSS-Payload-with-Double-Encoding

## Summary

This procedure creates an XSS payload that evades Glassdoor's WAF by using double HTML entity encoding combined with URL encoding, allowing injection of a JavaScript-executing img tag onerror handler.

## Description

The WAF blocks direct XSS attempts, but encoding techniques like &amp;#x00028; for '(' bypass filters. This step builds on initial injection by escalating to script execution, referencing cheat sheets for payload ideas, and prepares for full compromise.

## Requirements

1. Knowledge of HTML/URL encoding
2. Access to XSS payload resources like PortSwigger cheat sheet
3. Prior verification of basic injection

## Defense

Defensive measures and detection strategies:

- Normalize and decode inputs multiple times before validation
- Update WAF signatures for encoded payloads
- Implement allowlisting for parameter values

## Objectives

1. Generate a payload that avoids WAF detection
2. Ensure JavaScript execution capability
3. Test for broader exploit potential

## Instructions

### Step 1: Design the Core Payload

**Context**: Start with a simple XSS like <img src onerror=confirm(1)>.

Encode it doubly: Use &gt;&lt;img+src+onerror=confirm&amp;#x00028;1&amp;#x00029;&gt;

> This uses hexadecimal entities to obscure parentheses and amp for &.

### Step 2: Apply URL Encoding

**Context**: Encode the entire string for URL parameter.

Final encoded payload: %22%26gt%3B%26lt%3Bimg+src+onerror%3Dconfirm%26amp%3B%23x00028%3B1%26amp%3B%23x00029%3B%26gt%3B

> Integrate into filter.jobTitleExact as in the base URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/PortSwigger-XSS-Cheat-Sheet]]
- [[tools/Firefox]]
- [[tools/Chrome]]

## Tags

- [[xss]]
- [[waf-bypass]]
- [[encoding]]
