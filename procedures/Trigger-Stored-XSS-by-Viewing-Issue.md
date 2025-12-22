---
tags:
  - xss-trigger
  - javascript-execution
  - gitlab-view
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:18.317Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: d963339a-6213-4d56-a84f-9ef7715ff50e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-by-Viewing-Issue

## Summary

This procedure triggers the stored XSS by navigating to the affected issue's details page, causing the browser to render the malicious Markdown and execute injected JavaScript.

## Description

Upon viewing the issue, GitLab parses the Markdown description into HTML, injecting an <img> tag with an onload attribute that runs alert(1). This was verified in Firefox and Chrome, but not in IE11 or Edge due to rendering differences. The execution occurs client-side, affecting any authenticated or public viewer, enabling attacks like cookie theft.

## Requirements

1. Created issue with stored payload
2. Web browser (Firefox or Chrome) to render the page
3. Access to the project's issue details (public project allows anonymous views)

## Defense

Defensive measures and detection strategies:

- Deploy browser extensions or policies to block XSS alerts and unauthorized scripts
- Log and alert on JavaScript errors or popups in web apps
- Use web application firewalls (WAF) to inspect rendered content for malicious attributes

## Objectives

1. Render the issue page to execute the payload
2. Confirm JavaScript execution in the victim's browser context
3. Demonstrate impact on session or data access

## Instructions

### Step 1: Locate the Issue

**Context**: Find the injected issue in the list.

In the project's Issues section, click on the 'PoC' issue title.

> Details page loads with rendered description.

### Step 2: Observe Execution

**Context**: The page render triggers the onload event automatically.

View the page; the image tag in the description executes alert(1) immediately.

> Alert dialog appears; inspect page source to see <img src="a" onload="alert(1)" alt="xss\"" />.

### Step 3: Validate in Multiple Browsers

**Context**: Test cross-browser behavior.

Repeat in Chrome; note failure in IE11/Edge due to stricter parsing.

> Success in modern browsers confirms vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Chrome]]

## Tags

- xss-execution
- browser-trigger
- gitlab
