---
tags:
  - business-logic
  - json-tampering
  - web
  - payload-manipulation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:28.550Z'
sub_techniques: []
id: f55ef5cf-c633-45d8-8b2c-23a439916e6e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Tamper-and-Resubmit-Exam-JSON-Payload

## Summary

This procedure modifies the intercepted JSON exam submission payload to mark all answers as correct and resubmits it, exploiting the lack of server-side validation to pass the exam.

## Description

The Semrush Academy submission endpoint accepts a JSON body with an 'answers' object. By editing this client-side (e.g., in dev tools), attackers set all values to '1' for correct. The server trusts this without verification, leading to illegitimate passage. Prerequisites include an intercepted request from prior steps; outcomes include certificate issuance.

## Requirements

1. Intercepted submission request from retake
2. Ability to edit request payloads (dev tools or proxy)
3. Knowledge of question count to fully tamper

## Defense

Defensive measures and detection strategies:

- Add server-side logic to check answer integrity (e.g., hash or timestamp)
- Require client-side computation verifiable on server
- Detect payload size anomalies or perfect scores post-retake

## Objectives

1. Alter answers to all correct in JSON
2. Resubmit without triggering validation errors
3. Achieve exam passage and certificate

## Instructions

### Step 1: Intercept and Edit Payload

**Context**: Capture the submission request and modify the answers object.

In dev tools, pause the request on the submission POST. Edit the JSON body: change all empty values to '1', e.g., from {"answers": {"q1": "", "q2": ""}} to {"answers": {"q1": "1", "q2": "1"}}.

### Step 2: Resubmit Modified Request

**Context**: Forward the tampered request to the server.

Resume or replay the request. Monitor the response for success.

**Expected Output**: 200 OK response with passing status; certificate available.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[business-logic]]
- [[json-tampering]]
- [[web]]
- [[payload-manipulation]]
