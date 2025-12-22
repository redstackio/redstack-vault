---
tags:
  - file-read
  - gitlab
type: procedure
tools:
  - '[[tools/Rails-Console]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
  - Linux
techniques:
  - '[[File and Directory Discovery]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: de02dd40-c399-4892-bc95-5a63a669ab00
created_at: '2025-12-11T03:47:59.326Z'
updated_at: '2025-12-11T03:47:59.326Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1083]]'
---
# Move Issue to Trigger Arbitrary File Read

## Summary

This procedure moves a malicious issue between GitLab projects to trigger the UploadsRewriter, copying arbitrary files via path traversal without validation.

## Description

By moving the issue, the regex in UploadsRewriter matches the traversal path and copies files like /etc/passwd or secrets.yml to the destination project, allowing read access to sensitive data.

## Requirements

1. Two existing GitLab projects
2. Issue with traversal markdown in source project
3. Permissions to move issues

## Defense

Defensive measures and detection strategies:

- Patch GitLab to 12.9.1
- Audit upload and issue movement activities

## Objectives

1. Copy arbitrary files to accessible location
2. Access sensitive configurations
3. Prepare for escalation

## Instructions

### Step 1: Initiate Issue Move

**Context**: Use GitLab UI to move the issue to the destination project.

Select the issue and choose the move option, selecting the target project.

### Step 2: Verify Copied File

**Context**: Check the destination project's uploads for the arbitrary file.

Access the issue in the new project and view the referenced file.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- file-read
- gitlab
