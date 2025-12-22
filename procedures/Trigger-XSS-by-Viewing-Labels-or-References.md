---
id: proc-uuid-3
tags:
  - xss
  - trigger
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:56:19.874Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Trigger-XSS-by-Viewing-Labels-or-References

## Summary

This procedure triggers the stored XSS payload by accessing the imported project's labels page or referencing the malicious label in issues/merge requests, executing arbitrary JavaScript in the viewer's browser.

## Description

Once imported, the malicious label colors contain JavaScript that executes when rendered in GitLab UI, bypassing CSP due to trusted label styling. This can be triggered directly on /labels or via mentions like ~"label-name" in descriptions, even cross-project. Impact includes session theft or DoS. No tools/commands needed beyond browser access; expected outcome: Payload execution confirming vuln.

## Requirements

1. Imported project with malicious labels
2. Access to GitLab project (as victim/user)
3. Browser with JS enabled

## Defense

Defensive measures and detection strategies:

- Sanitize label colors to valid hex/CSS values only
- Enforce strict CSP blocking unsafe-inline/eval
- Monitor for JS alerts or anomalous browser behavior in logs

## Objectives

1. Execute injected JavaScript payload
2. Steal sensitive data like tokens
3. Demonstrate impact via DoS or takeover

## Instructions

### Step 1: View Labels Page

**Context**: Directly access the labels endpoint to render malicious colors.

**Instructions**: Navigate to https://gitlab.com/YOUR_NAMESPACE/PROJECT_NAME/-/labels in a browser.

> The page loads labels, executing JS in color attributes. Expected output: Alert or payload effect, e.g., alert(document.domain).

### Step 2: Reference Label in Issue

**Context**: Mention label to trigger in broader contexts.

**Instructions**: Create or view an issue/merge request with ~"malicious-label-name".

> Renders the label inline, firing XSS. Expected output: JS execution on render.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- trigger
- execution
