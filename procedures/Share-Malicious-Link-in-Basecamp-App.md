---
tags:
  - phishing
  - in-app-sharing
  - social-engineering
type: procedure
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:26:27.182Z'
skill_level: low
impact_level: low
detection_risk: high
sub_techniques: []
id: 6e72334f-dfe9-45f3-8754-a92a2abe35a7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Share Malicious Link in Basecamp App

## Summary

This procedure distributes the crafted malicious deeplink within Basecamp's collaboration features to entice victims into clicking and triggering the exploit.

## Description

Leveraging Basecamp's project comments, messages, or descriptions, the attacker posts the deeplink disguised as a legitimate reference (e.g., 'Check this progress report'). When rendered, the link becomes clickable, invoking the app's deeplink handler upon tap. This step relies on social trust within the app's ecosystem and requires authenticated access to the target project.

## Requirements

1. Authenticated Basecamp account with write access to project
2. Malicious URL from prior crafting step
3. Victim in the same project or shared space

## Defense

Defensive measures and detection strategies:

- Implement URL scanning in Basecamp for suspicious patterns (e.g., excessive '../')
- Educate users on verifying links in collaboration tools
- Enable preview-only mode for external links without auto-handling

## Objectives

1. Place link in visible, clickable context
2. Target specific victims via project permissions
3. Avoid detection by content filters

## Instructions

### Step 1: Select Sharing Context

**Context**: Choose an in-app feature supporting hyperlinks.

Use comments or project updates to embed the URL.

> Expected: Link appears as hyperlinked text.

### Step 2: Post and Notify

**Context**: Share to notify victim without raising suspicion.

Add URL with innocuous text like 'Updated progress: [link]' and @mention victim.

> Expected: Victim receives notification and views the post.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.002]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[in-app-sharing]]
- [[social-engineering]]
