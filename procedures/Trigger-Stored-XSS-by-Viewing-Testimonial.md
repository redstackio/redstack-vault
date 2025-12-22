---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567893
name: Trigger-Stored-XSS-by-Viewing-Testimonial
tags:
  - xss
  - execution
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
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:35.475Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-by-Viewing-Testimonial

## Summary

This procedure triggers the execution of the stored XSS payload by accessing the testimonial display page in Concrete CMS, causing JavaScript to run in the viewer's browser context.

## Description

When the testimonial is rendered on a frontend page, Concrete CMS outputs the name field without HTML escaping, allowing the injected `<img>` tag to execute its `onerror` handler. This leads to arbitrary JavaScript execution, such as alerts, cookie theft, or keylogging, impacting any unauthenticated user viewing the content. The scenario targets web browsers in a PHP/Concrete CMS environment, with outcomes including immediate script firing and potential data exfiltration.

## Requirements

1. Saved testimonial with payload in the system
2. URL or page access to view testimonials (public or authenticated)
3. Victim browser without XSS protections disabled

## Defense

Defensive measures and detection strategies:

- Apply output encoding (e.g., htmlspecialchars) when rendering testimonial names
- Deploy browser-based protections like XSS auditors or NoScript extensions
- Log and alert on JavaScript errors or unexpected alerts in client-side monitoring

## Objectives

1. Execute the persisted script in a target browser
2. Demonstrate impact like session hijacking or data theft
3. Validate the full stored XSS chain

## Instructions

### Step 1: Locate Display Page

**Context**: Find the endpoint that renders the testimonial.

Navigate to the frontend page, dashboard preview, or testimonial list where the saved entry is displayed.

### Step 2: Load the Page

**Context**: Trigger rendering of the vulnerable field.

Visit the URL containing the testimonial. The server outputs the name as raw HTML, parsing the `<img>` tag.

> The invalid `src=x` causes onerror to fire, running `alert(1)` in the current browser session.

### Step 3: Observe Execution

**Context**: Confirm script activation.

Watch for the alert popup or check browser console for execution traces. In a real attack, replace alert with malicious code like `document.cookie` exfiltration.

> Expected: Alert box with '1'; console logs script errors if dev tools open.

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
- [[Execution]]
