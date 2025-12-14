---
id: proc-trigger-xss-execution-on-import
tags:
  - xss
  - javascript-execution
  - payload-trigger
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
updated_at: '2025-12-14T03:15:36.220Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Execution-on-Import

## Summary

This procedure finalizes the XSS attack by rendering the malicious contact in Respondly, executing the JavaScript payload in the browser context.

## Description

Upon completing the import, Respondly outputs the contact names to the page without HTML escaping, causing the script in the malicious name to run. This can lead to session hijacking or data theft. Requires the prior steps; outcomes include arbitrary code execution on the Respondly domain.

## Requirements

1. Malicious contact present in the victim's Gmail
2. Import process initiated and fetching data
3. Victim's browser session active on Respondly

## Defense

Defensive measures and detection strategies:

- Enforce strict input validation and output encoding for all user data
- Implement XSS filters or WAF rules for script tags
- Monitor browser console for unexpected script execution or network requests

## Objectives

1. Render the unsanitized contact name in HTML
2. Execute the JavaScript payload client-side
3. Achieve impacts like cookie theft or account takeover

## Instructions

### Step 1: Complete Import Confirmation

**Context**: Finalize the process to trigger rendering.

In Respondly, review the contact preview if shown, and click 'Import' or 'Save Contacts' to process the list.

### Step 2: Observe Rendering

**Context**: The UI displays contacts, injecting the payload.

Watch as the page updates with the contact list; the malicious name will be inserted as raw HTML, e.g., via innerHTML without escaping.

### Step 3: Verify Execution

**Context**: Confirm the XSS fires.

Open browser dev tools (F12), check the console for errors or alerts, and monitor the Network tab for exfiltration requests (e.g., to attacker.com with cookie data).

> Successful execution: Payload runs, potentially alerting 'XSS' or sending data.

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
- [[javascript-execution]]
- [[payload-trigger]]
