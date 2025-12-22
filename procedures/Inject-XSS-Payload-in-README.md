---
id: proc-uuid-3
name: Inject-XSS-Payload-in-README
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:30.890Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss-payload
  - javascript-injection
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Inject-XSS-Payload-in-README

## Summary

This procedure inserts a malicious RDoc payload into the README.rdoc file, creating a clickable link that executes arbitrary JavaScript when rendered and interacted with in GitLab.

## Description

The payload exploits the RDoc parser's handling of link syntax, such as [label:JaVaScriPt:alert(1)], where the mixed-case 'JaVaScriPt' evades basic filters and generates an <a> tag with a javascript: URI. This stored XSS persists in the repository and affects all viewers clicking the link, potentially leading to session hijacking. The attack requires no additional tools, relying on GitLab's web editor.

## Requirements

1. README.rdoc file in the project
2. Edit access to the file
3. Understanding of RDoc link syntax for payload crafting

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to block inline JavaScript
- Use output encoding for all markup-generated HTML
- Scan repositories for suspicious strings like 'JaVaScriPt' in commits

## Objectives

1. Embed executable JavaScript in the rendered README
2. Ensure the payload renders as a clickable link
3. Enable client-side execution for any viewer

## Instructions

### Step 1: Open File for Editing

**Context**: Access the vulnerable file.

In GitLab, navigate to README.rdoc and click 'Edit'.

### Step 2: Insert Payload

**Context**: Add the crafted content.

Clear existing content and paste: `XSS[JaVaScriPt:alert(1)] <-- click to test`. This creates the malicious link.

### Step 3: Preview and Save

**Context**: Validate before committing.

Use the preview tab to check rendering, then commit with a neutral message like 'Update documentation'.

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
- [[payload-injection]]
