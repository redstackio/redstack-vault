---
tags:
  - xss
  - trigger
  - portal-settings
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
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
id: 1ac81d91-d4f4-4bc9-a594-c54cf0f452e7
created_at: '2025-12-14T00:11:16.155Z'
updated_at: '2025-12-14T00:11:16.155Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-on-Portal-Settings-Page

## Summary

This procedure demonstrates triggering the stored XSS payload when accessing the portal settings page, executing JavaScript in the victim's browser context.

## Description

Upon loading the settings page, the app renders the stored content, including the injected <img> tag. The onerror event fires due to the invalid src, executing the alert. This affects any user, including other admins or customers, potentially leading to session theft or further attacks.

## Requirements

1. Injected payload already saved in portal content
2. Victim access to the portal settings URL
3. No special privileges needed for triggering

## Defense

Defensive measures and detection strategies:

- Sanitize output on render (e.g., escape HTML entities)
- Monitor browser console for unexpected alerts or errors
- Implement XSS auditors or WAF rules for script patterns
- Restrict settings page access to verified admins

## Objectives

1. Execute arbitrary JS on page load
2. Confirm vulnerability impact on settings view
3. Simulate victim session compromise

## Instructions

### Step 1: Navigate to Settings Page

**Context**: Load the vulnerable content.

Open `https://services.alveo.io/dashboard-shopify/settings/portal/content` in a browser (attacker's or victim's session).

### Step 2: Observe Execution

**Context**: Trigger the onerror event.

The page renders the content; the broken image causes the alert(2) to pop up automatically.

### Step 3: Verify Impact

**Context**: Check for exploitation potential.

Inspect browser console for script execution; replace alert with data exfiltration in real attacks.

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
- [[trigger]]
- [[portal-settings]]
