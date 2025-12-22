---
id: proc-uuid-2
tags:
  - xss
  - execution
  - shopify
  - buy-button
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
updated_at: '2025-12-13T23:52:34.164Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-via-Buy-Button-Access

## Summary

This procedure triggers the stored XSS payload by accessing the Buy Button sales channel, causing the unsanitized currency formatting to render and execute arbitrary JavaScript in the victim's browser context.

## Description

Once the payload is stored in the currency settings, accessing the Buy Button feature (via admin or embedded page) renders the tainted HTML, executing the injected script. The payload `"><img src=x onerror=prompt(document.domain)>` triggers an alert confirming execution, but in a real attack, it could exfiltrate cookies or perform actions for account takeover. This targets the web platform, requiring the attacker to lure or directly access as a staff member; outcomes include JS execution in the channel's domain, potentially compromising sessions.

## Requirements

1. Payload already injected via prior procedure
2. Access to Buy Button sales channel (admin or public embed)
3. Victim browser context (e.g., another staff member's session)

## Defense

Defensive measures and detection strategies:

- Sanitize all rendered outputs in sales channels, escaping HTML entities
- Implement output encoding for currency fields in templates
- Log and alert on unexpected JS execution or error events in browser consoles

## Objectives

1. Render the stored payload to execute JavaScript
2. Confirm control over the victim's DOM
3. Enable escalation to account takeover

## Instructions

### Step 1: Navigate to Buy Button

**Context**: Access the feature that pulls and renders the currency settings.

In the Shopify admin, go to Sales Channels > Buy Button, or embed a Buy Button on a test page.

### Step 2: Render the Payload

**Context**: Load the page or component to trigger rendering of the tainted currency field.

View or interact with the Buy Button; the payload should inject into the HTML output, causing the img tag to fail loading and fire the onerror event.

> An alert box appears with the document domain (e.g., 'shopify.com'), verifying execution. For takeover, replace prompt with code to steal session tokens.

### Step 3: Validate Execution

**Context**: Check for signs of successful JS run in the target context.

Inspect browser console for errors or use developer tools to confirm DOM alterations.

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
- [[shopify]]
