---
id: proc-uuid-002
name: Trigger-XSS-via-Rendered-Link-Interaction
tags:
  - xss
  - execution
  - interaction
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
updated_at: '2025-12-14T03:16:14.551Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Rendered-Link-Interaction

## Summary

This procedure demonstrates observing the stored malicious URL rendered in the comments and triggering the XSS by clicking the link, leading to JavaScript execution if not blocked by CSP.

## Description

After submission, the Airship application renders the comment, inserting the unfiltered javascript: URL directly into the href attribute of a link element (e.g., <a href="javascript:alert(1)">Website</a>). When a user (victim) views the page and clicks the link, the browser executes the JavaScript in the page's context. The impact is limited by requiring interaction and default CSP blocking inline scripts, but it affects sites without CSP or with lax policies, enabling theft of session data or page manipulation.

## Requirements

1. The malicious comment already submitted and stored
2. Access to the blog post page where the comment is visible
3. A browser without strict CSP enforcement (or modified for testing)

## Defense

Defensive measures and detection strategies:

- Apply attribute escaping to URL fields during rendering (e.g., convert javascript: to safe text)
- Use a CSP header to block javascript: schemes and inline execution
- Implement client-side validation to prevent clicks on suspicious links
- Log and review rendered comments for anomalous href values

## Objectives

1. Verify storage and rendering of the malicious URL
2. Execute the JavaScript payload via user interaction
3. Highlight risks to users viewing comments

## Instructions

### Step 1: Load the Target Page

**Context**: Ensure the stored comment is rendered on the page.

Refresh or navigate to the blog post page containing the submitted comment.

### Step 2: Inspect Rendered Comment

**Context**: Confirm the URL is inserted without sanitization.

View the comments section and inspect the HTML source or use browser dev tools to locate the link element with the href set to the javascript: payload.

### Step 3: Interact to Trigger Execution

**Context**: Simulate victim behavior to execute the XSS.

Click on the rendered website link in the comment.

> If successful, the JavaScript runs, e.g., displaying an alert or sending data to an attacker-controlled server.

**Expected Output**: JavaScript execution, such as an alert popup or network request, unless blocked by CSP.

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
- [[Execution]]
- [[web]]
