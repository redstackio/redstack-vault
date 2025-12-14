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
id: 8083887e-def3-4ece-bc96-304bbfabde2e
created_at: '2025-12-14T17:32:01.990Z'
updated_at: '2025-12-14T17:32:01.990Z'
verified: false
validated: true
submitted: true
---
# Open-Wallet-Settings

## Summary

This procedure navigates to the settings page of the created operation wallet, exposing the API key management interface vulnerable to XSS.

## Description

Accessing wallet settings is a prerequisite for interacting with the API key creation form. In the attack scenario, this loads the page where client-side restrictions can be bypassed. The target environment is a web app, and success is indicated by the settings UI loading fully.

## Requirements

1. Existing operation wallet
2. Authenticated session
3. Browser with navigation capabilities

## Defense

Defensive measures and detection strategies:

- Implement session timeouts for sensitive pages
- Monitor access logs to wallet settings

## Objectives

1. Load the vulnerable API key interface
2. Prepare for key creation
3. Confirm settings accessibility

## Instructions

### Step 1: Select Wallet

**Context**: Choose the target wallet from the list.

**Action**: Click on the created wallet in the dashboard.

> This redirects to the wallet overview, with an option to open settings.

### Step 2: Access Settings

**Context**: Enter the configuration area.

**Action**: Click the settings or configure button for the wallet.

> The settings page loads, displaying API key options.

## MITRE ATT&CK Mapping

### Tactics


### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[web]]
