---
tags:
  - xss
  - execution
  - web
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 8edbf588-85e5-4032-a2ae-c8c8766d1aff
created_at: '2025-12-14T03:16:25.409Z'
updated_at: '2025-12-14T03:16:25.409Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute-XSS-in-Invitation-Requests-View

## Summary

This procedure triggers the execution of the injected XSS payload by rendering the unsanitized project name in the main page's invitation requests section, compromising the viewer's browser session.

## Description

Once an invitation request is submitted for a tainted project, the project name is fetched and displayed without HTML escaping in the invitation requests view. Viewing this section as the project owner or admin causes the browser to parse and execute the embedded JavaScript. This can steal session cookies, keystrokes, or redirect to phishing sites. Requires access to the invitations dashboard post-request. Outcomes include arbitrary code execution in the context of the authenticated session.

## Requirements

1. Pending invitation request tied to the malicious project
2. Authenticated access to view invitation requests
3. Vulnerable rendering endpoint (main page invitations section)

## Defense

Defensive measures and detection strategies:

- Apply output encoding (e.g., HTML entity escaping) when rendering project names in views
- Implement strict CSP headers to block unsafe inline scripts
- Log and alert on JavaScript errors or unusual DOM manipulations in client-side logs

## Objectives

1. Render the tainted project name in the browser
2. Achieve JavaScript execution for data exfiltration or hijacking
3. Compromise the session without server-side detection

## Instructions

### Step 1: Navigate to Invitation Requests Section

**Context**: Log in as the project owner and go to the main dashboard where pending invitations are listed.

Use the web navigation menu to select "Invitation Requests" or similar.

> The page loads, fetching and displaying project-associated data.

### Step 2: Trigger Rendering of Malicious Name

**Context**: View or expand the specific invitation request linked to the tainted project, causing the name to be inserted into the DOM.

Click on the request entry to display details including the project name.

> Payload executes immediately upon DOM insertion, e.g., showing a prompt.

### Step 3: Observe and Exploit Execution

**Context**: Confirm execution via the alert or console, then adapt payload for real attacks like cookie theft (e.g., via fetch to attacker server).

Monitor browser dev tools for script activity; for production, replace prompt with exfiltration code.

> Expected: Arbitrary JS runs, potentially logging session data to attacker-controlled endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
