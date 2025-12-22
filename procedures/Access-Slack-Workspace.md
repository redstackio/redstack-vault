---
tags:
  - slack
  - access
  - web
type: procedure
tools:
  - '[[tools/Slack-Self-XSS-Demonstration-Video]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:15:31.805Z'
sub_techniques: []
id: 048fdca1-341c-49c6-aca7-ec46e359e83f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Slack-Workspace

## Summary

This procedure outlines how to log in and access a Slack workspace, serving as the initial entry point for exploiting features like post creation in a self-XSS attack.

## Description

In the context of a self-XSS vulnerability in Slack, accessing the workspace is the prerequisite step to reach the post creation editor. This involves navigating to the workspace URL and authenticating with user credentials. The procedure assumes legitimate account access and targets web-based Slack interfaces. Expected outcome is a fully loaded workspace ready for further actions, with no execution risks at this stage.

## Requirements

1. Valid Slack account credentials (username/email and password)
2. Web browser (e.g., Firefox for optimal vulnerability reproduction)
3. Internet access to the Slack domain

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) to prevent unauthorized access
- Monitor login attempts from unusual IP addresses or locations

## Objectives

1. Establish a authenticated session in the Slack workspace
2. Prepare for post creation without triggering alerts
3. Ensure browser compatibility for subsequent execution

## Instructions

### Step 1: Navigate and Authenticate

**Context**: Open the browser and direct it to the Slack workspace to initiate login.

No command required; perform the following UI interaction:

Navigate to the workspace URL (e.g., `https://accountname.slack.com`).

> If not logged in, enter credentials and complete authentication. Upon success, the workspace interface loads, confirming access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Slack-Self-XSS-Demonstration-Video]]

## Tags

- [[slack]]
- [[access]]
