---
tags:
  - xss
  - execution
  - trigger
  - concrete-cms
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:25.111Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: a59f88b9-25f6-4be8-af51-eb69715babd6
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-by-Viewing-Entries

## Summary

This procedure triggers the execution of the stored XSS payload in Concrete CMS v8.1.0 by navigating to the Express entries page, causing the injected JavaScript to run in the viewer's browser context.

## Description

After payload injection, visiting /index.php/dashboard/express/entries or /index.php/dashboard/system/express/entities renders the unsanitized 'name' field, executing the script (e.g., onload event in SVG). This affects any authenticated user, enabling attacks like session hijacking. Prerequisites: Payload already stored; outcomes: Immediate JavaScript execution in the browser.

## Requirements

1. Payload successfully injected and stored
2. Authenticated session (any user viewing the page)
3. Access to the entries endpoints
4. Web browser to observe execution

## Defense

Defensive measures and detection strategies:

- Output encoding when rendering stored data (e.g., htmlspecialchars in PHP)
- Browser-based protections like XSS auditors or extensions
- Logging and alerting on JavaScript errors or unexpected popups

## Objectives

1. Execute the stored malicious script
2. Demonstrate impact on victim browsers
3. Enable further exploitation (e.g., data exfiltration)

## Instructions

### Step 1: Navigate to Entries Page

**Context**: Access the page where the payload is rendered.

Visit /index.php/dashboard/express/entries in the browser.

> Expected output: Page loads, and if payload is present, script executes automatically.

### Step 2: Observe Execution

**Context**: Verify the XSS trigger through visible effects.

Look for the confirm dialog or other payload effects (e.g., alert with document.domain).

> Expected output: JavaScript runs, potentially showing an alert or performing actions like cookie theft.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- xss
- execution
