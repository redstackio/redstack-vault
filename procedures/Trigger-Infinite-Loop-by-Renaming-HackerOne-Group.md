---
id: proc-uuid-3
tags:
  - infinite-loop
  - dos
  - resource-exhaustion
  - hackerone
type: procedure
tools:
  - '[[tools/python-requests]]'
  - '[[tools/python-json]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/verify-hackerone-group-loop]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:39.658Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-Infinite-Loop-by-Renaming-HackerOne-Group

## Summary

This procedure renames a HackerOne group containing an API token member, triggering a near-infinite loop in the backend serialization, resulting in massive resource consumption and denial of service.

## Description

The vulnerability stems from improper handling in Ruby on Rails code during group updates when API tokens are members, causing iterative processing without an exit condition. This leads to hundreds of repeated JSON objects in database storage and API responses, consuming excessive CPU and memory, and potentially causing 500 errors. The exploit is triggered via the web UI but persists in API calls.

## Requirements

1. Group with API token member from prior steps
2. Access to group edit functionality
3. Python environment for verification (optional but recommended)

## Defense

Defensive measures and detection strategies:

- Add loop detection and bounds checking in group update handlers
- Monitor for large JSON payloads and repeated entries in logs
- Rate-limit group modifications and validate member types

## Objectives

1. Activate the loop to exhaust server resources
2. Demonstrate impact via oversized responses and errors
3. Validate persistence in database and API

## Instructions

### Step 1: Edit Group Name

**Context**: Change the group name to initiate the vulnerable update process.

Use the web UI in group management.

> Edit the group (e.g., from 'Testing' to 'AAABC2') and save. Observe browser response for initial repetition.

### Step 2: Verify Loop in API

**Context**: Use [[commands/verify-hackerone-group-loop]] to fetch and inspect program members, revealing the repeated groups.

Execute [[commands/verify-hackerone-group-loop]]:

```bash
python verify_hackerone_group_loop.py
```

> The script sends a GET to https://api.hackerone.com/v1/programs/44544 with Basic auth, parses members' groups, and prints them. Expected: Hundreds of repeated lines like {'id':95004,'key':null,'name':'AAABC2','team_members_count':0,'permissions':[],'immutable':false,'team_member_ids':[]}, confirming exhaustion.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/verify-hackerone-group-loop]]

## Tools Used

- [[tools/python-requests]]
- [[tools/python-json]]

## Tags

- infinite-loop
- dos
- resource-exhaustion
