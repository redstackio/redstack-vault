---
id: proc-1147949-xss-execute
tags:
  - xss
  - csrf
  - execution
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:35.744Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Demonstrate-CSRF-Chained-XSS-Execution

## Summary

This procedure demonstrates the full exploitation by loading the CSRF PoC in a victim's browser, triggering the forged submission and resulting in reflected XSS execution within the authenticated session.

## Description

With the victim authenticated to the DoD site, loading the PoC HTML causes an invisible POST submission to the vulnerable endpoint, injecting the XSS payload. The reflected payload executes JavaScript on *.██████████, potentially stealing session cookies or performing other actions. This step validates the chain's effectiveness in a real browser environment.

## Requirements

1. Crafted CSRF PoC HTML from previous procedure.
2. Browser with active session to the target DoD subdomain.
3. No additional tools beyond a standard web browser.

## Defense

Defensive measures and detection strategies:

- Enable browser protections like XSS auditors or extensions.
- Monitor for unexpected alerts or script executions in client-side logs.
- Use multi-factor authentication to mitigate session hijacking impacts.

## Objectives

1. Trigger CSRF submission from the PoC.
2. Observe XSS alert in the target domain context.
3. Confirm potential for further exploitation like session theft.

## Instructions

### Step 1: Prepare Victim Session

**Context**: Ensure the browser is authenticated to the target site.

Log in to https://██████████ in the test browser to establish a valid session.

**Expected Output**: Active session cookies for the domain.

### Step 2: Load PoC HTML

**Context**: Open the malicious page while the session is active.

Save the PoC as an HTML file and open it in the browser (or host it externally).

**Expected Output**: Form auto-submits or button appears for manual trigger.

### Step 3: Trigger Submission and Observe

**Context**: Execute the request to chain CSRF with XSS.

Click the submit button if not auto-submitting; monitor for the POST request and response.

**Expected Output**: XSS alert pops up showing the document domain, confirming execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-execution
- csrf-demonstration
- session-hijack
