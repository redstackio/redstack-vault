---
id: proc-trigger-stored-xss-template
tags:
  - xss
  - trigger
  - shopify
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:49.959Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-via-Template-Selection

## Summary

This procedure triggers the stored XSS payload by rendering the tainted store name in a pre-built email template, executing arbitrary JavaScript in the Shopify admin panel.

## Description

Once the payload is stored, selecting a template causes the store name to be inserted into the email editor or preview without proper escaping, firing the JavaScript. This leads to execution in the admin context, potentially allowing alerts, data exfiltration, or further attacks like accessing employee dashboards. Targets Shopify web interfaces post-injection.

## Requirements

1. Previously injected XSS payload in store name
2. Access to email template editor in Shopify Email app
3. Admin session active

## Defense

Defensive measures and detection strategies:

- Escape outputs in all template rendering contexts (e.g., use safe HTML rendering libraries)
- Monitor for JavaScript errors or alerts in admin sessions via browser logs
- Audit template selections for anomalous behavior

## Objectives

1. Render the vulnerable store name in template context
2. Execute injected JavaScript for proof-of-concept or escalation
3. Demonstrate impact like domain alerting or data access

## Instructions

### Step 1: Navigate to Template Selector

**Context**: Access the area where templates are chosen and rendered.

No command required; use the UI:

- From Shopify Email app, go to Templates or Editor section
- Ensure the injected store name is part of the branding

> Templates list loads, ready for selection.

### Step 2: Select and Render Template

**Context**: Choose a pre-built template to force rendering of the store name.

No command required; use the UI:

- Pick any pre-built template (e.g., newsletter or order confirmation)
- View the template preview or editor

> The onerror event triggers, executing alert(document.domain).

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
