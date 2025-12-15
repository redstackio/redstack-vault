---
id: proc-trigger-deck-cache-001
tags:
  - nextcloud
  - deck
  - talk
  - cache-trigger
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:19.793Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-Deck-Card-Cache-via-Talk-Share

## Summary

This procedure triggers the caching of deck card reference data in Nextcloud's ReferenceManager by sharing a card link in a Talk conversation, exploiting the user-independent cache prefix to prepare for cross-user leakage.

## Description

In Nextcloud's Deck app, the CardReferenceProvider.php (lines 154-166) uses a cache prefix in ReferenceManager.php that does not incorporate user identity, leading to shared storage. An authorized user (User1) interacts with a deck card and shares its link in Talk, causing the server to cache the reference data. This data becomes accessible to any user who requests it with the correct boardId/cardId, enabling unauthorized access. The procedure assumes valid Nextcloud login and requires the Deck and Talk apps to be installed.

## Requirements

1. Valid Nextcloud user account with Deck access (User1)
2. Access to a Talk conversation
3. Knowledge of a specific deck board and card
4. Web browser for navigation

## Defense

Defensive measures and detection strategies:

- Implement user-specific cache keys in ReferenceManager
- Add access checks before serving cached references
- Monitor Talk shares for sensitive Deck links and log cache accesses

## Objectives

1. Cache deck card data server-side without isolation
2. Enable subsequent leakage to unauthorized users
3. Validate the vulnerability under minimal conditions

## Instructions

### Step 1: Log In and Navigate to Deck

**Context**: Authenticate as User1 and access the Deck app to select a target card.

Log in to Nextcloud at the server URL, then open the Deck app from the dashboard.

### Step 2: Generate and Share Card Link in Talk

**Context**: Create a shareable link for the card and post it in a Talk conversation to trigger caching.

1. Open a deck board, select a card.
2. Click the share icon to generate the card link (format: /apps/deck/#/board/{boardId}/card/{cardId}).
3. Navigate to the Talk app, open or create a conversation.
4. Paste and send the link.

This invokes ReferenceManager::getReference() which caches via APCu or similar with prefix 'deck_reference_' + boardId + '_' + cardId, independent of user ID.

**Expected Output**: Link shared successfully; no errors in UI. Server cache now holds card data.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- nextcloud
- deck
- cache
- share
