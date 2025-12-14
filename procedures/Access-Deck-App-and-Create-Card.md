---
id: proc-access-deck-create-card
tags:
  - access
  - deck-app
  - nextcloud
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
updated_at: '2025-12-14T00:11:09.460Z'
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
# Access-Deck-App-and-Create-Card

## Summary

This procedure authenticates into the Nextcloud instance and navigates to the Deck app to create a card, setting the stage for comment-based HTML injection.

## Description

After local setup, log in via the web interface and access the Deck app. Create a new board and card to expose the comments feature, which lacks proper HTML sanitization. This step ensures the attacker can reach the vulnerable input point.

## Requirements

1. Running Nextcloud instance with Deck app enabled
2. Valid user credentials
3. Web browser for navigation

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls in Nextcloud
- Log all app accesses and card creations
- Use CSP headers to mitigate potential injections

## Objectives

1. Authenticate and gain session access
2. Navigate to and prepare Deck app resources
3. Open comments interface for exploitation

## Instructions

### Step 1: Authenticate with Credentials

**Context**: Log in to establish a user session.

Open http://localhost/nextcloud and enter username/password.

**Expected Output**: Redirect to dashboard.

### Step 2: Navigate to Deck App

**Context**: Access the vulnerable Deck feature.

Click the Deck icon in the app menu to open the interface.

**Expected Output**: Deck boards list loads.

### Step 3: Create Board and Card

**Context**: Prepare a target for comment injection.

Create a new board, add a stack, and create a card within it. Click the card to open details.

**Expected Output**: Card details view with comments section.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[access]]
- [[deck-app]]
- [[nextcloud]]
