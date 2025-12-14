---
tags:
  - csrf
  - payload
  - plugin
  - web
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:36.188Z'
sub_techniques: []
id: 7c152442-3dfc-4015-9a0b-c362fc844afb
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute CSRF Payload to Create Plugin

## Summary

Send a forged POST request with JSON payload to the plugins endpoint, creating an unauthorized plugin on the victim's account.

## Description

The payload targets the vulnerable endpoint, which accepts JSON without CSRF checks. Success leads to account modification, potentially allowing further abuse via the created plugin.

## Requirements

1. Active victim session
2. Full attack chain setup
3. Payload details (email, name, webUrl)

## Defense

Defensive measures and detection strategies:

- Add CSRF tokens to all state-changing endpoints
- Validate Origin/Referer headers
- Audit plugin creation logs

## Objectives

1. Submit malicious JSON payload
2. Confirm plugin creation
3. Achieve unauthorized modification

## Instructions

### Step 1: Prepare Payload

**Context**: Define JSON for plugin creation.

Payload: {"email":"attacker@example.com","name":"csrf poc","webUrl":"csrf poc "}

> Integrate into Flash request.

### Step 2: Monitor Execution

**Context**: Observe request in DevTools.

Direct victim to malicious page; open Network tab.

Use [[tools/Browser-Developer-Tools]] to watch POST to endpoint.

> Expected: 200 OK, plugin created.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[csrf]]
- [[payload]]
