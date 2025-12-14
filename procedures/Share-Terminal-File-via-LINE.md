---
id: proc-line-share-001
tags:
  - phishing
  - file-sharing
  - macos
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.001]]'
updated_at: '2025-12-14T17:26:29.934Z'
skill_level: low
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
---
# Share-Terminal-File-via-LINE

## Summary

This procedure uses LINE's sharing feature from Keep to deliver the uploaded .terminal file to a victim, bypassing restrictions on direct executable sharing and relying on social engineering for download.

## Description

Once uploaded to Keep, files can be shared via LINE chats without additional filtering, allowing the .terminal executable to reach the victim. The file downloads to ~/Downloads upon victim interaction. This step requires the victim to be a LINE contact and assumes trust in shared files.

## Requirements

1. Uploaded .terminal file in attacker's Keep
2. Victim as LINE contact
3. LINE Mac client for both parties

## Defense

Defensive measures and detection strategies:

- Educate users on risks of downloading shared files from chats
- Implement client-side scanning for executables in downloads
- Log and alert on frequent Keep-to-chat shares of suspicious files

## Objectives

1. Deliver .terminal to victim's device
2. Position file for later execution
3. Maintain stealth in delivery

## Instructions

### Step 1: Initiate Share from Keep

**Context**: Select and send the file via LINE chat.

In LINE, go to Keep, find the .terminal file, tap share, select the victim's chat, and send. The file appears as an attachment.

**Expected Output**: Message sent with file link.

### Step 2: Confirm Delivery

**Context**: Verify victim receives and can download.

Monitor chat for victim acknowledgment or download indicators in LINE.

**Expected Output**: File status shows downloaded.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1566.001]] Phishing: Spearphishing Attachment

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- phishing
- line-sharing
