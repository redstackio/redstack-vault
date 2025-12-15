---
id: proc-view-pullrequests
tags:
  - exfiltration
  - source-code
  - pull-requests
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:58.345Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Gain Access to Pull Requests and Source Code

## Summary

This procedure navigates the unauthorized PullRequest session to view pull requests in the HackerOne infrastructure codebase, exposing sensitive source code.

## Description

Once in the organization, access the pull requests view to see diffs and code. Target: PullRequest web interface. Prerequisites: SSO access. Outcome: Unauthorized data exposure.

## Requirements

1. Active PullRequest session via SSO
2. Organization membership (via bypassed account)
3. Browser access

## Defense

Defensive measures and detection strategies:

- Restrict pull request visibility to authorized roles only
- Log and alert on access to sensitive repos from new accounts
- Use DLP to monitor code views/downloads

## Objectives

1. Expose internal source code
2. Demonstrate impact of auth bypass
3. Collect intelligence on infrastructure

## Instructions

### Step 1: Navigate to Pull Requests

**Context**: Load the pull requests section in the target organization.

No command; manual:

In PullRequest dashboard, select the HackerOne organization and go to Pull Requests.

> Expected: List of PRs with source code diffs visible, including infrastructure codebase.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- exfiltration
- source-code
- pull-requests
