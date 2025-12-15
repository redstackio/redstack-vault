---
id: proc-twitter-dm-override-001
tags:
  - twitter
  - android
  - dm-settings
  - privacy-violation
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Disable or Modify Tools]]'
updated_at: '2025-12-14T17:24:42.549Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Disable or Modify Tools]]'
---
# Override-Protection-by-Changing-DM-Settings-in-Android-App

## Summary

This procedure exploits a synchronization issue in the Twitter Android app by changing Direct Messages settings, which unexpectedly disables the 'Protect your Tweets' setting previously enabled via web, exposing private content publicly without notification.

## Description

The vulnerability stems from the app overriding external privacy settings during internal DM configuration changes, likely due to a flag reset or sync bug. Target environment: Twitter Android app (Java/Kotlin-based). Prerequisites: Protected tweets active, app logged in. Expected outcome: Tweets become public, enabling privacy violations or social engineering to trick users into this change.

## Requirements

1. Twitter Android app installed and updated
2. Account logged in with protected tweets enabled via web
3. Android device with internet connectivity

## Defense

Defensive measures and detection strategies:

- Change all settings via web interface only; avoid app for privacy toggles
- After any app setting change, immediately verify tweet protection status on web
- Use Twitter's API or third-party tools to monitor account privacy changes
- Report app bugs via Twitter support or HackerOne

## Objectives

1. Impair tweet privacy defenses through app interaction
2. Expose protected content to public view
3. Demonstrate potential for social engineering attacks

## Instructions

### Step 1: Access Direct Messages in App

**Context**: Navigate to the DM section to reach settings.

Open the Twitter Android app, ensure logged in, and tap the envelope icon for Direct Messages.

> DM inbox loads; no errors in navigation.

### Step 2: Open DM Settings

**Context**: Access the gear icon to modify options that trigger the override.

In the DM tab, tap the gear icon in the top right to open settings.

> Settings menu appears with options like 'Receive message requests' and 'Show read receipts'.

### Step 3: Toggle a DM Setting

**Context**: Change a setting to invoke the sync that unsets protection.

Select and toggle 'Receive message requests' from off to on (or vice versa), or 'Show read receipts'. Save or confirm the change.

> Setting updates without warning about tweet protection; app may briefly sync.

### Step 4: Observe No Notification

**Context**: Confirm the override happens silently.

Note the absence of any alert regarding tweet visibility; the app returns to DM view.

> No pop-up or log indicating protection change.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Disable or Modify Tools]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[privacy-violation]]
- [[android]]
