---
tags:
  - xss
  - reflected-xss
  - parameter-injection
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
updated_at: '2025-12-13T23:52:44.107Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 08146955-2c61-4dca-9c22-de869642ed82
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Identify-Reflected-XSS-in-Location-Parameter

## Summary

This procedure identifies a reflected XSS vulnerability in the 'location' parameter of the Twitter careers search page by testing for direct reflection of user input into HTML attributes without sanitization.

## Description

The attack targets https://careers.twitter.com/en/jobs-search.html?location=, where the parameter value is inserted into an HTML attribute like <input value="[user input]"> without proper escaping. This allows attackers to break out of the attribute using quotes and inject a script tag. The procedure involves manual testing with payloads to confirm reflection and breakout potential, setting the stage for payload execution in a web browser environment. Expected outcomes include confirmation of injection points that could lead to arbitrary JavaScript execution.

## Requirements

1. Web browser with developer tools (e.g., Chrome DevTools for inspecting HTML)
2. URL encoding tool or built-in browser encoding for crafting payloads
3. Public internet access to the target URL

## Defense

Defensive measures and detection strategies:

- Implement output encoding for HTML attributes (e.g., using HTML entity encoding)
- Deploy a Web Application Firewall (WAF) to detect and block XSS payloads in query parameters
- Enforce strict Content Security Policy (CSP) to limit script sources, though this procedure assumes a bypass exists

## Objectives

1. Confirm unsanitized reflection of the 'location' parameter in HTML
2. Validate attribute breakout capability for script injection
3. Identify potential for chaining with other exploits like CSP bypass

## Instructions

### Step 1: Test Basic Reflection

**Context**: Visit the target page and append a simple test string to check if input is echoed back unchanged.

Navigate to: https://careers.twitter.com/en/jobs-search.html?location=test

Inspect the page source in browser developer tools to locate the reflected input in an HTML attribute.

> Look for <input type="text" value="test" ...> or similar; if 'test' appears unencoded, proceed.

### Step 2: Attempt Attribute Breakout

**Context**: Craft a payload to escape the attribute and inject a benign tag to confirm control.

Use payload: ?location=1%22%3E%3Cimg%20src=x%20onerror=alert(1)%3E

Visit the URL and check if an alert triggers or if the img tag is injected.

> Success if the attribute closes prematurely and the img executes; this confirms XSS feasibility.

### Step 3: Refine for Script Injection

**Context**: Build toward full script tag injection by testing quote breakout.

Payload: ?location=1%22%3E%3Cscript%3Ealert(document.domain)%3C/script%3E

Observe if the script executes, noting any CSP blocks for later bypass.

> Expected: Script reflection without execution due to CSP, but structure intact.

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
- [[reflected-xss]]
