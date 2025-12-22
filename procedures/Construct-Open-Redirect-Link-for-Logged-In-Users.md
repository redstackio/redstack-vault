---
id: proc-slack-checkcookie-redirect
tags:
  - open-redirect
  - logged-in
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
updated_at: '2025-12-14T17:24:27.330Z'
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
# Construct-Open-Redirect-Link-for-Logged-In-Users

## Summary

This procedure chains a public file link with Slack's checkcookie endpoint to bypass restrictions and redirect authenticated users to arbitrary domains.

## Description

The checkcookie endpoint allows redir parameters, combined with the malicious file URL to force execution in the context of a logged-in session, enhancing phishing success.

## Requirements

1. Public file link from previous step

## Defense

- Validate and whitelist redirect URLs in checkcookie
- Log and alert on suspicious redir parameters

## Objectives

1. Create functional redirect for logged-in victims
2. Bypass session checks

## Instructions

### Step 1: Build Chained URL

**Context**: Append public file URL to checkcookie redir.

Construct: https://slack.com/checkcookie?redir=https://files.slack.com/files-pri/T1ARLSGBS-F1AU0FTGR/pixel?pub_secret=094ca97aee

### Step 2: Test Redirect

**Context**: Open in logged-in browser.

Should redirect to http://www.evil.com via the HTML script.

> Success if no errors and redirect occurs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- open-redirect
- slack
