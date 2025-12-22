---
id: proc-gitlab-xss-rst-001
tags:
  - xss
  - stored-xss
  - gitlab
  - restructuredtext
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:25.215Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-GitLab-README-rst

## Summary

This procedure exploits a persistent XSS vulnerability in GitLab's reStructuredText (RST) parser for README.rst files by injecting a malicious hyperlink using the javascript: URI scheme, leading to arbitrary JavaScript execution when users view and interact with the rendered project README.

## Description

GitLab renders README.rst files using an RST parser that fails to properly sanitize hyperlink targets, allowing attackers with project creation privileges to inject payloads. The attack involves creating a project, setting up a README.rst file, and embedding a payload like ``Security test link``__. __ javascript:alert(document.domain). When victims (e.g., project viewers or collaborators) click the link, the JavaScript executes in their browser context, potentially stealing cookies, session tokens, or performing other client-side attacks. This is a stored XSS variant, persisting across sessions and affecting multiple users. Prerequisites include a GitLab account; no advanced tools are needed, just the web interface.

## Requirements

1. Valid GitLab user account with permissions to create and edit projects
2. Access to a vulnerable GitLab instance (pre-8.14 versions affected)
3. Web browser for interaction and testing

## Defense

Defensive measures and detection strategies:

- Upgrade GitLab to version 8.14 or later, where RST sanitization is improved
- Disable RST rendering or use Markdown-only for README files
- Monitor project commits for suspicious RST content, such as javascript: schemes
- Implement Content Security Policy (CSP) to block inline JavaScript execution
- Educate users to avoid clicking untrusted links in project descriptions

## Objectives

1. Inject and persist a JavaScript payload in a GitLab project README.rst
2. Achieve execution of arbitrary code in victims' browsers upon interaction
3. Demonstrate potential for session hijacking or data exfiltration

## Instructions

### Step 1: Create and Initialize Project

**Context**: Set up a new repository to host the vulnerable file.

Navigate to your GitLab dashboard, click "New Project", enter a name, select visibility, and create an empty repository. Then, create an initial README.md with placeholder text (e.g., "Initial commit") and commit it.

> This initializes the repo; expected output is a successful commit and rendered README.

### Step 2: Rename to README.rst

**Context**: Switch to RST format to engage the vulnerable parser.

Edit the README.md file in the web interface, rename it to README.rst, keep or clear content, and commit the change.

> GitLab now parses the file as RST; verify by checking the rendered view for markup changes.

### Step 3: Inject the Payload

**Context**: Embed the XSS via RST hyperlink syntax to bypass sanitization.

Edit README.rst and replace content with:

````
``Security test link``__. __ javascript:alert(document.domain)
````

Commit the changes.

> The rendered page shows a clickable link; no errors indicate successful injection.

### Step 4: Trigger and Validate

**Context**: Interact to execute the payload and confirm vulnerability.

View the project README page and click the "Security test link". An alert should display the domain (e.g., gitlab.com).

> Success: JavaScript runs in the browser; failure: Link is sanitized or non-functional.

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
- stored-xss
- gitlab
- restructuredtext
