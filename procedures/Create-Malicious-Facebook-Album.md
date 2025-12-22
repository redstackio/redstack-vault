---
tags:
  - xss
  - facebook
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:08.066Z'
sub_techniques: []
id: 7228d76c-69a1-48af-bd74-f7f7b411a7cd
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Facebook-Album

## Summary

This procedure involves creating a Facebook photo album with a malicious name containing an XSS payload, which serves as the storage mechanism for the cross-site scripting attack when later imported into Slack.

## Description

In the context of exploiting Slack's Facebook integration, the attacker creates an album on Facebook where the title includes unsanitized JavaScript, such as an img tag with an onerror handler. This payload is stored persistently and fetched without escaping when selecting albums in Slack's photo selector, leading to XSS execution in the victim's browser session.

## Requirements

1. Active Facebook account with permissions to create albums and upload photos
2. Web browser to access Facebook
3. Knowledge of basic XSS payloads

## Defense

Defensive measures and detection strategies:

- Sanitize all user-controlled inputs, including album names from third-party APIs
- Implement Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous JavaScript alerts or network requests from photo upload features

## Objectives

1. Store XSS payload in a selectable Facebook resource
2. Ensure the payload remains unescaped when fetched by integrated applications
3. Prepare for reflection in target application like Slack

## Instructions

### Step 1: Log In and Navigate to Photos

**Context**: Access Facebook's photo management to create a new album.

Log in to Facebook at https://www.facebook.com. Click on Photos in the left sidebar, then select Albums > Create Album.

### Step 2: Set Malicious Album Name

**Context**: Inject the XSS payload into the album title field.

Enter the album name as `'><img src=x onerror=alert(document.cookie)>`. This payload will break out of any HTML context and execute JavaScript on reflection.

### Step 3: Upload a Photo and Save

**Context**: Make the album valid and selectable by adding content.

Upload at least one photo to the album and click Create Album to save.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- facebook
- payload-injection
