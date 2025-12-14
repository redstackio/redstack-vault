---
tags:
  - gitlab
  - wiki
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: a8e5b83e-d6ea-4978-8d13-23fb922c1053
created_at: '2025-12-14T00:11:16.539Z'
updated_at: '2025-12-14T00:11:16.539Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create GitLab Wiki Page

## Summary

This procedure involves creating a new wiki page in a GitLab project, serving as the initial step for injecting malicious content in vulnerabilities like stored XSS.

## Description

In GitLab, projects can have associated wikis for documentation. This procedure accesses the wiki feature to create a blank page, which can then be used to test or exploit rendering vulnerabilities in formats like RDoc. It targets web-based GitLab instances running on Linux with supporting services like PostgreSQL and Redis. The expected outcome is a new editable page ready for content insertion.

## Requirements

1. Valid GitLab account with project access
2. Permissions to create and edit wiki pages
3. Web browser for accessing GitLab interface

## Defense

Defensive measures and detection strategies:

- Monitor wiki creation and edits for suspicious activity
- Implement access controls to limit wiki modifications

## Objectives

1. Establish a wiki page for payload testing
2. Prepare for vulnerability exploitation
3. Confirm access to rendering engine

## Instructions

### Step 1: Access Project Wiki

**Context**: Navigate to the target GitLab project and enable the wiki if not already active.

Access the project sidebar, select 'Wiki', and click 'Create your first page' or similar to start a new page.

> This sets up the page for editing without executing any commands.

### Step 2: Confirm Page Creation

**Context**: Ensure the page is created and editable.

Save an empty or test page to verify functionality.

> Expected: Page appears in the wiki list.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[gitlab]]
- [[wiki]]
