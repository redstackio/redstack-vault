---
tags:
  - xss
  - payload-crafting
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:20.250Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 3358b9b9-533f-4883-8486-292c5a94ff64
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-XSS-Payload-for-JavaScript-Context

## Summary

This procedure focuses on designing a malicious payload tailored to the JavaScript string context in the reflected search input, allowing breakout and injection of arbitrary code like an alert for proof-of-concept.

## Description

Given the observation that the search query is reflected into an inline JavaScript string (e.g., var t = "query"), craft a payload that closes the string with a quote, injects executable code, and reopens the string to avoid syntax errors. For Informatica's endpoint, ';alert(0);t=' effectively executes alert(0) and sets t to the remaining value. This targets browser execution in the victim's context, with potential for escalation to data theft via cookie exfiltration to an attacker server.

## Requirements

1. Knowledge of JavaScript syntax and XSS payloads
2. Access to a text editor or browser console for testing
3. Understanding of the target reflection context from prior reconnaissance

## Defense

Defensive measures and detection strategies:

- Escape user input in JavaScript contexts using functions like encodeURIComponent
- Validate and sanitize all URL parameters server-side
- Employ runtime JavaScript parsers to detect injection attempts

## Objectives

1. Break out of the reflected string context
2. Inject harmless PoC code for validation
3. Prepare for delivery in a real attack scenario

## Instructions

### Step 1: Analyze Reflection Context

**Context**: Review the exact location of input reflection to tailor the payload.

From page source, confirm the JS like: var t = "<reflected_query>";

> Payload must start with " to close, then ;<code>; to execute, and resume var.

### Step 2: Construct Payload

**Context**: Build and mentally validate the injection string.

Use ';alert(0);t=' where " closes the string, alert(0) executes, and t= resumes assignment.

> Test locally in browser console: eval('var t = "';alert(0);t='";') – should alert without errors.

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
- payload-crafting
