---
tags:
  - vulnerability-confirmation
  - response-analysis
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Node.js
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 311a6488-9660-4c57-b143-bade141373c8
created_at: '2025-12-13T09:01:17.189Z'
updated_at: '2025-12-13T09:01:17.189Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe Server Response for Smuggling Confirmation

## Summary

This procedure involves monitoring the server response to confirm that the HTTP Request Smuggling payload was processed as multiple requests, verifying the vulnerability.

## Description

After sending the payload, check the server output or logs to see if it handled the request as a POST and a separate GET, rather than rejecting it as invalid due to malformed headers.

## Requirements

1. Running Node.js server with logging enabled
2. Access to server console or response stream
3. Prior execution of payload sending step

## Defense

Defensive measures and detection strategies:

- Log and alert on anomalous request parsing
- Use WAF rules to detect smuggling attempts

## Objectives

1. Confirm exploitation success
2. Validate impact of request splitting
3. Document vulnerability reproduction

## Instructions

### Step 1: Monitor Server Output

**Context**: Check the server's response or logs for evidence of request smuggling.

> Observe if the server processes and responds to two requests: the initial POST and the smuggled GET /flag, instead of a single invalid request.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[vulnerability-confirmation]]
- [[response-analysis]]
