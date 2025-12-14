---
tags:
  - sqli
  - fuzzing
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:04.844Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: b1dde196-2ff4-437e-9e4e-1cc677199e42
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Fuzz Cookies for SQL Injection Vulnerabilities

## Summary

This procedure tests cookie parameters for SQL injection by injecting payloads into 'orange' and 'squeeze' cookies during login requests to https://reviews.zomato.com, observing for errors, delays, or behavioral changes that indicate unsanitized query processing.

## Description

Fuzzing involves systematically replacing cookie values with SQL metacharacters, keywords, and payloads to probe for injection points. In this case, targeting the Zomato login, fuzzing reveals vulnerabilities when responses deviate from baseline (e.g., errors on quotes or unions). This is a black-box technique relying on response analysis, suitable for web apps with cookie-backed queries. Prerequisites include prior cookie observation; outcomes confirm if cookies influence SQL execution.

## Requirements

1. Interception proxy for request modification
2. List of SQL fuzz payloads (e.g., ', ", OR 1=1, etc.)
3. Timing tool to measure response durations

## Defense

Defensive measures and detection strategies:

- Parameterize all database queries involving cookies
- Validate and sanitize cookie inputs server-side
- Rate-limit login requests to detect fuzzing patterns

## Objectives

1. Identify injectable cookies
2. Classify vulnerability type (e.g., error-based, blind)
3. Gather evidence for deeper exploitation

## Instructions

### Step 1: Prepare Fuzzing Payloads

**Context**: Compile a set of common SQL injection test strings.

Create payloads like '1', "' OR '1'='1", "1'--", and inject into 'orange' and 'squeeze' separately.

**Expected Output**: List of 10-20 payloads ready for testing.

### Step 2: Inject and Observe Responses

**Context**: Modify cookies in intercepted requests and submit to login endpoint.

Replace cookie values one at a time, send POST, and note status, time, and body differences from baseline.

**Expected Output**: Anomalies like 500 errors on quotes or unexpected delays.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- sqli
- fuzzing
- web
