---
id: proc-uuid-1
name: Install Shopify Chat App
tags:
  - setup
  - shopify
  - chat-app
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
updated_at: '2025-12-13T23:55:38.353Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install Shopify Chat App

## Summary

This procedure sets up the Shopify Chat application on a target store, enabling the vulnerable chat functionality required for subsequent XSS exploitation.

## Description

The Shopify Chat app allows real-time messaging on store homepages or via Shopify Ping. Installing it exposes the unsanitized input handling that leads to stored XSS. This step requires standard Shopify admin access and is a prerequisite for injecting payloads. Expected outcome: Chat interface active, allowing message storage and display.

## Requirements

1. Valid Shopify admin account with app installation permissions
2. Access to the Shopify app store
3. Target store configured for app integrations

## Defense

Defensive measures and detection strategies:

- Restrict app installations to trusted admins only
- Monitor app installation logs for unusual activity
- Use Shopify's app review processes to validate integrations

## Objectives

1. Activate chat functionality on the store
2. Prepare environment for payload injection
3. Ensure chat messages are stored server-side

## Instructions

### Step 1: Access Shopify Admin

**Context**: Log in to the Shopify admin dashboard to begin app installation.

Navigate to the admin panel at `https://admin.shopify.com` and authenticate with admin credentials.

### Step 2: Install Chat App

**Context**: Search and install the official Shopify Chat app to enable messaging.

In the Apps section, search for "Chat" and select the official app. Click "Add app" and follow prompts to install on the target store.

**Expected Output**: Confirmation message: "Chat app installed successfully." Chat widget appears on the store frontend.

### Step 3: Verify Installation

**Context**: Test the chat interface to confirm functionality.

Visit the store homepage or open Shopify Ping, and check for the chat input box. Send a test message to ensure storage and display.

**Expected Output**: Test message appears in chat history.

**Success Indicators**:
- Chat widget loads without errors
- Messages are sent and received

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[shopify]]
- [[chat-app]]
