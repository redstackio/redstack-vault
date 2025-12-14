---
id: p3q4r5s6-t7u8-9012-defg-hi3456789012
tags:
  - navigation
  - ui
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:53.511Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Navigate-to-Bounty-Preferences

## Summary

This procedure directs the authenticated user to the HackerOne preferences page where the Bounty Preferences slider is located, setting the stage for triggering the vulnerable GraphQL mutation.

## Description

After authentication, navigating to the settings allows interaction with invitation preferences. This is a standard UI navigation step in the web environment, leading to the exposure of client-side controls that can be bypassed.

## Requirements

1. Active HackerOne session
2. Browser access

## Defense

Defensive measures and detection strategies:

- Session timeout enforcement
- Access logging for settings pages

## Objectives

1. Load preferences interface
2. Expose bounty slider

## Instructions

### Step 1: Access Settings

**Context**: Go to user settings.

Click or enter https://hackerone.com/settings/preferences.

> Page loads with preference options.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- settings
- preferences
