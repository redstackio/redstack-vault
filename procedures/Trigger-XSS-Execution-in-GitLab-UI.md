---
tags:
  - xss-execution
  - csrf-theft
  - csp-bypass
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
updated_at: '2025-12-13T23:52:39.123Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 2c52a616-3f0e-49a8-a953-6ff7f1f3bf15
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Execution-in-GitLab-UI

## Summary

This procedure triggers the stored XSS by viewing the malicious Markdown in GitLab, executing the injected JavaScript via iframe to steal the viewer's CSRF token and enable account takeover.

## Description

Viewing the file causes GitLab to render the Mermaid diagram, processing the directive to inject unsanitized HTML (iframe), which loads the artifact JS under 'self' CSP policy. The script runs in the authenticated context, accessing meta tags. Target: GitLab UI renderer. Prerequisites: Embedded payload. Outcomes: Token exfiltration, potential escalation.

## Requirements

1. Authenticated session as victim (or self for test)
2. Access to view the Markdown file
3. Browser with JS enabled

## Defense

Defensive measures and detection strategies:

- Implement strict CSP nonces for all scripts, blocking external loads
- Patch Mermaid to treat string 'false' as falsy in rendering
- Monitor browser console for unexpected alerts or iframe loads in Markdown views

## Objectives

1. Execute arbitrary JS in viewer's browser
2. Extract sensitive data like CSRF tokens
3. Facilitate account takeover via stolen credentials

## Instructions

### Step 1: Navigate to Malicious File

**Context**: Load the page that renders the Markdown, triggering Mermaid processing.

In GitLab UI, go to Project > README.md or overview page.

> Renderer parses directive, injects iframe HTML due to bypass.

### Step 2: Observe Execution and Exfiltration

**Context**: The iframe src loads exploit.js, running the alert script.

No action needed; watch for alert popup with token HTML.

> Success: Alert shows <meta name="csrf-token" content="...">; console logs execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[token-theft]]
- [[js-execution]]
