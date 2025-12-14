---
tags:
  - xss
  - execution
  - web
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:29:10.188Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 672db8fe-3022-474c-baf6-e1e188e52ab4
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-on-Admin-Access-Page

## Summary

This procedure triggers the execution of the stored XSS payload by navigating to the Admin Access page in Revive Adserver, causing the injected JavaScript to run in the viewer's browser.

## Description

The vulnerable page (Inventory > Admin Access) displays admin details, including the unsanitized email field from preferences. Loading this page renders the injected script, executing it client-side. This can lead to alerts, data exfiltration, or browser hooking. The attack relies on the persistence from the prior injection step and targets other admins viewing the page.

## Requirements

1. Active session as the secondary admin
2. Browser with JavaScript enabled (e.g., Firefox v47.0)
3. Access to the Inventory section

## Defense

Defensive measures and detection strategies:

- Sanitize all outputs on admin pages with HTML entity encoding
- Implement client-side validation and server-side filtering for email fields
- Monitor browser console errors and unexpected script executions via logging

## Objectives

1. Load the page containing the stored payload
2. Execute the JavaScript in the current browser context
3. Validate exploitation success

## Instructions

### Step 1: Navigate to Inventory Section

**Context**: Access the menu leading to the vulnerable page.

From the admin dashboard in Firefox, click on Inventory.

**Expected Output**: Inventory submenu appears.

### Step 2: Access Admin Access Page

**Context**: View the list of admins, triggering the display of the injected email.

Select Admin Access from the Inventory menu.

**Expected Output**: Page loads with admin list; JavaScript alert('xss') pops up.

> The payload executes automatically upon rendering the email field.

### Step 3: Verify Execution

**Context**: Confirm the XSS worked as intended.

Check the browser console for script execution logs or observe the alert dialog.

**Expected Output**: Visible alert box or console output indicating 'xss'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- xss-trigger
- browser-execution
