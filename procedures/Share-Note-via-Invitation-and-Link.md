---
tags:
  - phishing
  - shared-link
  - social-engineering
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.001]]'
updated_at: '2025-12-14T17:24:42.971Z'
skill_level: beginner
impact_level: low
detection_risk: medium
sub_techniques: []
id: 81d22512-3226-4178-b443-03cf4f5219a8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
---
# Share-Note-via-Invitation-and-Link

## Summary

This procedure shares the compromised Evernote note with the victim via invitation and generates a deeplink to enable remote access and trigger the exploit chain.

## Description

Evernote requires invitations for shared notes on Android. The attacker invites the victim by email and copies a shareable link (internal or web deeplink) that can be opened directly in the app. This facilitates the initial access vector without needing victim credentials.

## Requirements

1. Compromised note with renamed attachment
2. Victim's email address
3. Evernote account with sharing permissions

## Defense

Defensive measures and detection strategies:

- Warn users about unsolicited shared notes
- Implement link scanning for malicious deeplinks in email clients
- Rate-limit invitations from accounts to prevent abuse

## Objectives

1. Gain initial access to victim's app instance
2. Deliver deeplink for seamless note opening
3. Minimize friction for victim's first interaction

## Instructions

### Step 1: Invite Victim

**Context**: Send access invitation to pull victim into the shared note.

In the note, tap share > invite collaborator > enter victim's email and send.

### Step 2: Generate Shareable Link

**Context**: Create a clickable deeplink for the note.

Tap three dots in the note > Copy internal link or Copy web link (for Android deeplink).

> Copy the link to clipboard for distribution via email or other channels.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1566.001]] Spearphishing Attachment

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- sharing
- deeplink
- android
