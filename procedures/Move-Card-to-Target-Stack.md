---
tags:
  - nextcloud
  - deck
  - card-move
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/put-move-deck-card-own]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:19.817Z'
sub_techniques: []
id: bb3ab0f0-d3a9-4fc9-8a5b-922c3d432639
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Move-Card-to-Target-Stack

## Summary

This procedure demonstrates a legitimate move of a Deck card to another stack, capturing the PUT request structure for later modification in the exploitation chain.

## Description

Using the PUT /apps/deck/cards/{id} endpoint, update the card's stackId and metadata. This is a normal operation but sets up the interceptable request. Prerequisites include the card ID from creation. Outcome: Card relocated within own decks, request logged for tampering.

## Requirements

1. Card ID from prior creation step
2. Own stack IDs (e.g., 2 for target within own deck)
3. Timestamp for lastModified (use current Unix time)

## Defense

Defensive measures and detection strategies:

- Validate stack ownership in PUT handlers
- Audit logs for stackId changes across users

## Objectives

1. Relocate card legitimately
2. Capture request for interception
3. Prepare for unauthorized modification

## Instructions

### Step 1: Prepare Metadata

**Context**: Gather card details including timestamps and owner.

### Step 2: Execute Move

**Context**: Send PUT to move card to own stack 2.

**Command** ([[commands/put-move-deck-card-own]]):
```bash
curl -X PUT 'https://nextcloud.example.com/apps/deck/cards/13' \
  -H 'Content-Type: application/json' \
  -H 'OCS-APIRequest: true' \
  -H 'Cookie: nc_username=attacker; nc_token=session_token' \
  -d '{"title":"SOME_TEST","description":"","stackId":2,"type":"plain","lastModified":1588755341,"lastEditor":null,"createdAt":1588755341,"labels":null,"assignedUsers":null,"attachments":null,"attachmentCount":null,"owner":"attacker","order":999,"archived":false,"duedate":null,"deletedAt":0,"commentsUnread":0,"id":13,"overdue":0}'
```

> Updates stackId to 2. Expected: 200 OK.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/put-move-deck-card-own]]

## Tools Used


## Tags

- nextcloud
- deck
- api-move
