---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - web
  - initial-access
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
techniques: []
updated_at: '2025-12-14T05:32:10.063Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Create-Instacart-Store-List

## Summary

This procedure outlines the steps to create a new store list in the Instacart web application, providing access to the vulnerable background image upload feature.

## Description

In the context of exploiting the image upload path disclosure vulnerability, creating a store list is the initial step to reach the upload interface. This requires a standard user account and involves navigating the web UI to set up a list for stores, which then exposes the background customization options. The procedure assumes legitimate access and focuses on manual interaction without automation.

## Requirements

1. Valid Instacart user account with login credentials
2. Web browser with JavaScript enabled
3. Internet access to instacart.com

## Defense

Defensive measures and detection strategies:

- Monitor for unusual store list creation patterns from new or suspicious accounts
- Implement rate limiting on list creation endpoints

## Objectives

1. Gain access to the store list editing interface
2. Prepare for background image upload
3. Enable subsequent exploitation steps

## Instructions

### Step 1: Log In to Instacart

**Context**: Authenticate to access user-specific features.

Navigate to https://www.instacart.com and enter credentials to log in.

### Step 2: Navigate to Store Lists

**Context**: Locate the section for managing store lists.

From the dashboard, go to the 'Lists' or 'Shopping Lists' area and select 'Create New List' for stores.

### Step 3: Create and Save the List

**Context**: Finalize the list creation to unlock editing options.

Enter a name for the list (e.g., 'Test Store List') and save it.

**Expected Output**: Confirmation message and redirect to the list view.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web
- initial-access
