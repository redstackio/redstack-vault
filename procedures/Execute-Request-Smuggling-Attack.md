---
tags:
  - exploit
  - http
  - smuggling
type: procedure
tools:
  - '[[tools/cat]]'
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/cat-pipe-to-curl]]'
platforms:
  - Web
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 905f77b8-ce8d-4450-b554-8d98299502a3
created_at: '2025-12-13T09:01:22.358Z'
updated_at: '2025-12-13T09:01:22.358Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute Request Smuggling Attack

## Summary

This procedure sends the crafted payload to the vulnerable Tomcat server to perform HTTP request smuggling.

## Description

By piping the malicious payload file to curl using the telnet protocol, raw HTTP data is sent to the server. The vulnerability causes Tomcat to process the oversized trailer incorrectly, smuggling an additional request. This can lead to security bypasses in production setups.

## Requirements

1. Crafted attack5.txt file
2. Running Tomcat container on localhost:8082
3. Curl installed

## Defense

Defensive measures and detection strategies:

- Patch Tomcat to versions that fix the parsing issue
- Monitor for multiple responses to single requests
- Implement proxy-level request validation

## Objectives

1. Deliver the payload to the server
2. Observe request smuggling effects
3. Validate exploitation success

## Instructions

### Step 1: Send Payload

**Context**: Transmit the crafted request to exploit the vulnerability.

**Command** ([[commands/cat-pipe-to-curl]]):
```bash
cat attack5.txt | curl telnet://localhost:8082/ --output -
```

> Sends raw data via curl, outputting the response.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/cat-pipe-to-curl]]

## Tools Used

- [[tools/cat]]
- [[tools/curl]]

## Tags

- [[exploit]]
- [[http]]
- [[smuggling]]
