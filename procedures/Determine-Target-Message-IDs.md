---
tags:
  - id-enumeration
  - web
type: procedure
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-test-message-id]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:27:15.409Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: cff5840d-3690-4860-962c-173bd75429ca
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Determine Target Message IDs

## Summary

This procedure enumerates valid private message IDs on the Informatica community site by leveraging their sequential nature and testing deletions to identify recent, owned messages.

## Description

Message IDs are global and increment sequentially. The attacker sends a test message to themselves to capture a recent ID, then probes a range (e.g., last 50-100 IDs) to find valid ones. Invalid IDs cause failures, allowing refinement. This targets the victim's recent messages for deletion. Prerequisites: Site access and session. Expected outcome: List of probable victim message IDs.

## Requirements

1. Account on https://community.informatica.com
2. Ability to send/receive private messages
3. Session cookie for testing
4. Script or manual testing for range probing

## Defense

Defensive measures and detection strategies:

- Obfuscate or randomize message IDs
- Log and alert on rapid sequential deletion attempts
- Implement per-user ID namespaces
- Require POST for deletions with idempotency checks

## Objectives

1. Capture a baseline recent message ID
2. Probe and validate a range of IDs
3. Compile targets for batch deletion

## Instructions

### Step 1: Capture Baseline ID

**Context**: Send a test private message to obtain a current ID.

Log in, send message to self, inspect URL or response for messageID (e.g., 500).

**Expected Output**: Note max_id = 500.

### Step 2: Probe ID Range

**Context**: Test deletions in descending order from max_id to identify valid ones.

Execute [[commands/curl-test-message-id]] for each:

```bash
curl -X GET "https://community.informatica.com/pm-delete.jspa?messageID=450" -H "Cookie: JSESSIONID=session_cookie" -v
```

> Success (200/302) indicates valid ID; error (404/400) skips it. Collect successes.

### Step 3: Refine and List Targets

**Context**: Focus on recent interval (e.g., max_id - 50 to max_id).

Manually or script 50 tests; valid IDs are likely victim's.

**Expected Output**: Array of 10-20 valid IDs.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/curl-test-message-id]]

## Tools Used


## Tags

- [[id-enumeration]]
- [[web]]
