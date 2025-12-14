---
tags:
  - xss
  - execution
  - stored-xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 19304a9e-a21a-4e9b-8501-0b876c6d121c
created_at: '2025-12-14T03:15:35.632Z'
updated_at: '2025-12-14T03:15:35.632Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save-and-Trigger-Stored-XSS-in-Page-List

## Summary

This procedure covers saving the injected XSS payload in Concrete CMS and triggering its execution upon viewing the page list, demonstrating persistent arbitrary JavaScript execution.

## Description

After injection, submitting the form stores the payload in the database without sanitization. When any authenticated user views the page list, the title renders the payload, executing JavaScript in their browser context. This can lead to session theft via cookie access or phishing prompts, affecting all viewers until remediation. The procedure emphasizes verification through alert execution.

## Requirements

1. Injected payload from previous procedure
2. Permissions to save page list configurations
3. Ability to view the page list as a target user

## Defense

Defensive measures and detection strategies:

- Output encode all stored data on render (e.g., using Concrete CMS filters)
- Deploy client-side XSS auditors or browser extensions for detection
- Scan for anomalous JavaScript execution in user sessions via SIEM

## Objectives

1. Persist the malicious payload in the CMS storage
2. Execute JavaScript to confirm vulnerability
3. Simulate impact like alert or data exfiltration

## Instructions

### Step 1: Submit the Form

**Context**: Save the configuration to store the payload permanently.

Click 'Save' or 'Submit' on the edit form.

> Form processes without errors, updating the page list.

### Step 2: Navigate to View Page List

**Context**: Render the title to trigger execution.

Go to the page list view or dashboard where the title displays.

> Page loads, and the payload in the title executes immediately.

### Step 3: Verify Execution

**Context**: Confirm XSS success through observable effects.

Observe the alert(1) popup; in real attacks, replace with malicious code.

> Alert appears, proving arbitrary JS execution for viewers.

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
