---
tags:
  - xss
  - recon
  - web-testing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 7402cc19-3dfa-43c3-9abb-8e7f56728a7d
created_at: '2025-12-14T03:46:31.747Z'
updated_at: '2025-12-14T03:46:31.747Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Identify-Vulnerable-XSS-Parameters-in-ASP-Endpoints

## Summary

This procedure involves analyzing POST requests to ASP endpoints like /o/Default.asp and /r/Default.asp on uk.informatica.com to pinpoint parameters (PageLink, ResponseHandlingLanguage, UID) that lack proper sanitization, allowing reflected XSS payloads to be injected and executed.

## Description

In the context of web vulnerability assessment, this procedure targets opt-out forms on legacy ASP applications. By intercepting traffic and testing parameters with benign payloads, attackers identify reflection points. The target environment is a web server on port 80 running ASP, vulnerable due to unescaped user input in responses. Prerequisites include network access and a proxy like Burp Suite for request manipulation. Successful identification enables follow-on exploitation for JavaScript execution, leading to high-impact attacks like session theft.

## Requirements

1. Network access to uk.informatica.com on port 80
2. Web proxy tool for request interception and modification
3. Basic knowledge of HTTP POST requests and HTML contexts

## Defense

Defensive measures and detection strategies:

- Implement input validation and output encoding (e.g., HtmlEncode in ASP)
- Use Content Security Policy (CSP) to block inline scripts
- Monitor for anomalous request patterns with WAF logs

## Objectives

1. Discover unsanitized parameters in POST data
2. Confirm reflection without escaping
3. Prepare for payload crafting

## Instructions

### Step 1: Intercept Opt-Out Form Submission

**Context**: Submit the opt-out form normally to capture the baseline POST request structure.

Navigate to the opt-out page and submit with sample data, proxying through Burp or similar to log the request to /o/Default.asp or /r/Default.asp.

**Expected Output**: Raw POST body with parameters like PageLink=1, UID=, etc.

### Step 2: Test Parameters for Reflection

**Context**: Append test payloads to each parameter and resubmit to check if they appear unsanitized in the HTML response.

Modify the captured request: For PageLink, add '>test<'; for UID, add " onmouseover="alert(1). Observe the response body for unescaped output.

**Expected Output**: Payload reflected as-is, e.g., value=">test<" in HTML attribute.

### Step 3: Validate XSS Potential

**Context**: Escalate to simple script payloads to confirm execution feasibility.

Inject <script>alert(1)</script> into identified parameters and load the response in a browser.

**Expected Output**: Alert box if vulnerable; no execution if sanitized.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Reconnaissance]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[recon]]
- [[web-testing]]
