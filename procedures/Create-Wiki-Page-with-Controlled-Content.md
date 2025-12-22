---
tags:
  - gitlab
  - setup
type: procedure
tools:
  - '[[tools/ssh]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 3af07493-3d1d-412c-b7e2-ba391bfb424e
created_at: '2025-12-11T03:47:47.603Z'
updated_at: '2025-12-11T03:47:47.603Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Create Wiki Page with Controlled Content

## Summary

This procedure involves creating a new wiki page in a GitLab project with a specific commit message to control the content that will be used in subsequent file overwrite exploits.

## Description

In the context of exploiting Git flag injection in GitLab, this step sets up the necessary commit data that will be written to arbitrary files. It targets the wiki functionality and requires API access to create pages. The expected outcome is a controlled commit that can be leveraged for injection.

## Requirements

1. Valid GitLab API token
2. Access to a project with wiki enabled
3. HTTP access to GitLab instance

## Defense

Defensive measures and detection strategies:

- Monitor API calls for unusual wiki creations
- Restrict wiki access to trusted users

## Objectives

1. Establish controlled content in Git commit
2. Prepare for flag injection
3. Enable file overwrite with known data

## Instructions

### Step 1: Create the Wiki Page

**Context**: Use the GitLab UI or API to create a new wiki page named 'page' with commit message 'controlled content'.

> This sets the commit log that will be output during injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[commands/curl-gitlab-search-api]]
- #setup
