---
tags:
  - nextcloud
  - deck
  - card-creation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/post-create-deck-card]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:19.822Z'
sub_techniques: []
id: 1f96bcd8-bba2-4d54-89de-c7409e65e932
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Card-in-Own-Deck

## Summary

This procedure creates a new task (card) in the attacker's own Deck stack in Nextcloud, providing a card ID for subsequent manipulation in access control exploitation.

## Description

In the context of exploiting CVE-2020-8179, this step establishes a benign task that can be moved via API. The Nextcloud Deck app uses a POST to /apps/deck/cards endpoint, requiring authentication. No special permissions are needed beyond basic user access. Expected outcome: A new card with an assignable ID appears in the user's deck.

## Requirements

1. Authenticated session to Nextcloud (valid username and session token)
2. Knowledge of own stack ID (e.g., via Deck UI, typically starts at 1)
3. Access to HTTP client like curl or Burp Suite

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on card creation APIs
- Log all card creations with user and stack details for anomaly detection

## Objectives

1. Generate a test card for injection
2. Obtain card ID for API manipulation
3. Ensure card is in attacker's control initially

## Instructions

### Step 1: Authenticate and Prepare Request

**Context**: Log in to Nextcloud and identify your stack ID via the Deck app interface.

**Command** ([[commands/post-create-deck-card]]):
```bash
curl -X POST 'https://nextcloud.example.com/apps/deck/cards' \
  -H 'Content-Type: application/json' \
  -H 'OCS-APIRequest: true' \
  -H 'Cookie: nc_username=attacker; nc_token=session_token' \
  -d '{"title":"SOME_TEST","stackId":1,"type":"plain"}'
```

> This sends a POST request to create a plain card in stack 1. Expected output: JSON with {"id":13, "title":"SOME_TEST"}.

### Step 2: Verify Creation

**Context**: Check the Deck UI or query the card to confirm ID.

**Command** (GET /apps/deck/cards/{id}):
```bash
curl -X GET 'https://nextcloud.example.com/apps/deck/cards/13' \
  -H 'OCS-APIRequest: true' \
  -H 'Cookie: nc_username=attacker; nc_token=session_token'
```

> Confirms the card exists in the specified stack.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/post-create-deck-card]]

## Tools Used


## Tags

- nextcloud
- deck
- api-creation
