---
id: proc-trigger-xss-click
tags:
  - xss
  - execution
  - wordpress
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
updated_at: '2025-12-14T17:31:19.126Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Execution-via-Malicious-Link-Click

## Summary

This procedure executes the stored XSS by clicking the processed malicious link in the comment, running arbitrary JavaScript in the victim's browser.

## Description

After editing, view the post containing the comment. The now-decoded <a href="javascript:alert(1);"> link, when clicked, executes the JS payload directly in the current context (admin or viewer). This can lead to session hijacking, data exfiltration, or further attacks like clickjacking for RCE. Requires user interaction but targets any viewer, including admins.

## Requirements

1. Edited comment with decoded payload visible on a post
2. Ability to view the post in a browser
3. Victim (self or simulated) to click the link

## Defense

Defensive measures and detection strategies:

- Strip or block javascript: schemes entirely in comment rendering
- Educate users on not clicking untrusted links
- Implement JS sandboxing or no-script extensions
- Monitor for unexpected JS alerts or DOM manipulations

## Objectives

1. Execute JS payload via link click
2. Demonstrate arbitrary code execution in browser context
3. Highlight potential for escalation to RCE or data theft

## Instructions

### Step 1: View the Post

**Context**: Load the page to render the comment with the processed href.

Navigate to the post URL, e.g., http://target.com/post-title/.

### Step 2: Click the Malicious Link

**Context**: Interact with the link to trigger execution.

Locate the comment and click "Visit my web page".

> This runs javascript:alert(1);. Expected output: Alert box with "1" appears, confirming XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
- [[wordpress]]
