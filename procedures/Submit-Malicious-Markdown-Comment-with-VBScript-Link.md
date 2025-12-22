---
id: proc-uuid-1
tags:
  - xss
  - stored-xss
  - injection
  - markdown
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
updated_at: '2025-12-14T03:16:37.347Z'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Submit-Malicious-Markdown-Comment-with-VBScript-Link

## Summary

This procedure injects a stored XSS payload into GitLab's Markdown rendering by posting a comment with a malicious vbscript: protocol link, which is not sanitized and persists for viewing by victims.

## Description

In GitLab, the Markdown parser in project and issue comments fails to block or sanitize the vbscript: scheme in links. An attacker with comment-posting privileges can embed a link like [clickme](vbscript:alert(document.domain)), which renders harmlessly in modern browsers but executes VBScript in vulnerable Internet Explorer versions (7-10 or IE11 in compatibility mode). This leads to arbitrary JavaScript execution in the GitLab domain context, enabling attacks like session cookie theft. The payload is stored server-side and activates upon victim interaction.

## Requirements

1. Authenticated access to a GitLab project or issue (user-level permissions)
2. Standard web browser for injection (any modern browser suffices for posting)
3. Target GitLab version vulnerable to this issue (pre-fix for CVE or similar)

## Defense

Defensive measures and detection strategies:

- Sanitize Markdown links to block non-standard protocols like vbscript:
- Disable compatibility mode in IE11 and encourage modern browser use
- Monitor for unusual comment patterns or script-like content in audits

## Objectives

1. Store a persistent XSS payload in GitLab comments
2. Set up for client-side execution targeting IE users
3. Enable potential session hijacking upon victim click

## Instructions

### Step 1: Access GitLab Project or Issue

**Context**: Log in and navigate to a location where comments can be posted, such as a project description or issue thread.

**Instructions**: Use your GitLab credentials to access the target project. Go to an issue or merge request and locate the comment box.

### Step 2: Craft and Submit Malicious Comment

**Context**: Compose a Markdown comment embedding the vbscript: link to exploit the unsanitized rendering.

**Instructions**: Enter the following in the comment field:

`[Click me to learn more](vbscript:alert(document.domain))`

Submit the comment. The link will render as clickable text without triggering in the poster's browser.

> This stores the payload server-side, visible to all viewers of the page.

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
- [[gitlab]]
- [[vbscript]]
