---
tags:
  - xss
  - payload-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.196Z'
sub_techniques: []
id: 93e5868b-d3fb-4274-af02-d65f83deaf0d
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Self-XSS-by-Viewing-Placemark

## Summary

This procedure demonstrates executing the stored JavaScript payload by accessing the placemark on the WordPress front-end, confirming the self-XSS in the user's browser.

## Description

The plugin renders the placemark title on the front-end without escaping, causing the stored script to execute in the viewer's context. Since it's self-XSS, only the injecting user's session is affected. Use the preview or public view to trigger. Verify via alert or console logs. This step highlights the vulnerability's impact, limited to the authenticated user.

## Requirements

1. Saved placemark with payload
2. Access to front-end or preview URL
3. Same browser session for execution context

## Defense

Defensive measures and detection strategies:

- Escaping outputs with esc_js() or similar on front-end rendering
- Browser-based CSP enforcement
- User education on avoiding suspicious inputs

## Objectives

1. Execute the stored script
2. Observe effects in browser
3. Confirm self-contained impact

## Instructions

### Step 1: Locate Placemark View

**Context**: Find the URL or preview for the placemark.

From admin, use the preview link or navigate to the map page displaying the placemark.

> Page loads with placemark elements.

### Step 2: Render and Execute

**Context**: Trigger payload by viewing the title.

Load the page; the title renders, executing the script.

> Alert pops or console shows execution; inspect element to see unescaped script.

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
- [[payload-execution]]
