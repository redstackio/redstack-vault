---
tags:
  - xss-trigger
  - verification
  - javascript-execution
  - gitlab
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
updated_at: '2025-12-14T00:11:09.712Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 4c6939b8-043f-4d05-9137-8caad105d540
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-and-Verify-Stored-XSS

## Summary

This procedure views the tainted GitLab Wiki page to render the injected payload and confirms XSS execution by interacting with the malicious hyperlink, demonstrating persistent arbitrary JavaScript capability.

## Description

After injection, the stored payload renders as a hyperlink in the Markdown content. Clicking it executes the javascript:confirm in the viewer's browser context, bypassing parser protections due to the encoding trick. This affects all users in GitLab 10.0, highlighting the persistent nature across Markdown usages.

## Requirements

1. Successfully injected and saved Wiki page
2. Web browser without proxy interference
3. Access to view the Wiki as any user

## Defense

Defensive measures and detection strategies:

- Audit rendered Markdown for unexpected hyperlinks with javascript: schemes
- Implement client-side JS sandboxing or disable hyperlink execution in Wiki views
- Monitor browser console for unauthorized confirm/alert popups during page loads

## Objectives

1. Render the page to display the payload
2. Interact to execute JS and observe effects
3. Validate persistence by re-viewing as different users

## Instructions

### Step 1: View Updated Page

**Context**: Load the Wiki page post-injection to trigger Markdown parsing.

Disable any proxies, navigate to the Project Wiki URL (e.g., /projects/1/wikis/home), and observe the rendered content. The payload should appear as a clickable link: "Click to execute".

### Step 2: Interact and Confirm Execution

**Context**: Trigger the XSS to verify JavaScript runs.

Click the link. A browser confirm dialog should pop up displaying the GitLab domain (e.g., confirm('gitlab-instance.com')).

**Expected Output**: Alert/confirm executes, proving JS injection success. Inspect page source to see decoded payload in the HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-trigger]]
- [[verification]]
- [[javascript-execution]]
- [[gitlab]]
