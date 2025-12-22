---
tags:
  - path-traversal
  - gitlab
type: procedure
tools:
  - '[[tools/Rails-Console]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 723d3ecc-bf2b-4cd2-85db-982f80a3f91d
created_at: '2025-12-11T03:47:59.329Z'
updated_at: '2025-12-11T03:47:59.329Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Create Projects and Malicious Issue for Path Traversal

## Summary

This procedure sets up two GitLab projects and creates an issue with markdown containing a path traversal payload to reference arbitrary files, preparing for exploitation during issue movement.

## Description

In GitLab versions prior to 12.9.1, the UploadsRewriter lacks file name validation, allowing directory traversal via markdown in issues. This enables copying arbitrary files when moving issues between projects. The procedure targets the MARKDOWN_PATTERN regex and find_file method.

## Requirements

1. Authenticated GitLab account with project creation permissions
2. Access to GitLab web interface
3. Knowledge of target file paths (e.g., /etc/passwd)

## Defense

Defensive measures and detection strategies:

- Update to GitLab 12.9.1 or later
- Monitor issue movement logs for unusual file references

## Objectives

1. Prepare environment for file read exploit
2. Embed traversal payload in issue description
3. Enable arbitrary file access

## Instructions

### Step 1: Create Source and Destination Projects

**Context**: Set up two projects to facilitate issue movement.

Use the GitLab UI to create two new projects.

### Step 2: Add Issue with Traversal Markdown

**Context**: Create an issue in the source project with malicious markdown.

**Command** ([[commands/gitlab-markdown-traversal]]):
```markdown
![a](/uploads/11111111111111111111111111111111/../../../../../../../../../../../../../../etc/passwd)
```

> This markdown references an arbitrary file via path traversal, exploiting the lack of validation in UploadsRewriter.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/gitlab-markdown-traversal]]

## Tools Used



## Tags

- path-traversal
- gitlab
