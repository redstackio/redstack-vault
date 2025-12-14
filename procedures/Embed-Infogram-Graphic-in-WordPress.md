---
tags:
  - embed
  - wordpress
  - infogram
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:14.243Z'
sub_techniques: []
id: 45b1a9eb-6932-448a-a452-d26af3eb4140
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Embed Infogram Graphic in WordPress

## Summary

This procedure embeds the malicious Infogram project into a WordPress post using the plugin's interface, causing the unsanitized project name to be fetched and stored in the site content.

## Description

In the WordPress editor, the 'Add from Infogram' button opens a popup that queries Infogram for projects. Selecting the malicious project pulls the name into the display without escaping, storing the XSS payload. This targets authenticated WordPress users with plugin access. Outcomes include the graphic inserted, ready for triggering on view or interaction.

## Requirements

1. Active WordPress admin session
2. Installed Infogram plugin 1.5.1
3. Malicious project ID from Infogram

## Defense

Defensive measures and detection strategies:

- Validate and escape external API responses in plugins
- Audit embedded content for malicious scripts
- Disable or sandbox third-party embeds in content management systems

## Objectives

1. Integrate malicious external content into WordPress
2. Trigger fetch of unsanitized project metadata
3. Store payload for later execution in user context

## Instructions

### Step 1: Access WordPress Editor

**Context**: Prepare a post for embedding.

Log in to WordPress admin and create or edit a post/page in the editor.

### Step 2: Use Embed Button

**Context**: Select and insert the malicious graphic.

Click the 'Add from Infogram' button in the editor toolbar. In the popup, log in to Infogram if prompted, search for the malicious project, and select it to embed. Confirm insertion into the post content.

> The project name is now reflected in the popup HTML without sanitization.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- embed
- wordpress
- infogram
