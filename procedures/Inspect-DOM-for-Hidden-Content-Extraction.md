---
id: proc-uuid-2
tags:
  - dom-inspection
  - hidden-content
type: procedure
tools:
  - '[[tools/Browser-Dev-Tools]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:24:55.580Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Inspect-DOM-for-Hidden-Content-Extraction

## Summary

This procedure uses browser developer tools to inspect the Document Object Model (DOM) of a web page, uncovering hidden or obscured flags in HTML comments or elements that are not visible in the rendered view.

## Description

Web pages often hide sensitive data in DOM elements, comments, or attributes for CTF challenges. By inspecting the source after page load, attackers extract this without server interaction. Targets JavaScript-rendered pages on public web apps; prerequisites include browser access to the endpoint like /moved.

## Requirements

1. Modern web browser with dev tools
2. Access to the target URL
3. No special privileges

## Defense

Defensive measures and detection strategies:

- Obfuscate or remove hidden data from client-side code
- Monitor for unusual dev tools usage via JavaScript hooks
- Serve minified JS to complicate inspection

## Objectives

1. Extract client-side hidden flags
2. Identify poor data hiding practices
3. Enable quick low-effort discovery

## Instructions

### Step 1: Load and Inspect Page

**Context**: Visit the target page and use dev tools to view the full DOM source.

No command-line command; open browser dev tools (F12), navigate to Elements tab, and search for flag patterns in HTML.

> Look for comments like <!-- flag{...} --> or hidden divs; copy the flag directly.

### Step 2: Verify Extraction

**Context**: Confirm the flag is valid by checking CTF format.

Manually validate the extracted string matches expected flag pattern.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Browser-Dev-Tools]]

## Tags

- [[dom-inspection]]
- [[hidden-content]]
