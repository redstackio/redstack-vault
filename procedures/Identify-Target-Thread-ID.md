---
id: proc-002
tags:
  - enumeration
  - idor
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:30:27.368Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Identify-Target-Thread-ID

## Summary

This procedure enumerates private message thread IDs in BuddyPress to identify targets where the authenticated user is not a participant, enabling IDOR exploitation.

## Description

BuddyPress uses incremental thread_ids for private messages. By querying the database (if accessible) or guessing sequentially, attackers can find unauthorized threads. This targets the bp_messages_message_to table or similar; prerequisites include authentication. Expected outcomes: A list of thread_ids for injection testing.

## Requirements

1. Authenticated session from WordPress login
2. Database access (optional, via SQL injection or admin) or knowledge of ID patterns
3. Ability to create test threads between other users

## Defense

Defensive measures and detection strategies:

- Implement proper authorization checks on thread access
- Rate-limit ID enumeration attempts and log anomalous queries

## Objectives

1. Discover unauthorized thread_ids
2. Confirm non-participation to validate IDOR
3. Prepare for reply injection

## Instructions

### Step 1: Create Test Thread

**Context**: Generate a thread between non-attacker users to observe ID assignment.

Use BuddyPress UI to send a message between two test accounts.

> Expected output: New thread_id visible in URL or database (e.g., /messages/view/5/).

### Step 2: Enumerate IDs

**Context**: Guess or query sequential IDs starting from 1.

If DB access: SELECT id FROM wp_bp_messages_threads WHERE... (filter out user's threads).

> Explanation: Incremental IDs make brute-force feasible; skip owned threads.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- enumeration
- idor
