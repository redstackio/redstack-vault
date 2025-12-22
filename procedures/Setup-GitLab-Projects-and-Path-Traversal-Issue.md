---
tags:
  - gitlab
  - path-traversal
type: procedure
tools:
  - '[[tools/Rails-Console]]'
  - '[[tools/curl]]'
  - '[[tools/cat]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/rails-request-setup]]'
  - '[[commands/rails-set-serializer]]'
  - '[[commands/rails-cookie-jar]]'
  - '[[commands/rails-erb-payload]]'
  - '[[commands/rails-deprecated-proxy]]'
  - '[[commands/rails-set-signed-cookie]]'
  - '[[commands/rails-print-cookie]]'
  - '[[commands/curl-send-malicious-cookie]]'
  - '[[commands/cat-verify-file]]'
platforms:
  - Web
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 0206f2f5-97f6-436d-8f71-11721994217b
created_at: '2025-12-11T06:10:40.445Z'
updated_at: '2025-12-11T06:10:40.445Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Setup GitLab Projects and Path Traversal Issue

## Summary

This procedure sets up two GitLab projects and creates an issue in the source project with a Markdown description containing a path traversal payload to reference arbitrary files.

## Description

The vulnerability allows arbitrary file reads by exploiting the UploadsRewriter during issue movement. This setup prepares the environment by creating projects and embedding a traversal path in Markdown image syntax, enabling file copying without validation.

## Requirements

1. Access to a vulnerable GitLab instance
2. Permissions to create projects and issues
3. Knowledge of target file paths (e.g., /etc/passwd)

## Defense

Defensive measures and detection strategies:

- Validate file paths in Markdown references
- Monitor issue movement logs for suspicious paths

## Objectives

1. Prepare projects for issue transfer
2. Embed traversal payload
3. Enable arbitrary file access

## Instructions

### Step 1: Create Source and Destination Projects

**Context**: Set up two projects in GitLab for moving the issue between them.

Create the projects via GitLab UI or API.

### Step 2: Add Issue with Traversal Payload

**Context**: Create an issue in the source project with Markdown containing the traversal.

Use syntax like: ![image](/uploads/11111111111111111111111111111111/../../../../../../../../../../../../../../etc/passwd)

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- gitlab
- path-traversal
