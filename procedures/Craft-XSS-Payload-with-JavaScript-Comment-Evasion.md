---
id: proc-xss-craft-001
tags:
  - xss
  - javascript
  - payload-crafting
  - filter-evasion
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
updated_at: '2025-12-13T23:52:39.496Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft XSS Payload with JavaScript Comment Evasion

## Summary

This procedure crafts a reflected XSS payload exploiting parameter pollution on IRCCloud's badges page, using JavaScript comments to close HTML attributes and inject a script tag, effectively bypassing robust XSS filters for arbitrary code execution.

## Description

The attack leverages the earlier identified parameter pollution to manipulate the 'hostname' output, inserting a payload that uses comments (/* and //) to prematurely close tags like <script type="text/javascript" src="hostname"> and inject alert('XSS\n-Rohit Dua'). This targets web applications with strong but incomplete filtering, in authenticated browser contexts. Outcomes include JavaScript execution for session theft or phishing. Requires knowledge of HTML/JS and the pollution vuln.

## Requirements

1. Confirmed parameter pollution on target page
2. Web browser developer tools for testing payloads
3. Understanding of HTML attribute injection and JS comments

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs with context-aware encoding (e.g., HTML entity encoding for attributes)
- Implement Content Security Policy (CSP) to block inline scripts
- Scan for comment-based evasion patterns in WAF rules and monitor for unusual JS execution

## Objectives

1. Bypass XSS filters using pollution and comments
2. Inject functional script tag
3. Prepare payload for execution without detection

## Instructions

### Step 1: Analyze Page Structure

**Context**: Examine how 'hostname' is reflected in the page.

Load www.irccloud.com/badges and use browser dev tools to find 'hostname' in script src or attributes.

> Expected: Identification of injectable points, e.g., <script src="hostname">

### Step 2: Build Base Payload

**Context**: Use pollution to insert closing quotes and tags.

Start with ?hostname=hostname" type="text/javascript"> to close attributes and open a script.

> Expected: Partial injection without errors.

### Step 3: Add Comment Evasion and Payload

**Context**: Incorporate comments to hide from filters and add execution.

Extend to ?hostname=hostname" type="text/javascript"> /*&hostname=*/alert('XSS\n-Rohit Dua'); //

> Expected: Full payload that evades filters and executes alert on load.

### Step 4: Test Payload

**Context**: Iterate in browser to refine.

Enter URL and check for execution; adjust comments if filtered.

> Expected: Alert fires, confirming evasion.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- evasion
- javascript
