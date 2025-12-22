---
tags:
  - xss
  - stored-xss
  - embed
  - concrete-cms
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: b4c497a4-63cc-48c4-b2df-ee4361e43e22
created_at: '2025-12-14T05:32:13.280Z'
updated_at: '2025-12-14T05:32:13.280Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Embed-and-Trigger-XSS-in-Portfolio-Section

## Summary

This procedure embeds the uploaded malicious SVG into a Concrete CMS portfolio section and triggers its execution, realizing stored XSS via browser parsing of the embedded script.

## Description

Once uploaded, the SVG is inserted into editable content like a portfolio project. Viewing the page causes the browser to render the SVG, executing the JS. This exploits the lack of sanitization in embedding. Prerequisites: Uploaded file and edit access; outcome: JS alert or payload runs.

## Requirements

1. Admin access to edit portfolio sections
2. Known path to uploaded SVG
3. Web browser for triggering

## Defense

Defensive measures and detection strategies:

- Sanitize embedded assets, blocking script execution
- Implement strict CSP headers
- Audit portfolio content for external files

## Objectives

1. Integrate payload into site content
2. Execute JS on access
3. Confirm XSS impact

## Instructions

### Step 1: Edit Portfolio Section

**Context**: Locate and modify content to include the SVG.

In dashboard, go to Portfolio > Project Title. Edit a slide or add new content block.

> Expected: Editor opens for HTML/asset insertion.

### Step 2: Insert SVG Asset

**Context**: Embed using file path to trigger on render.

Use the file picker or HTML editor to insert: `<img src="/path/to/malicious.svg" alt="test">`. Save changes.

> Expected: SVG preview shows in editor; no immediate execution.

### Step 3: Access and Verify Execution

**Context**: Load the page to parse and run the script.

View the portfolio section in a browser. The SVG embeds, executing the alert('xss').

> Expected: Alert pops up, confirming stored XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[embed]]
- [[concrete-cms]]
