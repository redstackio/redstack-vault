---
id: proc-connect-github-slack-001
name: Connect-GitHub-Account-to-Slack
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T03:16:37.462Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - integration-setup
  - account-linking
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

# Connect-GitHub-Account-to-Slack

## Summary

This procedure establishes a connection between a GitHub account and a Slack workspace, enabling subsequent integration setups that can be exploited for vulnerabilities like stored XSS.

## Description

In the context of exploiting Slack's GitHub integration, this step involves authenticating the user's GitHub account via OAuth or similar authorization flow within Slack's web interface. It requires a valid GitHub account and Slack permissions to add apps/integrations. The outcome is a linked account that allows access to GitHub repositories for monitoring in Slack channels. Prerequisites include active accounts on both platforms and browser access to Slack.

## Requirements

1. Valid Slack user account with integration setup permissions
2. Valid GitHub account with accessible repositories
3. Modern web browser with JavaScript enabled

## Defense

Defensive measures and detection strategies:

- Enforce least-privilege for integration setups (e.g., require admin approval)
- Monitor OAuth authorization logs for unusual account linkages
- Use browser security features like Content Security Policy (CSP) to limit third-party integrations

## Objectives

1. Gain authorized access to GitHub data within Slack
2. Prepare for integration configuration that exposes input fields
3. Enable payload injection in subsequent steps

## Instructions

### Step 1: Navigate to Slack Integrations

**Context**: Access the integrations section in Slack to initiate GitHub connection.

Go to Slack's Apps & Integrations menu and search for GitHub.

### Step 2: Authorize GitHub Account

**Context**: Complete the OAuth flow to link accounts.

Click 'Add to Slack', authenticate with GitHub credentials, and grant necessary permissions (e.g., repository access).

> Upon success, Slack displays a confirmation that the GitHub account is connected.

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
- [[account-linking]]
