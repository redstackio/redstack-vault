---
id: proc-slack-direct-domain-redirect
tags:
  - open-redirect
  - anonymous
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
updated_at: '2025-12-14T17:24:27.327Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Use-Direct-Slack-Domain-for-Universal-Redirect

## Summary

This procedure uses the slack.com/files-pri domain directly for public file access, enabling redirects for both logged-in and anonymous users without additional chaining.

## Description

Direct links to files on slack.com bypass some checks on files.slack.com, serving HTML universally and executing scripts regardless of authentication status.

## Requirements

1. Public file link components (team, file_id, filename, pub_secret)

## Defense

- Consistent sanitization across all file serving domains
- Force downloads for non-image MIME types

## Objectives

1. Achieve universal access to malicious file
2. Trigger redirect without login

## Instructions

### Step 1: Form Direct Link

**Context**: Replace files.slack.com with slack.com in the public URL.

Example: https://slack.com/files-pri/T1ARLSGBS-F1AU0FTGR/pixel?pub_secret=094ca97aee

### Step 2: Verify Execution

**Context**: Access anonymously.

Browser should render HTML and redirect to evil.com.

> No prompt to download; direct execution.

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
- universal
