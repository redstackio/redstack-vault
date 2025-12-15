---
id: uuid-placeholder-4
tags:
  - request-capture
  - api
  - buddypress
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Sniffing]]'
updated_at: '2025-12-14T17:28:51.920Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Sniffing]]'
---
# Capture-Legitimate-Group-Member-Edit-Request

## Summary

This procedure intercepts a valid HTTP POST request for editing group member roles in BuddyPress using browser tools, providing a template for modification in the escalation attack.

## Description

Logged in as the moderator (B) in their private group 'def', attempt a self-edit action to trigger and capture the REST API request. This reveals the structure of legitimate calls to /wp-json/buddypress/v1/groups/[id]/members/[id], including authentication tokens. Used to bypass auth checks later. Requires dev tools access.

## Requirements

1. Moderator access to group 'def'
2. Browser with developer tools (e.g., Chrome DevTools)
3. Network tab enabled for request logging

## Defense

Defensive measures and detection strategies:

- Monitor for unusual API request patterns from moderators
- Enforce CSRF tokens on all member edit endpoints
- Log all REST API calls with user context

## Objectives

1. Obtain a working API request template
2. Identify key parameters like group_id and action
3. Ensure request includes valid auth

## Instructions

### Step 1: Open Developer Tools

**Context**: Prepare to monitor network traffic.

Log in as B, open browser dev tools (F12), go to Network tab, and filter for XHR/Fetch.

### Step 2: Trigger Member Edit

**Context**: Generate the legitimate request.

Navigate to /groups/def/admin/manage-members/, select self (B), and attempt to edit role (e.g., no change needed, just submit).

**Expected Output**: Captured POST request in dev tools, showing URL, method, headers, and body (e.g., action=edit&role=member).

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Network Sniffing]] Network Sniffing

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- request-capture
- api
- buddypress
