---
tags:
  - xss
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-05T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:37.079Z'
sub_techniques: []
id: 64fc9720-fa64-4501-9266-7484b5637387
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload into Post Title

## Summary

This procedure describes entering a JavaScript payload into the WordPress post title field, leveraging privileged user permissions to bypass sanitization and store malicious code.

## Description

WordPress 5.3 allows admins and editors to post unfiltered HTML, including <script> tags, in titles and content. This technique exploits that by injecting XSS in the title, which is rendered without escaping on the frontend. The scenario targets authenticated users aiming to compromise viewers via script execution, such as alerting the domain or exfiltrating cookies.

## Requirements

1. Active admin dashboard session
2. Access to Posts > Add New interface
3. Knowledge of a basic XSS payload (e.g., <script>alert(document.domain);</script>)

## Defense

Defensive measures and detection strategies:

- Disable unfiltered HTML for non-super admins via role capabilities
- Use content security policy (CSP) headers to block inline scripts
- Audit posts for suspicious HTML using security plugins

## Objectives

1. Insert unsanitized script into post metadata
2. Ensure payload persists in the editor
3. Set up for storage and later execution

## Instructions

### Step 1: Access Post Creation

**Context**: Navigate to the post editor to input the title.

From the dashboard, select Posts > Add New.

> The editor loads with empty title and body fields.

### Step 2: Enter Payload

**Context**: Place the XSS script directly in the title.

Type `<script>alert(document.domain);</script>` into the title field. Optionally add neutral body text.

> The field accepts the input without stripping tags, confirming unfiltered mode.

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
- [[injection]]
