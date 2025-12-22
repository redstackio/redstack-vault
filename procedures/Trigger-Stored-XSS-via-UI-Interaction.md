---
tags:
  - xss
  - trigger
  - ui-interaction
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:43.587Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 4b2ace26-6af0-4da8-85e2-040f7115b75b
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-via-UI-Interaction

## Summary

This procedure describes loading a vulnerable GitLab issue page and performing a minimal UI interaction to execute the stored XSS payload resulting from prototype pollution, allowing arbitrary JavaScript in the victim's session.

## Description

Once the malicious Mermaid diagram is rendered, the polluted prototype causes the 'template' property to inject an iframe with external script during certain UI events, such as focusing the search bar. This stored XSS requires no direct input from the victim beyond page load and a common interaction. It targets GitLab's client-side rendering and assumes the viewer has a valid session. Outcomes include JavaScript execution for data exfiltration or account manipulation.

## Requirements

1. URL of the issue containing the malicious payload
2. Victim's web browser accessing the GitLab instance
3. No special privileges; triggers on standard view access

## Defense

Defensive measures and detection strategies:

- Isolate prototype objects in JavaScript rendering libraries like Mermaid
- Monitor for unexpected script executions or network requests from issue pages
- Implement strict XSS filters and audit UI event handlers for template usage

## Objectives

1. Execute the injected JavaScript in the victim's browser context
2. Steal session data or perform unauthorized actions
3. Confirm exploit success with minimal interaction

## Instructions

### Step 1: Load Issue Page

**Context**: Access the page to render the polluted Mermaid diagram.

Open the issue URL (e.g., https://gitlab.com/cataha319/stored-xss/-/issues/2) in a browser and wait for full load.

> The diagram renders, applying the prototype pollution silently.

### Step 2: Perform Triggering Interaction

**Context**: Invoke the polluted template via a UI element.

Click on the search menu in the top navigation bar.

> This triggers the malicious iframe and script execution, such as loading external JS that may alert or exfiltrate data.

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
- [[trigger]]
- [[ui-interaction]]
