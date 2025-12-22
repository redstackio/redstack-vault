---
id: uuid-placeholder-1
tags:
  - xss
  - reflected-xss
  - javascript
  - web
  - uber
  - krux
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:50.074Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Reflected-XSS-via-kxsrc-Parameter

## Summary

This procedure exploits a reflected Cross-Site Scripting (XSS) vulnerability in the 'kxsrc' parameter on Uber's website by crafting a URL that injects malicious JavaScript through the third-party Krux beacon service (beacon.krxd.net). It enables arbitrary code execution in the victim's browser, suitable for testing or demonstrating impacts like session hijacking on affected subdomains.

## Description

The vulnerability arises from insufficient validation of the kxsrc parameter, which is used to construct a URL for the Krux beacon's optout_check endpoint. By URL-encoding a callback parameter with JavaScript (e.g., alert('/XSSED/')), the beacon service injects and executes the code when the page loads. This affects www.uber.com and subdomains like partners.uber.com, getrush.uber.com, etc. Prerequisites include a web browser and public access to the target site; no authentication is needed. Expected outcomes include confirmed JS execution, highlighting risks of data theft or phishing.

## Requirements

1. Web browser with developer tools enabled for monitoring
2. Public internet access to Uber domains and beacon.krxd.net
3. Basic knowledge of URL encoding and JavaScript payloads

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and validation for URL parameters like kxsrc, rejecting or escaping callback injections
- Deploy Content Security Policy (CSP) to block inline scripts and third-party callbacks
- Monitor network traffic for anomalous requests to beacon services with encoded payloads
- Use Web Application Firewall (WAF) rules to detect XSS patterns in query parameters

## Objectives

1. Inject and execute arbitrary JavaScript in the browser context
2. Demonstrate potential for stealing session cookies or user data
3. Validate vulnerability across multiple subdomains for broader impact assessment

## Instructions

### Step 1: Craft the Malicious URL

**Context**: Encode the JavaScript payload in the callback parameter of the Krux beacon URL, then append it to the kxsrc parameter on the target page.

No specific command required; manually construct the URL: https://www.uber.com/?kxsrc=https%3A//beacon.krxd.net/optout_check%3Fcallback%3Dalert%28/XSSED/.source%29.

> This URL passes the encoded callback to the beacon service without sanitization.

### Step 2: Load the URL in Browser

**Context**: Visit the crafted URL to trigger the reflected payload during page load.

Open the URL in a browser and inspect the network tab for the beacon request.

> The page renders normally, but the beacon fetches and executes the JS.

### Step 3: Verify Execution

**Context**: Observe the effects of the injected JavaScript to confirm successful exploitation.

Check for the alert dialog or console logs; in production, inspect for data exfiltration.

> Alert('/XSSED/') confirms execution; replace with document.cookie for real impact.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[JavaScript]]
- [[web]]
- [[uber]]
- [[krux]]
