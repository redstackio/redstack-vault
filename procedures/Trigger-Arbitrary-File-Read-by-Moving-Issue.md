---
tags:
  - gitlab
  - arbitrary-file-read
type: procedure
tools:
  - '[[tools/Rails-Console]]'
  - '[[tools/curl]]'
  - '[[tools/cat]]'
tactics:
  - '[[Discovery]]'
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
  - '[[Use Alternate Authentication Material]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: ebcb9461-af22-435a-9715-da0665d5c751
created_at: '2025-12-11T06:10:40.441Z'
updated_at: '2025-12-11T06:10:40.441Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1550]]'
---
# Trigger Arbitrary File Read by Moving Issue

## Summary

This procedure moves the prepared issue to the destination project, triggering the file copy via UploadsRewriter.

## Description

Moving the issue invokes the vulnerable code, copying the referenced file to the new project without path validation, allowing access to sensitive files.

## Requirements

1. Projects and issue from previous setup
2. Permissions to move issues

## Defense

Defensive measures and detection strategies:

- Implement path sanitization in UploadsRewriter
- Audit file access logs

## Objectives

1. Copy arbitrary file
2. Access sensitive data

## Instructions

### Step 1: Move the Issue

**Context**: Use GitLab UI or API to move the issue to the destination project.

This action copies the file specified in the traversal path.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Use Alternate Authentication Material]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- gitlab
- arbitrary-file-read
