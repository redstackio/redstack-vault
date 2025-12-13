---
tags:
  - http-request-smuggling
  - exploit-execution
type: procedure
tools:
  - '[[tools/Burp-Suite-Intruder]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
id: 3d0b3f31-de2f-4430-918e-94a4c66c60e3
created_at: '2025-12-13T09:01:17.703Z'
updated_at: '2025-12-13T09:01:17.703Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute Burp Intruder Attack

## Summary

This procedure executes the configured Burp Intruder attack to send smuggled HTTP requests, exploiting desync to alter headers and force redirects.

## Description

By running the Intruder attack, crafted requests are sent to the target, leveraging chunked encoding desync to smuggle a secondary request with a malicious Host header. This can lead to arbitrary redirects, bypassing security controls in vulnerable web setups like Acronis.

## Requirements

1. Pre-configured payload in Burp Intruder
2. Stable connection to target
3. Burp Suite running

## Defense

Defensive measures and detection strategies:

- Use WAF rules to block invalid Transfer-Encoding formats
- Log and alert on request smuggling patterns

## Objectives

1. Send smuggled requests successfully
2. Exploit server desync
3. Achieve header manipulation

## Instructions

### Step 1: Start Attack

**Context**: Initiate the attack from Burp Intruder interface.

> Click 'Start attack' to send requests.

### Step 2: Monitor Responses

**Context**: Observe server responses for signs of successful smuggling.

> Look for anomalies in response codes or content.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite-Intruder]]

## Tags

- [[http-request-smuggling]]
- [[exploit-execution]]
