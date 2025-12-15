---
id: proc-trigger-rce-render
tags:
  - rce
  - render
  - kramdown
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
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:24:15.034Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---
# Trigger-RCE-by-Rendering-Wiki-Page

## Summary

This procedure loads the malicious wiki page in GitLab UI, triggering Kramdown rendering and executing the Ruby payload via directory traversal.

## Description

Wiki rendering pipeline: render_wiki_content -> GitHub::Markup.render -> Kramdown::Document.new with Rouge. Unsafe options allow const_get('Redis') and require on traversed path, loading payload.rb for RCE.

## Requirements

1. Malicious file pushed to wiki
2. Access to GitLab wiki UI
3. Server logs accessible for verification

## Defense

Defensive measures and detection strategies:

- Patch Kramdown/Rouge validation
- Log rendering errors with traversal patterns
- Disable .rmd rendering or sanitize options

## Objectives

1. Execute arbitrary Ruby code on server
2. Confirm RCE via log indicators

## Instructions

### Step 1: Refresh Wiki

**Context**: Update sidebar to show new page.

No command; navigate to Project > Wiki, refresh.

> page1 appears on right-hand side.

### Step 2: Load Page

**Context**: Click to render, triggering pipeline.

No command; click page1.md.

> Rendering executes payload; check logs for "wrong constant name [path]".

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Command-Line Interface]] Command and Scripting Interpreter

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- rce
- render
- kramdown
