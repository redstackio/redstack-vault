---
tags:
  - setup
  - web
type: procedure
tools: []
tactics: []
commands: []
platforms:
  - Web
techniques: []
sub_techniques: []
id: eb644bad-e649-4172-8ccc-b395d9f7be47
created_at: '2025-12-14T17:32:01.988Z'
updated_at: '2025-12-14T17:32:01.988Z'
verified: false
validated: true
submitted: true
---
# Initiate-New-API-Key

## Summary

This procedure starts the API key creation process within wallet settings, revealing the vulnerable name input field.

## Description

By pressing 'New key', the form for API key generation appears, including the unsanitized name field. This step is essential for targeting the XSS vulnerability in a web-based operator wallet system.

## Requirements

1. Wallet settings open
2. User permissions for key creation
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Rate-limit API key creations
- Audit key generation events

## Objectives

1. Display the key creation form
2. Expose the name input for manipulation
3. Set up for payload injection

## Instructions

### Step 1: Locate Button

**Context**: Identify the initiation control.

**Action**: Find and click the 'New key' button in the settings.

> The form modal or section opens with input fields.

### Step 2: Verify Form

**Context**: Confirm the vulnerable field is present.

**Action**: Inspect the form to see the name input with maxlength=30.

> Ensure the interface is ready for bypass.

## MITRE ATT&CK Mapping

### Tactics


### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[web]]
