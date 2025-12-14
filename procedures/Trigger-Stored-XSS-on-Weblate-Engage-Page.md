---
tags:
  - xss
  - execution
type: procedure
tools:
  - '[[tools/payload-js]]'
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
updated_at: '2025-12-14T03:16:20.254Z'
sub_techniques: []
id: 2dc8b301-a2cd-4a7a-a653-b3b440145c3b
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-on-Weblate-Engage-Page

## Summary

This procedure triggers the stored XSS by accessing the vulnerable engage page, causing the injected script to load and execute arbitrary JavaScript in the browser.

## Description

The `/engage/<project_slug>` endpoint in Weblate renders the project name using unsafe string formatting, allowing the script tag to execute. When a victim (or attacker) views this page, the external `payload.js` loads under Weblate's origin, enabling further actions like issuing authenticated requests despite HttpOnly cookies.

## Requirements

1. Knowledge of the injected project's slug
2. Browser access to the Weblate instance
3. Hosted `payload.js` on external domain

## Defense

Defensive measures and detection strategies:

- Audit view rendering for unescaped user input
- Log and alert on external resource loads from engage pages
- Use Django's `mark_safe` judiciously or prefer template rendering

## Objectives

1. Execute the injected JavaScript payload
2. Gain code execution in the authenticated session context
3. Prepare for subsequent API interactions

## Instructions

### Step 1: Navigate to Vulnerable Endpoint

**Context**: Access the engage page for the injected project to trigger rendering of the unescaped name.

Open the URL `/engage/<project_slug>` in a browser authenticated to Weblate.

> The project name is fetched and inserted via `format()` in the view, executing the script tag.

**Expected Output**: Page loads; network tab shows request to `http://adversary-domain.com/payload.js` succeeding.

### Step 2: Verify Execution

**Context**: Confirm the payload runs by adding a test alert or console log in `payload.js`.

Monitor browser console for output from `payload.js`.

> Success if script executes without CSP blocks.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/payload-js]]

## Tags

- [[xss]]
- [[Execution]]
