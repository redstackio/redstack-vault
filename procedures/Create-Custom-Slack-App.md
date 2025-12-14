---
id: proc-slack-create-app
tags:
  - slack
  - app-creation
  - ssrf-setup
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:14.479Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Custom-Slack-App

## Summary

This procedure sets up a custom Slack application on api.slack.com, enabling the configuration of slash commands necessary for SSRF exploitation targeting internal IPv6 services.

## Description

In the context of exploiting SSRF in Slack, creating a custom app provides the foundation for configuring malicious slash commands. The target environment is any Slack workspace where the attacker has app creation permissions. Expected outcomes include an active app with slash command support, allowing subsequent URL configuration for redirects to internal endpoints like [::]:22. Prerequisites include a valid Slack account and web access to api.slack.com.

## Requirements

1. Slack account with permissions to create and install apps in a workspace
2. Web browser for accessing api.slack.com
3. No special tools required beyond standard web navigation

## Defense

Defensive measures and detection strategies:

- Restrict app creation to trusted admins via workspace settings
- Monitor api.slack.com logs for unusual app configurations
- Implement URL whitelisting for slash command requests

## Objectives

1. Establish a custom app as the entry point for SSRF payload
2. Enable slash command feature for request forgery
3. Prepare for internal service access via redirects

## Instructions

### Step 1: Access Slack App Dashboard

**Context**: Log in to initiate app creation.

Navigate to https://api.slack.com/apps and sign in with your Slack credentials.

> Successful login redirects to the app management dashboard.

### Step 2: Create New App

**Context**: Build the app from scratch to include slash commands.

Click 'Create New App', select 'From scratch', enter an app name (e.g., "TestApp"), and choose your target workspace.

> App creation completes, showing the basic app settings page.

### Step 3: Enable Slash Commands

**Context**: Add the slash command feature to the app.

In the left sidebar, select 'Slash Commands' > 'Create New Command'. Set command name to /yourslash and provide a brief description.

> Slash command added; configuration options appear for URL setup in next steps.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[slack]]
- [[app-creation]]
- [[ssrf-setup]]
