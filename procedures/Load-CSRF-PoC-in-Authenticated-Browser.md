---
id: proc-uuid-3
tags:
  - csrf-execution
  - browser-exploit
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:29.629Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Load-CSRF-PoC-in-Authenticated-Browser

## Summary

This procedure loads the crafted CSRF HTML PoC in a browser with an active LGTM session, enabling the form to submit authenticated requests to the vulnerable endpoint.

## Description

With the LGTM session active, opening the local HTML file allows the browser to use existing cookies for the POST request, bypassing origin checks due to the platform's weak CSRF protections. The PoC form is hidden and can auto-submit via JavaScript if desired, but manual click simulates victim interaction. This step exploits the same-origin policy relaxation in modern browsers for local files.

## Requirements

1. Active LGTM session in the target browser
2. Saved CSRF HTML PoC file from previous procedure
3. Browser supporting file:// protocol (e.g., Chrome, Firefox)

## Defense

Defensive measures and detection strategies:

- Use Content Security Policy (CSP) to restrict script execution from local files
- Educate users on phishing risks and avoiding unsolicited HTML attachments
- Browser extensions like uBlock Origin can block suspicious form submissions

## Objectives

1. Load PoC without disrupting LGTM session
2. Prepare form for submission using session cookies
3. Confirm form data integrity

## Instructions

### Step 1: Ensure Active Session

**Context**: Verify LGTM authentication before loading PoC.

Keep the LGTM tab open and confirm session via dashboard access.

**Expected Output**: No login prompts.

### Step 2: Open HTML File

**Context**: Load the PoC in the same browser window or tab.

Drag-and-drop the HTML file into the browser or use File > Open File.

**Expected Output**: Page loads with form (visible or hidden); inspect elements to see inputs.

### Step 3: Inspect for Readiness

**Context**: Check that form targets correct endpoint and includes nonce.

Use developer tools (F12 > Elements) to view form action and inputs.

**Expected Output**: Form action="https://lgtm-com.pentesting.semmle.net/internal_api/v0.2/savePublicInformation" with populated fields.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[browser]]
