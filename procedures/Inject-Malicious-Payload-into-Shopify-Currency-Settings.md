---
id: proc-uuid-1
tags:
  - xss
  - stored-xss
  - injection
  - shopify
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:34.176Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Shopify-Currency-Settings

## Summary

This procedure involves injecting a malicious JavaScript payload into Shopify's store currency formatting field, exploiting a lack of proper escaping to store XSS persistently for later execution in the Buy Button channel.

## Description

In the Shopify admin panel, the 'HTML with currency' field under Settings > General > Store currency allows custom formatting but fails to sanitize inputs properly. By appending a payload like `"><img src=x onerror=prompt(document.domain)>` to the format string (e.g., `€{{amount}}`), an attacker with staff access can store executable JavaScript. This payload breaks out of the HTML attribute context and triggers on error, enabling arbitrary code execution when rendered. Prerequisites include valid staff credentials with settings edit permissions; the attack targets web-based admin interfaces and assumes no additional input validation.

## Requirements

1. Valid Shopify staff account with access to store settings
2. Web browser for navigation and payload injection
3. Knowledge of HTML/JS for crafting payloads

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and escaping for all user-controlled fields, especially HTML outputs
- Use Content Security Policy (CSP) to restrict inline script execution in admin panels
- Monitor for anomalous JavaScript alerts or DOM manipulations in audit logs

## Objectives

1. Store malicious payload persistently in backend settings
2. Ensure payload survives without immediate detection
3. Prepare for execution in downstream components like Buy Button

## Instructions

### Step 1: Access Store Settings

**Context**: Log in and navigate to the vulnerable settings page to prepare for injection.

Log in to the Shopify admin dashboard and go to Settings > General > Store currency section.

### Step 2: Modify Currency Formatting Field

**Context**: Append the payload to the 'HTML with currency' field to inject the XSS without breaking existing functionality.

Edit the 'HTML with currency' field by changing it to: `€{{amount}} "><img src=x onerror=prompt(document.domain)>`. This appends the malicious HTML after the legitimate currency output, closing any open attributes and injecting an onload-breaking img tag.

> Save the settings. If successful, no errors appear, and the payload is stored for rendering in Buy Button.

### Step 3: Verify Storage

**Context**: Refresh or check the settings to confirm the payload persists without auto-sanitization.

Reload the settings page; the field should retain the injected content.

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
- [[stored-xss]]
- [[shopify]]
