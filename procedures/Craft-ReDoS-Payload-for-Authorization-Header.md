---
id: proc-redos-payload-craft
tags:
  - redos
  - payload
  - http-header
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:31:19.605Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Craft ReDoS Payload for Authorization Header

## Summary

This procedure crafts a malicious string for the HTTP Authorization header to exploit the ReDoS vulnerability in WEBrick's DigestAuth, using repeated backslash-b patterns to trigger catastrophic backtracking.

## Description

In the attack scenario, the payload targets the vulnerable regex by creating a long sequence that maximizes backtracking attempts. The target environment is any HTTP client capable of sending custom headers. Expected outcomes include a string that causes the server to hang for seconds due to CPU exhaustion during parsing.

## Requirements

1. Understanding of the vulnerable regex pattern
2. Text editor for payload construction
3. Optional: Regex testing tool like regex101.com

## Defense

Defensive measures and detection strategies:

- Validate and sanitize Authorization headers for length and patterns before processing
- Use non-backtracking regex engines or rewrite patterns to avoid nested quantifiers
- Log and alert on unusually long auth headers

## Objectives

1. Generate a backtracking-inducing string
2. Ensure compatibility with Digest auth format
3. Test payload length for optimal impact

## Instructions

### Step 1: Design Payload Structure

**Context**: Base the payload on Digest auth format but inject repeating \b.

Start with 'Authorization: Digest ' followed by a parameter like a="...".

### Step 2: Build Repeating Pattern

**Context**: Create a long string of \b to exploit the (.|\[^"])* quantifier.

Construct: a="\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b". Adjust length (e.g., 30+ \b) for increased delay.

> This payload causes the regex engine to explore exponential paths, consuming 100% CPU.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- redos
- payload
