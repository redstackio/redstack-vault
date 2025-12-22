---
tags:
  - sqli
  - time-based
  - blind
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:04.842Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 07f7c944-399a-494a-b14d-e74eab9184bf
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test Orange Cookie with Time-Based Payload

## Summary

This procedure confirms time-based blind SQL injection in the 'orange' cookie by injecting SLEEP functions into login requests to https://reviews.zomato.com, where response delays indicate successful query execution without visible errors.

## Description

Time-based blind SQLi exploits delays from functions like MySQL's SLEEP() to infer data when no output is returned. Here, setting 'orange' to a payload like '1'=sleep(10)='1' causes the server to pause if injected into a query, changing the expected quick 302 redirect to a delayed 200 response. This technique is stealthy, evading basic logging, and targets cookie processing in the login backend. Prerequisites: confirmed fuzzable cookie; outcomes: proof of injection with timing evidence.

## Requirements

1. Precise timing measurement (e.g., proxy with stopwatch)
2. Knowledge of target DBMS sleep functions (SLEEP for MySQL)
3. Multiple test iterations for reliability

## Defense

Defensive measures and detection strategies:

- Use prepared statements for all cookie-influenced queries
- Monitor for unusual response times on login endpoints
- Implement timeout thresholds and anomaly detection in WAF

## Objectives

1. Induce and measure server-side delays
2. Confirm blind injection without error messages
3. Validate payload execution in query context

## Instructions

### Step 1: Craft Time-Based Payload

**Context**: Build a payload that forces a delay only on injection success.

Use '1'=sleep(10)='1' for 'orange' cookie, ensuring it balances the query if injected.

**Expected Output**: Payload string ready for injection.

### Step 2: Submit and Time Response

**Context**: Intercept login request, set cookie, and measure full round-trip time.

Submit POST with modified 'orange', start timer on send, note delay before response.

**Expected Output**: ~10-second delay with HTTP 200 instead of 302.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- sqli
- time-based
- blind
