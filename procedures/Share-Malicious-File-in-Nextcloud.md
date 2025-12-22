---
id: proc-share-file-nextcloud
tags:
  - sharing
  - phishing
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.001]]'
updated_at: '2025-12-14T17:24:40.134Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
---
# Share-Malicious-File-in-Nextcloud

## Summary

This procedure uses Nextcloud's built-in sharing features to distribute a malicious HTML file to a target victim, increasing the likelihood of them opening it in the vulnerable iOS app.

## Description

After uploading the payload, the attacker leverages Nextcloud's sharing capabilities to create a public link or direct share with the victim's account. This can be disguised as a legitimate file to encourage opening. The share can be sent via email or integrated apps. Prerequisites: Uploaded file and knowledge of victim's Nextcloud username or email. Expected outcome: Victim receives access and interacts with the file.

## Requirements

1. Access to the uploaded malicious file in Nextcloud
2. Victim's Nextcloud account details or email for sharing
3. Permissions to create shares (default for most users)

## Defense

Defensive measures and detection strategies:

- Educate users on suspicious shares and verify file senders
- Log and alert on shares of executable file types like HTML
- Implement share approval workflows for sensitive files

## Objectives

1. Deliver the malicious file to the victim without direct suspicion
2. Ensure easy access via Nextcloud iOS app notification
3. Set up for payload execution upon opening

## Instructions

### Step 1: Initiate Sharing

**Context**: Select the file and configure sharing options.

In the Nextcloud interface, right-click or select the "malicious.html" file, choose "Share", and set it to public link or specific user. For public, generate a password-protected link if needed; for direct, enter victim's username.

> Expected output: Share link or invitation sent; confirmation in UI.

### Step 2: Distribute the Share

**Context**: Notify the victim to prompt interaction.

Copy the share link and send it via email or chat, e.g., "Please review this important document: [link]". If direct share, the victim gets an in-app notification.

> Expected output: Victim sees the file in their Nextcloud dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.001]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[sharing]]
- [[Phishing]]
- [[nextcloud]]
