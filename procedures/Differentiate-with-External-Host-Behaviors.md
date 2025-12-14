---
id: proc-differentiate-external
tags:
  - ssrf
  - validation
  - external-testing
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T04:39:02.174Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Differentiate-with-External-Host-Behaviors

## Summary

This procedure uses external hosts with unusual ports to compare SSRF behaviors and confirm the vulnerability's internal reach.

## Description

Submitting external URLs like `http://google.com:22/` results in timeouts for closed ports, differing from localhost's immediate errors. This differentiation proves the server is making requests on behalf of the attacker, validating SSRF without external dependencies.

## Requirements

1. Functional macro form
2. Reliable external hosts (e.g., google.com)
3. Observation of response timings and errors

## Defense

Defensive measures and detection strategies:

- Block non-standard ports in URL validation
- Rate-limit form submissions to prevent scanning
- Differentiate logging for internal vs. external requests

## Objectives

1. Validate SSRF through behavioral comparison
2. Rule out client-side issues
3. Refine understanding of error patterns

## Instructions

### Step 1: Select External Test

**Context**: Choose a known reachable host with closed port.

Use `http://google.com:22/` as it won't connect on port 22.

> External hosts ensure the difference isn't due to network isolation.

### Step 2: Compare Responses

**Context**: Submit and contrast with localhost tests.

Enter the URL, submit, and time the response. Expect longer timeouts for external closed ports vs. quick local errors.

> Success: Distinct outcomes confirm server-side execution for internals.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Vulnerability Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[validation]]
