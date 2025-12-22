---
tags:
  - xss-trigger
  - preview-execution
  - session-theft
type: procedure
tools: []
tactics:
  - '[[Collection]]'
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:33.717Z'
sub_techniques: []
id: eff32dfe-fc99-43e8-8027-3a915995de96
validated: true
mitre_tactics:
  - '[[Collection]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-in-App-Preview

## Summary

This procedure describes triggering the stored XSS payload by previewing app changes and viewing the example store, causing JavaScript execution in the attacker's or victim's browser on the Shopify domain.

## Description

After injecting a payload into the URL fields, clicking 'Preview changes' and then 'View example store' renders the stored content, executing the JavaScript without escaping. This runs in the high-privilege context of apps.shopify.com, allowing access to session cookies or page data for authenticated users. The attack relies on social engineering to lure victims to preview the app or occurs automatically if the attacker previews in a shared environment.

## Requirements

1. Injected payload in a URL field
2. Access to the preview functionality on the edit page
3. Victim or test browser session on apps.shopify.com

## Defense

Defensive measures and detection strategies:

- Escape user-controlled content in preview renders
- Implement strict CSP to block inline JavaScript
- Log and alert on preview executions with anomalous behavior

## Objectives

1. Execute arbitrary JavaScript in victim context
2. Steal session data or perform actions
3. Confirm exploitation success

## Instructions

### Step 1: Initiate Preview

**Context**: Load the preview to render stored content.

On the edit page, after saving the payload, click the 'Preview changes' button.

> Expected output: Preview interface loads with app details.

### Step 2: View Example Store

**Context**: Trigger the payload execution.

In the preview, click 'View example store' to display the vulnerable rendered URL.

> Expected output: JavaScript executes, e.g., alert dialog or network request to attacker server.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]
- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- execution
- preview
