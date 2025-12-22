---
tags:
  - access
  - livechat
  - rocket-chat
type: procedure
tools:
  - '[[tools/Web-Inspector]]'
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
updated_at: '2025-12-14T03:46:25.835Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 1fd9dc1f-d4f0-47b4-b5b0-d8d340987925
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Rocket-Chat-Livechat-Instance

## Summary

This procedure establishes initial unauthenticated access to a Rocket.Chat instance with the Livechat feature enabled, setting the stage for subsequent JavaScript-based exploitation.

## Description

Rocket.Chat's Livechat allows anonymous visitor interactions. By simply loading the public instance, an attacker can access the visitor interface without credentials. This is a prerequisite for executing Meteor methods via browser console. The target environment is a web application built on Meteor.js, Node.js, and MongoDB, typically exposed on port 80/443.

## Requirements

1. Web browser (e.g., Chrome, Firefox) with developer tools.
2. Public URL of Rocket.Chat instance with Livechat enabled.
3. Internet connectivity.

## Defense

Defensive measures and detection strategies:

- Enable Livechat only for authenticated sessions if possible.
- Monitor for unusual visitor traffic patterns.
- Use WAF to block suspicious JavaScript executions.

## Objectives

1. Load the Livechat interface.
2. Verify feature availability.
3. Prepare console for injections.

## Instructions

### Step 1: Navigate to Instance

**Context**: Access the target Rocket.Chat URL to load the Livechat widget.

No command required; simply visit the URL like https://open.rocket.chat/ in your browser.

> The page should render the Livechat interface without requiring login.

### Step 2: Open Developer Tools

**Context**: Enable JavaScript execution environment.

Press F12 or right-click > Inspect to open Web Inspector, then switch to Console tab.

> Console should be interactive; test by typing `console.log('test')`.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Inspector]]

## Tags

- access
- livechat
- rocket-chat
