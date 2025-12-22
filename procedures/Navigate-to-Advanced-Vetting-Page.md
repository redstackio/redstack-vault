---
id: proc-983077-navigate-vetting
tags:
  - xss
  - web-navigation
  - vetting-page
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:20.864Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Navigate-to-Advanced-Vetting-Page

## Summary

This procedure navigates to the advanced vetting settings page for the target program, positioning the attacker to access the vulnerable example DCA generation feature.

## Description

After creating the program, the advanced vetting page at /:handle/advanced_vetting loads the stored Program Name. In local PoC, this is http://localhost:8080/handle/advanced_vetting. No execution occurs here, but it sets up the environment for the Markdown React component to process unsanitized input.

## Requirements

1. Program handle from previous creation step
2. Authenticated session
3. Browser access to HackerOne or local server on port 8080

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls for vetting pages
- Log and alert on rapid program creation followed by vetting access
- Escape outputs in page rendering to prevent reflection

## Objectives

1. Load the vetting page with stored payload context
2. Verify page functionality without premature execution
3. Prepare for DCA trigger

## Instructions

### Step 1: Construct and Visit URL

**Context**: Use the program's handle to build the URL and navigate.

In browser, go to https://hackerone.com/:handle/advanced_vetting, replacing :handle with the actual handle (e.g., https://hackerone.com/my-sandbox/advanced_vetting). For local: http://localhost:8080/handle/advanced_vetting.

> Page loads with settings; Program Name may appear but not execute yet.

### Step 2: Confirm Access

**Context**: Ensure the page is fully loaded and interactive.

Check for the 'View document' button presence.

> Expected: Settings form visible, no JS errors in console.

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
- [[web-navigation]]
