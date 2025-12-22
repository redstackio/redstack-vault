---
tags:
  - xss
  - trigger
  - concrete-cms
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - PHP
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 03b80cd4-43cd-47d2-9920-8d9e7e7ee408
created_at: '2025-12-14T00:11:09.643Z'
updated_at: '2025-12-14T00:11:09.643Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-by-Editing-Attribute

## Summary

This procedure triggers the stored XSS by re-editing the attribute in Concrete CMS, causing the malicious payload to render and execute in the browser context.

## Description

After injection, revisiting the edit interface for the select attribute renders the option values without escaping, executing the JS payload. This affects admin pages like /index.php/dashboard/pages/attributes/edit/xxx and Express Form blocks. In unauthenticated scenarios, if the attribute is used in public forms allowing additions, any visitor viewing the form triggers it. The root cause is in concrete/attributes/select/type_form.php at line 40, where echo statements output raw input. Outcomes include alert dialogs for testing or session theft via cookie exfiltration.

## Requirements

1. Select attribute with injected XSS payload
2. Access to edit the attribute (admin) or view Express Form (any user)
3. Vulnerable Concrete CMS version

## Defense

Defensive measures and detection strategies:

- Apply patches for Concrete CMS XSS vulnerabilities
- Implement client-side escaping in attribute rendering forms
- Log and alert on JS errors or unexpected script executions in admin sessions

## Objectives

1. Execute the stored JavaScript in the target context
2. Achieve session compromise or data theft
3. Demonstrate persistence for all affected users

## Instructions

### Step 1: Revisit Attribute Edit Page

**Context**: Load the page that renders the stored options to trigger execution.

Navigate to the attribute edit URL, e.g., /index.php/dashboard/pages/attributes/edit/[attribute-id]. The options list will display the payload.

> Upon loading, the <script> tag executes immediately in the DOM.

### Step 2: Observe and Escalate Impact

**Context**: Verify execution and adapt for real attacks.

Watch for the alert('XSS') dialog. In production, replace with exfiltration: inspect network requests for cookie sends to attacker server. For Express Forms, add the attribute to a block via Dashboard > Blocks > Express Forms, then view the form publicly.

> Success confirms the vuln; escalation could involve phishing or full takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
