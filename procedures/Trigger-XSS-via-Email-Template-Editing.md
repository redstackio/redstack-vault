---
id: proc-trigger-xss-template-editing
tags:
  - xss
  - trigger
  - email-template
  - exfiltration
  - shopify
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
updated_at: '2025-12-13T23:52:43.965Z'
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
# Trigger-XSS-via-Email-Template-Editing

## Summary

This procedure triggers the stored XSS by editing an email template in the Shopify Email App that renders the injected store address, leading to JavaScript execution and potential data exfiltration.

## Description

Upon opening a template editor, the app fetches and displays the store address, including the malicious HTML. The payload executes in the app's context, allowing requests to internal endpoints like GraphQL and exfiltration of page elements such as CSRF tokens to external servers.

## Requirements

1. Installed Shopify Email App
2. Stored XSS payload in store address
3. Browser with network monitoring (dev tools)
4. External server ready for data receipt

## Defense

Defensive measures and detection strategies:

- Escape HTML in all template renders, especially dynamic store data
- Implement strict CSP to prevent JS execution and external requests
- Monitor for anomalous network traffic from app contexts to external domains

## Objectives

1. Execute the payload in a privileged app context
2. Exfiltrate sensitive data like CSRF tokens
3. Abuse internal APIs for further compromise

## Instructions

### Step 1: Open Email App Dashboard

**Context**: Access template management.

From Shopify admin, click the Email App icon.

> Expected: App opens to template list.

### Step 2: Select Vulnerable Template

**Context**: Choose one that includes store address rendering.

Pick a default template (e.g., order confirmation) and click Edit.

> Expected: Editor loads; payload renders, triggering onerror.

### Step 3: Monitor Execution

**Context**: Observe JS execution and exfiltration.

Open browser dev tools (Network tab) to watch for POST to https://fbs.ninja and potential GraphQL calls.

> Expected: Request sent with document.head.innerHTML; possible eval of response for further actions.

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
- [[trigger]]
- [[Exfiltration]]
