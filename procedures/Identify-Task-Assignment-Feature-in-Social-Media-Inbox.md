---
id: proc-uuid-1
name: Identify Task Assignment Feature in Social Media Inbox
tags:
  - recon
  - idor
  - semrush
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:34.613Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Identify Task Assignment Feature in Social Media Inbox

## Summary

This procedure involves navigating the Semrush Social Media Inbox tool to identify the task assignment feature, which allows delegating message management to colleagues, setting the stage for IDOR testing.

## Description

In the context of testing Semrush's web-based Social Media Inbox, this procedure focuses on exploring the tool's functionality for linking social media accounts and using the task tracker to assign messages. The target environment is the Semrush web application, requiring a valid user account. Expected outcomes include confirmation of the feature's presence and understanding its workflow, which may reveal authorization gaps.

## Requirements

1. Valid Semrush account with access to Social Media Inbox
2. Web browser with JavaScript enabled
3. Network access to Semrush platform

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) to limit feature visibility
- Log all feature explorations and alert on unusual navigation patterns

## Objectives

1. Locate the task assignment interface
2. Understand delegation workflow
3. Identify potential entry points for IDOR exploitation

## Instructions

### Step 1: Access Social Media Inbox

**Context**: Log in and navigate to the tool to begin exploration.

Log in to your Semrush account and select the Social Media Inbox from the dashboard.

### Step 2: Link Accounts and Explore Task Tracker

**Context**: Set up the environment and identify the assignment feature.

Link any required social media accounts, then open the task tracker section. Observe options for assigning messages to users.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- recon
- idor
- semrush
