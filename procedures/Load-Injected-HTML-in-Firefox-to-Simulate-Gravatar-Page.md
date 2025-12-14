---
tags:
  - xss
  - local-simulation
  - browser
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: bacf3b61-1f48-49b7-93fe-ad4c557399a5
created_at: '2025-12-14T03:15:35.919Z'
updated_at: '2025-12-14T03:15:35.919Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Load-Injected-HTML-in-Firefox-to-Simulate-Gravatar-Page

## Summary

This procedure loads the payload-injected HTML file in Firefox to render a simulated Gravatar page, allowing inspection of vulnerable elements like JSON/XML links prior to triggering the XSS.

## Description

To test the Gravatar XSS without remote access, open the local 'gravatar_poc.html' file in Mozilla/Firefox. This simulates the service's rendering of unsanitized content, as shown in PoC screenshots (e.g., http://grabilla.com/04318-271a0763-cad8-4482-ab02-3d8948f33b04.html). The browser executes the page in a victim-like context, exposing injected attributes for interaction. This step confirms the payload's presence and sets up for execution, demonstrating high-severity risks like session hijacking.

## Requirements

1. Firefox or Mozilla browser installed
2. Local HTML file from previous procedure
3. No network connectivity required

## Defense

Defensive measures and detection strategies:

- Browser extensions like NoScript to block JS execution
- Server-side validation to prevent payload injection
- Logging of unusual local file loads in enterprise environments

## Objectives

1. Render vulnerable page locally
2. Visualize injected elements
3. Prepare for trigger without errors

## Instructions

### Step 1: Open File in Browser

**Context**: Launch the browser and load the file to simulate Gravatar rendering.

Navigate to the file location and double-click 'gravatar_poc.html', or use File > Open in Firefox.

> The page loads, displaying links with hidden payloads; check browser console for any immediate issues.

### Step 2: Inspect Page Elements

**Context**: Verify injection in dev tools.

Right-click a link and select Inspect Element to confirm onmouseover attributes.

> Expected: Attributes show 'prompt(916137)' injection; no CSP blocks.

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
- [[browser-simulation]]
