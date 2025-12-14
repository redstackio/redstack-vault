---
tags:
  - slack
  - post-creation
  - web
type: procedure
tools:
  - '[[tools/Slack-Self-XSS-Demonstration-Video]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:31.801Z'
sub_techniques: []
id: 1959ec2f-18ef-45f6-bec6-5cfc8917b32f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Initiate-Slack-Post-Creation

## Summary

This procedure describes starting a new post in Slack to access the vulnerable editor for payload injection in a self-XSS scenario.

## Description

Once in the Slack workspace, this step opens the post creation interface, which contains the text editor susceptible to self-XSS when code formatting is applied. The target environment is the web version of Slack, and the outcome is an open editor ready for input. No privileges beyond standard user access are needed.

## Requirements

1. Active Slack workspace session
2. Access to the main workspace dashboard
3. Web browser with JavaScript enabled

## Defense

Defensive measures and detection strategies:

- Rate-limit post creation attempts to prevent abuse
- Log editor interactions for anomaly detection

## Objectives

1. Open the post creation editor
2. Expose the formatting toolbar for exploitation
3. Set up for payload entry without session disruption

## Instructions

### Step 1: Select Post Creation Option

**Context**: Use the workspace UI to begin creating a post.

No command required; perform the following UI interaction:

Click the plus (+) sign below the workspace name and select 'Create Post' from the menu.

> The post editor opens, displaying a text area and toolbar, indicating successful initiation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Slack-Self-XSS-Demonstration-Video]]

## Tags

- [[slack]]
- [[post-creation]]
