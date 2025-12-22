---
tags:
  - execution
  - xss
  - observation
type: procedure
tools:
  - '[[tools/Chrome]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:53.119Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 32aeff8d-528c-4db0-aabc-b486512cf570
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-and-Observe-Stored-XSS-Execution

## Summary

This procedure views the campaign details in Twitter Ads to trigger the stored XSS payload, observing JavaScript execution that could lead to session hijacking or data theft.

## Description

Once the malicious app name is stored, rendering it in the browser without escaping executes the injected JS. This step confirms the vulnerability by loading the affected page, where the payload (e.g., img onerror=alert(1)) fires. Impact includes arbitrary script execution for any authenticated user viewing the campaign, enabling theft of cookies or phishing. Target: Web interface post-injection. Prerequisites: Successful prior injection.

## Requirements

1. Campaign with injected app active
2. Access to view campaign details
3. Browser developer tools for observation

## Defense

Defensive measures and detection strategies:

- Apply output encoding to all user-viewed stored data
- Use strict CSP to prevent JS execution from external fetches
- Alert on JS errors or anomalous script executions in client logs

## Objectives

1. Render the stored payload to execute JS
2. Confirm exploitation via alert or console
3. Assess potential for further attacks like session theft

## Instructions

### Step 1: View Campaign Details

**Context**: Load the page where the app name is displayed.

No specific command; perform in browser:

Navigate to or refresh the campaign summary/details page.

> Expected output: App name rendered, triggering the XSS (e.g., alert(1) pops up).

### Step 2: Observe Execution

**Context**: Verify JS ran using browser tools.

Open browser console (F12) and check for errors or executed code.

> Expected output: Console logs or alert confirming payload execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome]]

## Tags

- [[Execution]]
- [[xss]]
- [[observation]]
