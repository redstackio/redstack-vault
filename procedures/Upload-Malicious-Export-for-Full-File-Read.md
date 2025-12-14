---
tags:
  - gitlab-import
  - secrets-leak
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-25T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:08.351Z'
sub_techniques: []
id: fba73091-249b-4639-8d34-aaa57117cd12
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Malicious-Export-for-Full-File-Read

## Summary

This procedure uploads a project.json-symlinked export to GitLab, triggering full arbitrary file read via symlink dereference in the restoration process.

## Description

Using the import interface, the tampered archive causes IO.read to follow the symlink and load the full file as JSON, resulting in a parse error that leaks the entire content. Scenario: Attacker with import access targets config files or secrets. Outcomes: Access to Rails secrets, tokens, enabling further exploitation.

## Requirements

1. Archive with project.json symlink
2. Permissions for project import
3. GitLab web access

## Defense

Defensive measures and detection strategies:

- Block symlink following in file restoration code
- Size-limit and validate imported files
- Alert on JSON parse errors containing non-JSON data

## Objectives

1. Exploit restoration to read full file
2. Leak application secrets
3. Set up for RCE chain

## Instructions

### Step 1: Initiate Import

**Context**: Select export import option.

Visit project creation page and choose GitLab export import.

### Step 2: Submit Malicious File

**Context**: Upload to trigger processing.

Select and upload test.tar.gz.

**Expected Output**: ActiveSupport::JSON.decode error with full file contents (e.g., complete /etc/passwd or secrets.yml).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab-import]]
- [[secrets-leak]]
