---
id: p2b3c4d5-e6f7-8901-bcde-f2345678901
tags:
  - oauth
  - app-creation
  - web
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:36.254Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Create-OAuth-Application

## Summary

This procedure creates a new OAuth application on Tumblr to facilitate testing of API connections, setting the stage for cookie injection and DoS verification.

## Description

Within the attack scenario, creating an OAuth app involves navigating to the apps dashboard and submitting a form with basic app details. The target is the Tumblr OAuth management interface, and the procedure assumes an authenticated session. Prerequisites include login without existing OAuth cookies. Expected outcomes: A new app is registered, enabling subsequent 'Explore API' interactions that trigger the vulnerable endpoint.

## Requirements

1. Active Tumblr session.
2. Access to https://www.tumblr.com/oauth/apps.
3. Arbitrary app name and description.

## Defense

Defensive measures and detection strategies:

- Rate-limit app creation attempts.
- Log and alert on rapid app registrations.
- Require verification for new apps.

## Objectives

1. Register a test OAuth application.
2. Ensure no pre-existing cookies block the attack.
3. Enable API exploration for vulnerability trigger.

## Instructions

### Step 1: Navigate to OAuth Apps

**Context**: Access the application management page.

Use browser to go to https://www.tumblr.com/oauth/apps.

> Page loads with option to create new app.

### Step 2: Submit App Creation Form

**Context**: Fill and submit the creation form.

Enter a random app name (e.g., 'TestApp'), description, and submit.

> App appears in the list upon success.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- oauth
- app-creation
- web

