---
id: proc-identify-xss-params
tags:
  - xss
  - recon
  - web-testing
  - parameter-discovery
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
updated_at: '2025-12-14T03:15:41.469Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-XSS-Vulnerable-Parameters-in-Web-Endpoints

## Summary

This procedure involves manually testing web endpoints for reflected input parameters that lack proper sanitization, focusing on query strings like 'currency' to identify potential XSS entry points by observing HTML reflection.

## Description

In a typical attack scenario, attackers probe public-facing web applications like WordPress.com's /website/ endpoint to find unsanitized parameters. By appending test values and inspecting the response HTML, vulnerabilities such as attribute context reflections are uncovered. This step requires no special tools, just a browser, and sets the stage for payload injection. Expected outcomes include pinpointing reflection sites that allow context breakout, leading to JavaScript execution in subsequent steps.

## Requirements

1. Web browser with developer tools (e.g., Chrome DevTools)
2. Direct network access to the target endpoint (e.g., https://wordpress.com/website/)
3. Basic knowledge of HTML and URL query parameters

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) to restrict script execution
- Use input validation and output encoding (e.g., htmlspecialchars in PHP) on all reflected parameters
- Monitor for anomalous query parameters in web logs using WAF rules

## Objectives

1. Discover parameters that reflect user input without escaping
2. Map reflection contexts (e.g., attributes, tags) for exploitation planning
3. Validate initial vulnerability without triggering alerts

## Instructions

### Step 1: Access and Probe Endpoint

**Context**: Navigate to the target endpoint and introduce test parameters to observe reflection.

Access https://wordpress.com/website/ in your browser. Append ?currency=TEST and load the page. Open developer tools (F12), go to the Elements tab, and search for 'TEST' in the HTML source to locate the reflection point, such as within a <title> tag or attribute.

> If 'TEST' appears unescaped (e.g., <title currency="TEST">), it's a potential injection site. No command execution; this is manual inspection.

### Step 2: Test for Breakout Feasibility

**Context**: Escalate testing by injecting partial payloads to confirm lack of sanitization.

Modify the URL to ?currency="<test> and reload. Inspect if the quotes or tags disrupt the HTML structure without errors, indicating breakout potential.

> Successful disruption (e.g., malformed attributes in source) confirms vulnerability for full payloads.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[recon]]
- [[web-testing]]
