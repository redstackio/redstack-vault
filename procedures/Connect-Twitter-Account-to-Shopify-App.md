---
id: proc-uuid-002
name: Connect-Twitter-Account-to-Shopify-App
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:42.529Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - shopify
  - twitter
  - oauth
  - web
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Connect-Twitter-Account-to-Shopify-App

## Summary

This procedure authenticates and links a Twitter account to the installed Shopify Twitter app via OAuth, creating the session state vulnerable to CSRF-based disconnection.

## Description

Following app installation, this step uses the app's interface to initiate Twitter OAuth authentication. The user grants permissions, linking the accounts and enabling features like tweet posting from Shopify. Analysis of this flow reveals the disconnect endpoint lacks CSRF protection. Prerequisites: Installed app and Twitter credentials. Outcome: Active integration, confirmed in app settings.

## Requirements

1. Installed Twitter app in Shopify
2. Valid Twitter account credentials
3. Web browser for OAuth flow

## Defense

Defensive measures and detection strategies:

- Enforce OAuth scopes review before granting
- Log all OAuth connections for anomaly detection
- Use multi-factor authentication for app linkages

## Objectives

1. Establish authenticated Twitter integration with Shopify
2. Create session cookies exploitable in CSRF attacks
3. Verify linkage for disruption potential

## Instructions

### Step 1: Access App Settings

**Context**: Open the Twitter app within Shopify admin.

Navigate to Shopify admin > Apps > Twitter app.

### Step 2: Initiate Connection

**Context**: Start the OAuth process to link accounts.

Click 'Connect Twitter Account' and follow redirects to Twitter for authentication. Authorize permissions and complete the flow.

> Success is indicated by a confirmation message and updated status showing 'Connected'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[twitter]]
- [[oauth]]
- [[web]]
