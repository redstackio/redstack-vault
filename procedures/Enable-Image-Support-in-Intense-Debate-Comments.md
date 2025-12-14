---
id: proc-001
tags:
  - xss
  - configuration
  - web
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-13T23:52:44.518Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Enable-Image-Support-in-Intense-Debate-Comments

## Summary

This procedure configures the Intense Debate moderation panel to allow image tags in comments, which is a prerequisite for injecting img-based XSS payloads that bypass basic HTML restrictions.

## Description

The Intense Debate comment system requires explicit enabling of image support for img tags to be parsed and rendered. Without this, payloads may be stripped. This step involves accessing the admin interface to toggle the setting, setting up the environment for stored XSS exploitation. It assumes the attacker has moderator access or can social-engineer it. Expected outcome is that subsequent img tags in comments will load and execute attributes like onload.

## Requirements

1. Valid moderator account for the blog using Intense Debate
2. Access to the moderation panel URL (e.g., https://intensedebate.com/moderate/{{ID}})
3. Web browser for navigation

## Defense

Defensive measures and detection strategies:

- Disable image support in comment systems unless necessary
- Implement role-based access controls for moderation settings
- Monitor for unauthorized changes to comment configurations

## Objectives

1. Prepare the comment system for HTML injection
2. Ensure img tags are not filtered out
3. Enable execution of onload attributes

## Instructions

### Step 1: Access Moderation Panel

**Context**: Log in and navigate to the settings for comment features.

Navigate to https://intensedebate.com/moderate/{{ID}} and locate the comments section.

> Replace {{ID}} with the blog's Intense Debate ID. Look for options related to HTML or media embedding.

### Step 2: Enable Images

**Context**: Toggle the image allowance to permit img tags.

In the comments settings, check the box or select the option to "Allow images in comments" and save changes.

> Confirm the update via a success message or by testing a benign img tag in a comment.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[web]]
- [[configuration]]
