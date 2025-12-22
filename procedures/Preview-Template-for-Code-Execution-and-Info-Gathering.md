---
id: proc-uuid-2
name: Preview-Template-for-Code-Execution-and-Info-Gathering
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:23:24.266Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - rce
  - info-disclosure
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Preview Template for Code Execution and Info Gathering

## Summary

This procedure triggers the execution of injected Liquid code by previewing the notification template, allowing an attacker to view disclosed information such as object methods, class details, and YAML dumps without alerting users via email.

## Description

Once malicious code is inserted, previewing the template in Shopify's editor causes the Liquid engine to render it against a sample order object. This executes the injected method calls, outputting sensitive data directly in the browser. It's ideal for initial reconnaissance of available methods and properties, confirming the vulnerability before exfiltration. The impact is limited to parameterless methods, but sufficient for discovering hashed passwords and other hidden fields on objects like OrderDrop.

## Requirements

1. Malicious code already injected into a notification template
2. Shopify admin access to the template editor
3. A sample order or draft for preview context

## Defense

Defensive measures and detection strategies:

- Disable or sandbox preview functionality for templates with untrusted input
- Log all preview actions and scan rendered output for anomalies (e.g., YAML dumps)
- Use content security policies to restrict template rendering

## Objectives

1. Execute injected code to list available methods and dump objects
2. Gather intelligence on Ruby object structure for further exploitation
3. Validate vulnerability without external notifications

## Instructions

### Step 1: Select Template for Preview

**Context**: Ensure the edited template is open in the admin editor.

No command required; stay in the Notifications > New Order template editor.

> Verify the malicious code is present in the body.

### Step 2: Trigger Preview

**Context**: Render the template to execute Liquid code.

No command required; click the "Preview" button in the editor.

```liquid
The preview will render: {{ methods | json }} {{ systemu }} {{ class }} {{ to_yaml }}
```

> Output appears in the preview pane, showing JSON of methods, system info, class name, and full YAML dump of the order object.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript (via Liquid execution)

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- rce
- info-disclosure
- shopify
