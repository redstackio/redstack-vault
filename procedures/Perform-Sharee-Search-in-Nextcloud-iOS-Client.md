---
id: proc-nextcloud-ios-search-001
tags:
  - ios
  - nextcloud
  - client-flaw
  - privacy-leak
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Automated Collection]]'
updated_at: '2025-12-14T17:24:39.963Z'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Automated Collection]]'
---
# Perform-Sharee-Search-in-Nextcloud-iOS-Client

## Summary

This procedure simulates a user action in the Nextcloud iOS app to trigger a sharee search, highlighting the client's failure to include the 'lookup' parameter, which defaults to global querying on the server.

## Description

The iOS Nextcloud client, when used for file sharing, sends requests to the server's sharee search endpoint without the 'lookup' parameter. This omission causes the server to interpret it as true, initiating external queries. Unlike web and desktop clients, the iOS app does not prompt for global search consent, leading to privacy issues in default setups.

## Requirements

1. iOS device with Nextcloud app installed and logged into the target server
2. A file in Nextcloud to share
3. Network connectivity to the server

## Defense

Defensive measures and detection strategies:

- Update to fixed iOS client versions that include the 'lookup' parameter
- Educate users on disabling global search server-side
- Proxy iOS traffic to detect missing parameters in API calls

## Objectives

1. Initiate a sharee search without global intent
2. Trigger server-side default behavior
3. Observe lack of consent prompt

## Instructions

### Step 1: Navigate to File Sharing

**Context**: Access the sharing feature in the app.

Open the Nextcloud iOS app, select a file or folder, and tap the share icon to enter the sharee search interface.

> Expected: Share dialog opens without additional prompts.

### Step 2: Enter Search Term

**Context**: Perform the search that omits the parameter.

Type a search term (e.g., a username) in the search field and submit. The app constructs a request to /ocs/v2.php/apps/files_sharing/api/v1/sharees without 'lookup=false'.

> Expected: Search results load, but underlying request is vulnerable.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Automated Collection]] Automated Collection

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[ios]]
- [[nextcloud]]
- [[client-flaw]]
- [[privacy-leak]]
