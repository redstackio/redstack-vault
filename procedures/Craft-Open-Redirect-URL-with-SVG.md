---
id: proc-slack-craft-redirect-104087
tags:
  - open-redirect
  - url-crafting
  - phishing
  - slack
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:26.093Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft-Open-Redirect-URL-with-SVG

## Summary

This procedure constructs a malicious URL using Slack's /checkcookie endpoint and the public SVG link in the redir parameter, bypassing the domain restriction since the SVG is on a Slack-hosted domain.

## Description

The /checkcookie endpoint was patched to only allow redirects to slack.com domains, but Slack file URLs qualify. By setting redir to the public SVG URL, the endpoint redirects to it, and the SVG's onload JavaScript then redirects further to an external site, re-enabling open redirects for phishing.

## Requirements

1. Public SVG URL from previous step.
2. Knowledge of the /checkcookie endpoint.
3. Text editor or URL builder for crafting.

## Defense

Defensive measures and detection strategies:

- Enhance /checkcookie to validate redir paths beyond domain, e.g., block file.slack.com redirects.
- Log and monitor unusual redir parameter values.
- Educate users on suspicious Slack links.

## Objectives

1. Bypass open redirect domain checks.
2. Chain redirect to SVG execution.
3. Create a phishing-ready link.

## Instructions

### Step 1: Prepare the Base URL

**Context**: Start with the Slack checkcookie endpoint.

Use: https://slack.com/checkcookie?redir=

### Step 2: Append SVG Public URL

**Context**: Insert the full public SVG link as the redir value.

Construct: https://slack.com/checkcookie?redir=https://files.slack.com/files-pri/T0E7QLVLL-F0G41EG2W/redirect.svg?pub_secret=7a6caed489

> Test in browser: It should redirect to the SVG without blocking.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[open-redirect]]
- [[url-crafting]]
- [[Phishing]]
- [[slack]]
