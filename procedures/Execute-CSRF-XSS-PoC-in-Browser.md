---
id: proc-uuid-4
tags:
  - execution
  - browser
  - xss
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:42.463Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute CSRF XSS PoC in Browser

## Summary

This procedure involves opening the crafted HTML PoC in a browser while authenticated to the target application, triggering the CSRF submission and subsequent XSS execution for arbitrary JavaScript.

## Description

The attacker (or victim via phishing) loads the local HTML file in a browser session logged into the app. The auto-form submits the POST with the XSS payload, reflecting it globally due to no CSRF checks. This executes JS like alert(1), but could extend to keylogging or actions on behalf. Environment: Modern browsers like Firefox/Chrome. Outcomes: Confirmed execution via popup or console, demonstrating full impact.

## Requirements

1. Authenticated browser session to the target app.
2. Local access to the PoC HTML file.
3. Browsers supporting JavaScript and form submission.

## Defense

Defensive measures and detection strategies:

- Browser extensions blocking auto-submits (e.g., NoScript).
- Server-side logging of unexpected POST origins.
- User training to avoid opening untrusted HTML files.

## Objectives

1. Trigger form submission via CSRF.
2. Achieve XSS payload execution.
3. Validate impact like session actions.

## Instructions

### Step 1: Prepare Browser Session

**Context**: Ensure the browser is logged into the target application.

Navigate to the app in Firefox or Chrome and authenticate if needed.

**Expected Output**: Active session cookies for the domain.

### Step 2: Load PoC File

**Context**: Open the HTML file locally to initiate auto-submit.

Use File > Open File to load the PoC.html.

**Expected Output**: Form submits immediately without user interaction.

### Step 3: Verify Execution

**Context**: Check for JS execution indicators.

Observe alert(1) popup or inspect console for errors triggering onerror.

**Expected Output**: Successful alert or logged execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Google-Chrome]]

## Tags

- [[xss]]
- [[csrf]]
