---
tags:
  - http-request-smuggling
  - exploit
  - bypass
type: procedure
tools:
  - '[[tools/python3]]'
  - '[[tools/nc]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/python3-payload-nc]]'
platforms:
  - Web
  - Node.js
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: cb3c335a-46f9-4954-9ca0-07217be2e462
created_at: '2025-12-13T09:01:17.106Z'
updated_at: '2025-12-13T09:01:17.106Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute HTTP Request Smuggling Attack via Chunk Extension

## Summary

This procedure executes an HTTP Request Smuggling attack by injecting an invalid newline in a chunk extension to mismatch parsing between ATS and Node.js, bypassing proxy controls.

## Description

The attack crafts a chunked HTTP request with a newline in the extension, which Node.js ignores but ATS misparses, allowing a smuggled request to /admin. Impact includes bypassing access controls, though response retrieval is limited by an ATS bug.

## Requirements

1. ATS proxy on localhost:8080
2. payload.py script available
3. python3 and nc installed

## Defense

Defensive measures and detection strategies:

- Update to patched versions of Node.js and ATS
- Monitor for anomalous chunked requests with invalid characters

## Objectives

1. Smuggle request to restricted endpoint
2. Bypass proxy controls
3. Demonstrate vulnerability impact

## Instructions

### Step 1: Send Crafted Payload

**Context**: Generate payload and send via netcat to proxy.

**Command** ([[commands/python3-payload-nc]]):
```bash
python3 payload.py | nc localhost 8080
```

> This sends the smuggled request, expecting '/admin was reached!' in terminal.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/python3-payload-nc]]

## Tools Used

- [[tools/python3]]
- [[tools/nc]]

## Tags

- [[http-request-smuggling]]
- [[exploit]]
- [[bypass]]
