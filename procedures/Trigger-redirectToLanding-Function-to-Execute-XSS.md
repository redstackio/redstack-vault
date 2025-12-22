---
tags:
  - xss-execution
  - gocd
  - javascript
type: procedure
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
updated_at: '2025-12-13T23:52:49.921Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: df7e9eda-6eef-498f-adc2-4a8de4395c06
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-redirectToLanding-Function-to-Execute-XSS

## Summary

This procedure executes the crafted XSS payload by loading the malicious URL in a browser, triggering the redirectToLanding function in GoCD's loading page to run arbitrary JavaScript.

## Description

With the malicious URL prepared, access it during GoCD server startup when the loading page is active. The function automatically invokes, parsing the redirect_to parameter and executing the javascript:alert("XSS") via decodeURIComponent and window.location assignment. This results in reflected XSS, potentially stealing session cookies (e.g., via document.cookie) or performing actions. Targets browser contexts on web platforms; limited to startup phase.

## Requirements

1. Running GoCD instance in startup mode
2. Crafted malicious URL from prior procedure
3. Victim browser (or controlled environment for testing)

## Defense

Defensive measures and detection strategies:

- Disable or refactor direct window.location assignments from user input
- Implement browser-side sandboxing or no-script modes
- Detect via web application firewall rules for javascript: in parameters

## Objectives

1. Execute injected JavaScript in the page context
2. Demonstrate impact like alert popup or data exfiltration
3. Validate exploitation success for reporting

## Instructions

### Step 1: Prepare Environment

**Context**: Ensure the loading page is accessible.

Start or wait for GoCD server startup to display new.loading.page.html.

**Expected Output**: Loading page loads without errors.

### Step 2: Load Malicious URL

**Context**: Deliver the payload to trigger the function.

Enter or navigate to http://target-gocd/loading/new.loading.page.html?redirect_to=javascript:alert("XSS") in the browser address bar.

**Expected Output**: Page loads, function triggers, and alert("XSS") pops up.

### Step 3: Observe and Escalate Impact

**Context**: Verify execution and potential for further abuse.

In a real attack, replace alert with code to exfiltrate document.cookie or perform clicks; here, confirm execution.

**Expected Output**: JavaScript runs, e.g., alert displayed; console logs show window.location change.

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

- xss-execution
- gocd
- javascript
