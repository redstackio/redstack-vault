---
id: proc-add-github-integration-001
name: Add-New-GitHub-Integration-and-Select-Repositories
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T03:16:37.461Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - integration-setup
  - repository-selection
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Add-New-GitHub-Integration-and-Select-Repositories

## Summary

This procedure creates a new GitHub integration in Slack and selects specific repositories, setting the stage for injecting payloads into configuration fields like the Branches option.

## Description

After linking accounts, this involves navigating to the integration creation flow in Slack, choosing the GitHub app, and selecting repositories to monitor for events like commits or PRs. The process exposes optional fields intended for branch filtering but vulnerable to injection. Expected outcome is a partially configured integration ready for payload insertion. Targets web-based Slack with connected GitHub.

## Requirements

1. Linked GitHub account in Slack
2. Slack permissions to add custom integrations
3. Access to GitHub repositories owned or accessible by the account

## Defense

Defensive measures and detection strategies:

- Audit integration additions for anomalous repository selections
- Implement rate limiting on integration setups
- Log all configuration changes for review

## Objectives

1. Configure integration to access target repositories
2. Reach the advanced configuration fields
3. Avoid triggering any early validation

## Instructions

### Step 1: Initiate New Integration

**Context**: Start the GitHub integration setup process.

In Slack, go to Settings > Apps > Add apps, search for GitHub, and select 'Add Configuration'.

### Step 2: Select Repositories

**Context**: Choose repositories to integrate.

From the list of accessible GitHub repos, select one or more to monitor, then proceed to optional settings.

> The form advances to fields like Branches without errors if selections are valid.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[integration-setup]]
- [[repository-selection]]
