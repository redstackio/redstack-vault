---
id: proc-embed-url-basecamp
tags:
  - social-engineering
  - phishing
  - basecamp
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
  - '[[Malicious File]]'
updated_at: '2025-12-14T17:23:50.056Z'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Malicious File]]'
---
# Embed-Crafted-URL-in-Basecamp-Post

## Summary

This procedure involves inserting a crafted malicious URL into a Basecamp post or comment, optionally leveraging invitation emails for cross-account access, to entice victims to click within the desktop app.

## Description

By posting the URL http://launchpad.dev.mydomain.com/file.exe?attachment=true in Basecamp, the link appears as a legitimate attachment. Clicking 'respond in Basecamp' in ping emails can mimic invitation acceptance, adding victims to the attacker's account. This relies on the prior subdomain and server setup, targeting collaborative environments.

## Requirements

1. Active Basecamp account
2. Crafted URL from previous steps
3. Victim in contact via Basecamp or email

## Defense

Defensive measures and detection strategies:

- Sanitize and preview links in posts before rendering
- Warn users about external attachments in internal tools
- Audit account joins from email interactions

## Objectives

1. Deliver the malicious link to the victim
2. Facilitate cross-account access if needed
3. Prompt user interaction in the vulnerable app

## Instructions

### Step 1: Create Basecamp Post

**Context**: Embed the URL in a post to make it clickable.

Log into Basecamp, create a new post or comment, and insert: http://launchpad.dev.mydomain.com/file.exe?attachment=true.

> Style it as an image or attachment to increase click likelihood.

### Step 2: Optional Email Exploitation

**Context**: Use pings or invites to broaden reach.

Send a ping email with a 'respond in Basecamp' link; clicking adds the user to your account, exposing the post.

> Expected: Victim joins account unintentionally, sees the malicious post.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Malicious File]] User Execution: Malicious File

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[social-engineering]]
- [[Phishing]]
