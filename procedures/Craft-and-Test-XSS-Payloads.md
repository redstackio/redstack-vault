---
tags:
  - xss
  - payload-crafting
  - poc
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
id: 87e1fc65-f67e-4f73-8bf9-4173d68ff7ee
created_at: '2025-12-14T03:46:38.200Z'
updated_at: '2025-12-14T03:46:38.200Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-and-Test-XSS-Payloads

## Summary

This procedure focuses on creating URL-encoded XSS payloads using SVG elements to bypass filters and test injection into category slugs, confirming JavaScript execution upon reflection.

## Description

Payloads exploit the lack of HTML encoding by breaking out of attributes or tags with sequences like "> <svg onload=alert(`XSS`)>. URL encoding ensures delivery via the slug parameter. Testing involves loading the crafted URL in a browser on vulnerable sites. Outcomes include successful alert popups, demonstrating arbitrary code execution potential for attacks like cookie theft.

## Requirements

1. URL encoding capability (browser console or online tool)
2. Vulnerable /category/ endpoint confirmed
3. Clean browser session to avoid CSP interference

## Defense

Defensive measures and detection strategies:

- Encode all outputs using libraries like OWASP ESAPI
- Validate and sanitize slug inputs server-side
- Log and alert on URLs with high entropy or encoded scripts

## Objectives

1. Inject and execute JavaScript via reflected slug
2. Validate payload efficacy across contexts
3. Document PoC for reporting

## Instructions

### Step 1: Encode Payload

**Context**: Create a safe, executable payload that triggers an alert.

Use a tool or console to encode "><svg onload=alert(`XSS`)> as %22%3E%3Csvg%20onload%3Dalert%60XSS%60%3E.

> This payload closes any open attribute and injects an SVG with onload handler.

### Step 2: Construct and Test URL

**Context**: Deliver the payload via the category slug and observe execution.

Build https://target.com/category/%22%3E%3Csvg%20onload%3Dalert%60XSS%60%3E and load in browser.

> Expected: Page loads with 'XSS' alert, confirming reflection and execution.

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
- [[payload-crafting]]

