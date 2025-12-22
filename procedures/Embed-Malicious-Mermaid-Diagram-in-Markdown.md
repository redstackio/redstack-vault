---
tags:
  - mermaid-xss
  - stored-xss
  - markdown-injection
type: procedure
tools: []
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:52:39.125Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 495dab35-8671-4edb-aefb-875f0f32bcef
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Embed-Malicious-Mermaid-Diagram-in-Markdown

## Summary

This procedure injects a stored XSS payload into GitLab Markdown files using a Mermaid diagram with a misconfigured directive to bypass HTML sanitization and render an iframe loading the exploit script.

## Description

The core vulnerability stems from Mermaid's config handling: sanitization checks for boolean false, but rendering treats string 'false' as truthy, allowing HTML injection. Combined with the artifact iframe, this stores the XSS for any viewer. Target: GitLab Markdown renderer. Prerequisites: Artifact ready with job ID. Outcomes: Persistent XSS triggerable on file view.

## Requirements

1. GitLab repository with artifact job ID
2. Edit access to Markdown files (e.g., README.md)
3. Understanding of Mermaid syntax and directives

## Defense

Defensive measures and detection strategies:

- Update Mermaid config to strictly parse directives as booleans
- Sanitize all flowchart.htmlLabels to prevent string bypass
- Scan commits for suspicious %%{init} directives in Markdown

## Objectives

1. Bypass Mermaid sanitization for HTML rendering
2. Embed iframe to load external same-origin JS
3. Store payload for execution on authenticated views

## Instructions

### Step 1: Craft Mermaid Payload

**Context**: Create a fenced block with init directive setting htmlLabels to string 'false' to disable sanitization check while enabling HTML render.

In README.md web editor, insert:

```markdown
```mermaid
%%{init: {"flowchart": {"htmlLabels": "false"}} }%%
flowchart TD
    A([<iframe src="/api/v4/projects/{PROJECT_ID}/jobs/{JOB_ID}/artifacts/exploit.js" style="display:none;"></iframe>])
```
```
Replace {PROJECT_ID} and {JOB_ID} with actual values.

> Preview shows diagram; commit to store.

### Step 2: Commit and Verify Storage

**Context**: Ensure the payload persists without immediate execution.

Commit changes via UI; no render on edit.

> Success: File updated, payload embedded for later trigger.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[directive-bypass]]
- [[iframe-injection]]
