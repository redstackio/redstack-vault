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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:27.075Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: cabae5c5-1cb7-4c90-9756-1a6228504dcb
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft XSS Payload for Title Injection

## Summary

This procedure crafts a malicious XSS payload to inject JavaScript into Slack's sign-in page title by closing the HTML attribute and embedding an executable element.

## Description

Building on the identified reflection point, this step focuses on creating a payload that escapes the title attribute context and injects JavaScript. The target environment is the web browser rendering the Slack page. The approach uses a simple SVG onload handler for cross-browser compatibility. Prerequisites: Knowledge of HTML/JS injection techniques. Expected outcome: A valid payload that executes on reflection.

## Requirements

1. Understanding of HTML attribute breakout techniques
2. Text editor or browser console for payload testing
3. Local HTML file for safe payload validation

## Defense

Defensive measures and detection strategies:

- Sanitize all inputs with context-aware encoding (e.g., HTML for attributes)
- Validate and restrict subdomain formats at the application level
- Employ WAF rules to block common XSS payloads in parameters

## Objectives

1. Break out of the title attribute using ">
2. Inject executable JavaScript without triggering parsing errors
3. Test payload for domain-context execution

## Instructions

### Step 1: Design Basic Payload

**Context**: Create a payload to close the title and inject an alert for proof-of-concept.

Formulate the payload as "><svg onload=prompt(document.domain)>. This uses SVG for onload execution, which is less likely to be filtered.

> Explanation: The "> closes the title attribute and tag, allowing the SVG to be parsed as body content. Expected output in local test: Prompt showing current domain.

### Step 2: Validate Payload Locally

**Context**: Test the payload in an isolated HTML environment.

Create a local HTML file with <title>Test "><svg onload=prompt(1)></title> and open in browser. Confirm execution without errors.

> Expected output: Alert/prompt fires on page load, verifying syntax.

### Step 3: Adapt for Slack Context

**Context**: Ensure payload works with subdomain injection.

For subdomain use, register or use a malicious subdomain like 'payload.slack.com'. For parameters, URL-encode the payload (e.g., %22%3E%3Csvg%20onload%3Dprompt(document.domain)%3E).

> Expected output: Payload ready for insertion into URL.

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
- payload
- injection
