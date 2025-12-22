---
tags:
  - xss
  - parameter-discovery
  - web-vuln
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:47:18.533Z'
sub_techniques: []
id: 6f4a3409-b2a1-4576-b9ab-731f8abbd07e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Injectable-Parameter-for-XSS

## Summary

This procedure involves scanning and testing URL parameters in a web application to identify those that reflect user input without proper sanitization, serving as entry points for reflected XSS attacks. It is commonly used during web vulnerability assessments to map injection opportunities.

## Description

In the context of the MTN Caller Tunes application, the 'page' parameter in https://play.mtn.co.za/callertunez/?page=2 is examined by appending test payloads to detect reflection. The procedure targets GET parameters that are echoed back into HTML without encoding, allowing subsequent XSS exploitation. Prerequisites include access to a web browser and basic knowledge of HTML contexts. Expected outcomes include confirmation of vulnerable parameters, enabling payload crafting for JavaScript execution.

## Requirements

1. Web browser (e.g., Chrome or Firefox) with developer tools enabled.
2. Direct network access to the target URL (https://play.mtn.co.za).
3. Optional: Intercepting proxy like Burp Suite for parameter manipulation.

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to restrict script execution.
- Use input validation and output encoding (e.g., HTML entity encoding) on all user inputs.
- Monitor for anomalous URL parameters in web server logs.

## Objectives

1. Discover reflected parameters vulnerable to XSS.
2. Validate injection points by observing HTML breakage.
3. Prepare for payload testing to confirm exploitability.

## Instructions

### Step 1: Inspect Target Endpoint

**Context**: Access the endpoint and review the URL for query parameters that could accept user input.

Navigate to https://play.mtn.co.za/callertunez/?page=2 in your browser.

**Expected Output**: Page loads with pagination, showing the 'page' parameter in the URL.

### Step 2: Test for Reflection

**Context**: Append special characters to check if input is reflected unsanitized.

Modify the URL to https://play.mtn.co.za/callertunez/?page=2' and reload. View page source (Ctrl+U) to see if the quote appears raw.

**Expected Output**: Input echoed in HTML, e.g., <div>page=2'</div>, without encoding.

### Step 3: Confirm Context

**Context**: Determine the HTML context (e.g., attribute, script) for payload tailoring.

Use browser dev tools (F12) to inspect elements where the parameter is rendered.

**Expected Output**: Parameter inside an HTML attribute or tag, breakable with > or <.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- web-testing
