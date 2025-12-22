---
tags:
  - csp-bypass
  - gitlab
  - data-injection
type: procedure
tools:
  - '[[tools/Axios]]'
  - '[[tools/jQuery]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: ee0eb016-9ece-4799-9c77-0f8f22c000ab
created_at: '2025-12-14T00:11:16.641Z'
updated_at: '2025-12-14T00:11:16.642Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Bypass CSP in GitLab Using Data Attribute Injection

## Summary

This procedure bypasses GitLab's Content Security Policy by injecting data-diff-for-path attributes to load malicious JSON, which is then parsed and injected via jQuery, enabling script execution despite CSP restrictions.

## Description

The bypass exploits single_file_diff.js and popover handling, where data-diff-for-path allows loading arbitrary JSON paths. Combined with style injections for overlays, user clicks trigger axios requests to load JSON, which jQuery injects as HTML, executing scripts. This targets commit comments in GitLab projects.

## Requirements

1. CSP enabled on GitLab instance
2. Ability to create snippets, projects, and comments
3. Access to raw snippet URLs

## Defense

Defensive measures and detection strategies:

- Restrict data-diff-for-path to trusted sources
- Sanitize attributes in comments to prevent injections
- Monitor network requests for unexpected JSON loads

## Objectives

1. Upload malicious JSON and inject bypass payload
2. Trigger execution via user interaction
3. Achieve JS execution in CSP-protected environment

## Instructions

### Step 1: Enable CSP

**Context**: Configure CSP to block unauthorized scripts.

> Follow GitLab docs to set CSP via omnibus configuration.

### Step 2: Upload Malicious JSON

**Context**: Create a public snippet with executable JSON.

> Upload aaa.json: {"html":"<script>alert(document.domain)</script>"} and note raw path.

### Step 3: Create Project and Commit

**Context**: Set up a commit for commenting.

> Create project and commit README.md.

### Step 4: Add Bypass Payload Comment

**Context**: Inject payload with data-diff-for-path and styles.

> Add comment with payload to load JSON on interaction.

### Step 5: Trigger Bypass

**Context**: Interact to execute the script.

> Reload and click twice to load via axios and inject with jQuery.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Axios]]
- [[tools/jQuery]]

## Tags

- [[csp-bypass]]
- [[gitlab]]
