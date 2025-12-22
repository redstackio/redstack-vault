---
id: proc-share-malicious-post
tags:
  - phishing
  - social-engineering
type: procedure
tools:
  - '[[tools/Slack-Web-UI]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Desktop (Electron)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Phishing]]'
updated_at: '2025-12-14T17:24:15.159Z'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[T1566.001]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Share-Malicious-Slack-Post

## Summary

This procedure shares the HTML-injected Slack Post with a channel or user to entice clicking in the desktop app.

## Description

Sharing propagates the malicious post, relying on social engineering to get the target to interact with the large image in the Electron desktop client, triggering the redirect.

## Requirements

1. Edited post from previous injection.
2. Target channel or user access.
3. Slack web or desktop for sharing.

## Defense

Defensive measures and detection strategies:

- User training on suspicious posts/links.
- Scan shared content for malicious HTML.
- Alert on rapid post edits.

## Objectives

1. Distribute post to targets.
2. Entice click on injected image.
3. Initiate redirect chain.

## Instructions

### Step 1: Share Post

**Context**: Post the malicious content.

In Slack web UI, share the post to a channel or DM, e.g., "Check out this image!".

> Post appears with large clickable image.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Phishing]] Phishing

### Sub-Techniques

- [[T1566.001]] Spearphishing Attachment

## Commands Used


## Tools Used

- [[tools/Slack-Web-UI]]

## Tags

- phishing
- social-engineering
