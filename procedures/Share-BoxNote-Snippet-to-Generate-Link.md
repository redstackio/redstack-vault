---
id: proc-slack-boxnote-share-001
tags:
  - sharing
  - link-generation
  - xss
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
updated_at: '2025-12-14T03:16:37.483Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Share-BoxNote-Snippet-to-Generate-Link

## Summary

This procedure uploads the malicious BoxNote to Slack's file storage and generates a shareable link, allowing distribution to team members for subsequent exploitation.

## Description

Once the payload is injected, the BoxNote must be persisted on files.slack.com via upload or sharing. This creates a URL that any team member can access, setting up the stored XSS for execution. The process leverages Slack's file sharing mechanics, which do not re-sanitize content during link generation, enabling persistence across the team.

## Requirements

1. Saved BoxNote with injected payload
2. Slack workspace access for file upload
3. Ability to generate and share links within the team

## Defense

Defensive measures and detection strategies:

- Scan uploaded files for malicious patterns before storage
- Limit file sharing to verified users
- Log and alert on unusual file uploads containing script-like content

## Objectives

1. Persist the malicious snippet on files.slack.com
2. Obtain a team-accessible URL
3. Enable easy distribution without alerting defenses

## Instructions

### Step 1: Upload the BoxNote

**Context**: Use Slack's interface to upload the created BoxNote as a file.

In the Slack channel, drag-and-drop or use the file upload feature to submit the BoxNote snippet.

### Step 2: Generate Shareable Link

**Context**: Once uploaded, copy the generated URL for the file.

The upload results in a URL like `https://files.slack.com/files-pri/T027N7MK3-F1NCA92JF/XSS______script___img_src___img_src_search__onerror_alert__Xss__________marquee__boxnote.boxnote`. Right-click the file preview and select 'Copy link'.

### Step 3: Distribute the Link

**Context**: Share the link with target team members to lure them into accessing it.

Post the link in a channel or direct message, encouraging viewing of the 'raw' content.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[sharing]]
- [[xss]]
