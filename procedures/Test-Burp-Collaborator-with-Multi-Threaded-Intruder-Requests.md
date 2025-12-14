---
tags:
  - burp-suite
  - intruder
  - collaborator
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Desktop
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Disable or Modify Tools]]'
updated_at: '2025-12-14T17:24:22.461Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 93deed9c-b39c-48bc-abb6-15a8bf5cbed0
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Disable or Modify Tools]]'
---
# Test-Burp-Collaborator-with-Multi-Threaded-Intruder-Requests

## Summary

This procedure uses Burp Suite's Intruder tool to send 100 concurrent threads of requests to a Burp Collaborator server, revealing anomalous response processing indicative of client-side issues in extensions like JSBeautifier.

## Description

In a pentesting setup, configure Burp as a proxy and use Intruder to flood the Collaborator OOB server with simultaneous requests. This simulates high-load conditions, triggering differences in responses due to asynchronous processing without synchronization, particularly for JS content. The target environment is a local Burp installation proxying browser traffic, with no server modifications needed. Expected outcomes include subtle response variations every few requests, pointing to buffer handling flaws.

## Requirements

1. Burp Suite Professional with Collaborator enabled
2. Network access to Collaborator server (e.g., via Burp's built-in)
3. Proxy configuration in browser or tools

## Defense

Defensive measures and detection strategies:

- Disable unnecessary BApps like JSBeautifier in production use
- Monitor Burp logs for async processing errors or high thread counts
- Use synchronized queuing in custom extensions to prevent races

## Objectives

1. Detect client-side anomalies in response handling
2. Isolate issues to Burp processing
3. Gather initial evidence for further reproduction

## Instructions

### Step 1: Configure Intruder Attack

**Context**: Set up a multi-threaded payload attack targeting the Collaborator server to simulate concurrent requests.

**Command** (Burp GUI Configuration):
```bash
# In Burp: Target > Site map > Right-click Collaborator payload > Send to Intruder > Positions: Add § to request body > Payloads: Simple list (e.g., unique payloads) > Options: Thread count = 100 > Start attack
```

> This launches 100 threads sending requests; observe the Results table for response bodies differing slightly (e.g., missing chars or altered JS).

### Step 2: Analyze Responses

**Context**: Inspect the Intruder results for patterns of inconsistency.

**Command** (Burp Inspection):
```bash
# No CLI; use Burp's Response viewer to compare raw vs. rendered responses across threads
```

> Look for anomalies like incomplete beautification or timing delays; note occurrences every 5-10 requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Disable or Modify Tools]] Impair Defenses: Disable or Modify Tools

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- burp-suite
- intruder
- testing
