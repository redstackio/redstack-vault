---
id: proc-weblate-navigate-project-001
tags:
  - navigation
  - project-setup
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:18.954Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Navigate-to-Add-New-Translation-Project

## Summary

This procedure uses the web interface to reach the translation project creation page, setting the stage for initiating the trial signup request.

## Description

As part of the race condition exploitation, this step maneuvers the application to the point where the trial prompt appears. It targets the Django-based web app at hosted.weblate.org. No tools beyond a proxied browser are needed. Expected outcome: Interface ready for trial button interaction.

## Requirements

1. Logged-in account from prior setup
2. Proxied browser session active
3. No additional privileges required

## Defense

Defensive measures and detection strategies:

- Log navigation patterns to detect scripted or automated flows
- Implement session timeouts for idle project creation
- CAPTCHA on project addition for bots

## Objectives

1. Access project creation UI
2. Prepare for trial activation
3. Ensure state for request capture

## Instructions

### Step 1: Access Project Addition

**Context**: Locate and trigger the project creation flow.

After login, click the top '+' icon in the dashboard, then select 'add a new translation project' from the menu.

> The page should load with fields for project details, and the trial option visible if limits are exceeded.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- navigation
- project-setup
