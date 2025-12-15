---
id: proc-access-leaked-card-001
tags:
  - nextcloud
  - deck
  - data-leak
  - access-bypass
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
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:29:19.766Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---
# Access-Leaked-Card-Data-with-Known-IDs

## Summary

This procedure exploits the shared cache in Nextcloud's ReferenceManager to retrieve unauthorized deck card information using known boardId and cardId, bypassing access controls due to lack of user isolation.

## Description

After caching is triggered, an unauthorized user (User2) can request the reference data via the Talk conversation or direct URL with boardId/cardId. The ReferenceManager serves the cached data from Deck's CardReferenceProvider without verifying User2's permissions on the deck, leading to information disclosure. This affects card details like title, description, and attachments. Exploitation requires prior knowledge of IDs, often from shared links, and the risk is minimal without them.

## Requirements

1. Valid Nextcloud user account without Deck permissions (User2)
2. Access to the Talk conversation or direct knowledge of boardId/cardId
3. Cached data from prior trigger (e.g., User1's share)
4. Web browser for accessing references

## Defense

Defensive measures and detection strategies:

- Enforce user-specific caching with UID in keys
- Implement permission checks in ReferenceManager::resolveReference()
- Audit cache accesses and correlate with user sessions
- Disable or restrict Deck-Talk integrations for sensitive boards

## Objectives

1. Retrieve deck card data without direct access rights
2. Demonstrate cross-user data leakage
3. Confirm vulnerability impact under specific conditions

## Instructions

### Step 1: Log In as Unauthorized User

**Context**: Authenticate as User2, who lacks permissions on the target deck.

Log in to Nextcloud at the server URL.

### Step 2: Request Cached Reference

**Context**: Access the Talk conversation or construct a reference request using known IDs to pull leaked data.

1. Open the Talk app and navigate to the conversation with the shared link.
2. Click the shared Deck card link (or manually construct: /apps/deck/#/board/{boardId}/card/{cardId}).
3. If direct access, use the browser to load the reference endpoint, triggering ReferenceManager to fetch from cache.

The cache hit returns User1's card data without authorization checks in CardReferenceProvider::resolve().

**Expected Output**: Card details visible to User2, including sensitive info not permitted by their role.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Information Repositories]] Data from Information Repositories

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- nextcloud
- deck
- leakage
- unauthorized-access
