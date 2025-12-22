---
id: proc-slack-invoke-command
tags:
  - ssrf
  - invocation
  - trigger
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
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T03:46:14.473Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Invoke-Slack-Slash-Command

## Summary

This procedure triggers the SSRF by invoking the custom slash command in a Slack workspace, causing the server to fetch the redirect URL and access internal IPv6 services.

## Description

Invocation sends a request from Slack's backend to the configured URL, following the PHP redirect to internal endpoints. This exploits the vulnerability for service disclosure. Target: Slack channel. Outcomes: Proxied response from internal services in the chat.

## Requirements

1. Installed custom app with configured slash command
2. Access to a Slack channel in the workspace
3. No additional tools; uses Slack UI

## Defense

Defensive measures and detection strategies:

- Proxy and inspect outgoing requests from Slack servers
- Rate-limit slash command invocations
- Block responses containing internal banners

## Objectives

1. Execute the SSRF payload via command trigger
2. Proxy internal service responses to attacker
3. Validate exploitation success

## Instructions

### Step 1: Open Slack Channel

**Context**: Prepare the environment for invocation.

Join or create a channel in the target workspace where the app is installed.

> Channel ready for messaging.

### Step 2: Type and Send Command

**Context**: Trigger the backend request.

Type `/yourslash` (or your custom name) in the message box and press Enter.

> Message sends; Slack processes the command.

### Step 3: Monitor Response

**Context**: Await the SSRF result.

Watch for the bot response in the channel, which may include loading indicators.

> Response appears, potentially with internal data or errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[invocation]]
- [[trigger]]
