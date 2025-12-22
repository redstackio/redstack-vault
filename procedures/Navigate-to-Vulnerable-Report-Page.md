---
tags:
  - reconnaissance
  - hackerone
type: procedure
tools:
  - '[[tools/H1-Triage-Wizard-Chrome-Extension]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T00:11:09.492Z'
sub_techniques: []
id: 10d23bfe-84ea-40b2-be5f-5a6a5b6a276a
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Navigate-to-Vulnerable-Report-Page

## Summary

This procedure accesses a specific HackerOne report page using a URL with parameters that influence the extension's modal behavior, setting up the conditions for HTML injection.

## Description

By navigating to a report like https://hackerone.com/reports/1622449?subject=security&/bugs=1, the 'subject' parameter populates the handle in the triage modal. This step targets public report pages where the extension can interact, leading to unsanitized input rendering in the browser context.

## Requirements

1. Active internet connection
2. Chrome browser with H1 Triage Wizard enabled
3. No authentication needed for public reports

## Defense

Defensive measures and detection strategies:

- Implement URL parameter validation on web applications
- Log unusual parameter usage in access logs
- Use Content Security Policy (CSP) to restrict script sources

## Objectives

1. Load the target page to engage the extension
2. Confirm parameter influence on modal content
3. Prepare for modal triggering without detection

## Instructions

### Step 1: Open the Target URL

**Context**: Directly access the vulnerable report page to initialize the environment.

In Chrome, enter or paste https://hackerone.com/reports/1622449?subject=security&/bugs=1 into the address bar and press Enter.

> The page should load the report details, with the subject parameter ready to affect the modal.

### Step 2: Verify Page Load

**Context**: Ensure the page is fully rendered and extension is active.

Inspect the page source or console for any extension hooks; no errors should appear.

> Success: Report content displays correctly, including any bug references.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/H1-Triage-Wizard-Chrome-Extension]]

## Tags

- reconnaissance
- web-navigation
