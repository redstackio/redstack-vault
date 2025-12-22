---
id: proc-001
tags:
  - xss
  - dom-xss
  - gitlab
  - csp-bypass
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:13.906Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Demonstrate DOM-based XSS in GitLab Gemfile Preview

## Summary

This procedure demonstrates a DOM-based Cross-Site Scripting (XSS) vulnerability in GitLab's Gemfile preview feature, where double conversion of URLs to HTML links causes improper rendering of malicious payloads, such as nested <a> tags around <img> elements with JavaScript onerror handlers. The attack requires a GitLab user account and results in HTML/CSS injection on protected instances like gitlab.com due to Content Security Policy (CSP), but can lead to full JavaScript execution in unpatched GitLab Community Edition (CE) or Enterprise Edition (EE) deployments.

## Description

The vulnerability stems from GitLab's display logic in the Gemfile preview, which converts gem URLs twice: first to links and then again during rendering, allowing attacker-controlled HTML to bypass sanitization. An attacker creates a project and uploads a Gemfile with a payload like `gem '<img/src/onerror=alert(location)>','2'`, then previews it. This injects executable HTML, but CSP on gitlab.com blocks the alert(). In self-hosted instances without CSP or updates, this enables arbitrary JavaScript, potentially stealing cookies or performing actions on behalf of the user. The procedure assumes access to a GitLab instance and focuses on reproduction for reporting or testing.

## Requirements

1. Valid GitLab user account with permissions to create projects and files
2. Web browser with developer tools enabled (e.g., Chrome, Firefox)
3. Access to GitLab web interface (gitlab.com or self-hosted)

## Defense

Defensive measures and detection strategies:

- Enable and configure strict CSP headers to block inline JavaScript execution
- Sanitize user-controlled content in preview features, avoiding double encoding/decoding of HTML
- Regularly update GitLab to patched versions (post-report fixes in future releases)
- Monitor for anomalous HTML rendering in logs or browser consoles

## Objectives

1. Reproduce the DOM-based XSS to confirm vulnerability presence
2. Assess impact by observing CSP interactions and potential JS execution
3. Document payload rendering for vulnerability reporting

## Instructions

### Step 1: Authenticate to GitLab

**Context**: Gain access to the platform to perform subsequent actions.

Navigate to your GitLab instance (e.g., gitlab.com) and log in with valid credentials.

> Successful login redirects to the user dashboard, confirming access.

### Step 2: Create a New Project

**Context**: Establish a repository to host the malicious file without affecting existing projects.

From the dashboard, select 'New Project > Create blank project', provide a name, and create it.

> The project page loads with an empty repository, ready for file addition.

### Step 3: Add Malicious Gemfile

**Context**: Introduce the payload that exploits the double conversion during preview.

In the project, click 'New file', name it 'Gemfile', and enter the payload: `gem '<img/src/onerror=alert(location)>','2'`. Commit with a message like 'Add Gemfile'.

> The file is committed, and its content is stored in the repository.

### Step 4: Trigger Preview

**Context**: Render the file to activate the vulnerable URL-to-link conversion logic.

Open the Gemfile, switch to the editor view, and click the 'Preview' tab.

> The preview renders the content, injecting the <img> tag inside a converted <a> link, visible via element inspection.

### Step 5: Inspect for XSS

**Context**: Validate the injection and CSP effects using browser tools.

Open developer tools (F12), go to the Console, and refresh the preview. Check for errors.

> Console displays CSP violations like 'Refused to execute inline script because it violates CSP', confirming blocked JS but successful HTML injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- dom-xss
- gitlab
- csp
