---
tags:
  - xss
  - dom-xss
  - tooltip
  - firefox
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
id: 3d3c70c0-64a6-4be5-a381-726d7f3f4c2e
created_at: '2025-12-13T23:52:43.677Z'
updated_at: '2025-12-13T23:52:43.677Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Referencing-the-Issue

## Summary

This procedure triggers the DOM-based XSS by referencing the malicious issue in a comment or wiki, causing Bootstrap tooltips to render the SVG on hover, executing the JavaScript in the viewer's browser context on Firefox.

## Description

Issue references like #1 generate tooltips using Bootstrap, which inserts the issue title's SVG without blocking external loads. Firefox's SVG support for foreignObject and the svg4everybody polyfill enable script execution, allowing arbitrary JS like session theft.

## Requirements

1. Issue ID from previous procedure
2. Firefox browser
3. Access to post in discussions or wikis

## Defense

Defensive measures and detection strategies:

- Sanitize tooltips to remove SVG <use> and xlink:href
- Disable SVG rendering in tooltips or use a stricter sanitizer
- Monitor for anomalous JS alerts or network requests from tooltips

## Objectives

1. Render the tooltip to load the SVG
2. Execute JS in the authenticated user's session
3. Demonstrate impact like URL exfiltration

## Instructions

### Step 1: Create Reference Context

**Context**: Post a comment or wiki entry referencing the issue.

In an issue discussion or wiki, add: "Move mouse over #1 to see alert" (replace 1 with actual ID).

### Step 2: Hover to Trigger

**Context**: Interact with the reference in Firefox.

View the page and hover over the #1 link.

**Expected Output**: Tooltip displays; SVG loads, iframe executes, alert shows "Hello: " + current URL.

### Step 3: Validate Execution

**Context**: Confirm JS runs in victim context.

The alert should access window.parent.location.href, proving same-origin execution.

**Expected Output**: Alert with victim's page URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- firefox
