---
id: proc-uuid-2
name: Configure-README-as-RDoc
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:30.893Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - rdoc
  - markup-config
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Configure-README-as-RDoc

## Summary

This procedure renames the README file to use the .rdoc extension, forcing GitLab to parse it with the vulnerable RDoc markup engine, which lacks proper JavaScript sanitization.

## Description

GitLab supports multiple markup formats for README files, including RDoc, reStructuredText, and Textile. By specifying README.rdoc, the parser switches to RDoc mode, where specially crafted links like [label:javascript:payload] bypass sanitization and execute on render. This step is crucial for targeting the specific vulnerability without affecting other formats unnecessarily. Prerequisites include an existing project with a README file.

## Requirements

1. Existing GitLab project with a README file
2. Edit permissions on the repository
3. Knowledge of GitLab's file naming conventions

## Defense

Defensive measures and detection strategies:

- Disable legacy markup parsers like RDoc in GitLab configurations
- Sanitize all user-generated markup inputs server-side
- Log file extension changes and scan for suspicious patterns

## Objectives

1. Activate the vulnerable RDoc parsing mode
2. Prepare for payload insertion without immediate detection
3. Ensure compatibility with the exploit chain

## Instructions

### Step 1: Edit File Name

**Context**: Change the extension to trigger RDoc.

In the GitLab repository, select the README file, click 'Edit', and rename it to README.rdoc in the file name field.

### Step 2: Save Changes

**Context**: Commit the rename to update the repository.

Add a commit message like 'Update README format' and commit the change.

### Step 3: Verify Rendering

**Context**: Confirm the parser switch.

View the project page to ensure the README renders without errors, indicating RDoc is active.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[rdoc]]
- [[file-config]]
