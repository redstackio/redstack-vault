---
id: a81833df-0d5f-4da7-a774-49723955fe24
name: Identify-Vulnerable-User-Agent-Header
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:09.861Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - sqli
  - identification
  - headers
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Identify-Vulnerable-User-Agent-Header

## Summary

This procedure manually identifies the User-Agent HTTP header as a SQL injection vector by injecting test payloads and observing application behavior in a SharePoint-based web app.

## Description

Targeting applications that concatenate User-Agent strings into SQL queries without sanitization, this procedure uses a proxy to modify headers and detect susceptibility through response anomalies. It follows automated scanning and focuses on manual verification for precision in blind scenarios with MySQL backends.

## Requirements

1. Proxy tool like Burp Suite for request interception
2. Access to send custom HTTP requests to the target
3. Knowledge of basic SQL syntax for payloads

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all HTTP headers before database interaction
- Log and alert on non-standard User-Agent strings containing SQL keywords
- Employ input whitelisting for expected User-Agent formats

## Objectives

1. Confirm User-Agent as injectable parameter
2. Isolate the vulnerability location
3. Prepare for confirmation payloads

## Instructions

### Step 1: Intercept and Modify Request

**Context**: Use Burp Suite to capture a legitimate request and alter the User-Agent header with a test payload.

Set User-Agent to: 'Mozilla/5.0 (test; SQL' and forward the request.

> Observe for database errors, delays, or unexpected responses indicating SQL parsing.

### Step 2: Iterate Payloads

**Context**: Test variations to confirm header inclusion in queries.

Try payloads like 'AND 1=1' appended to a standard User-Agent.

> Differential behavior confirms vulnerability without full automation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[sqli]]
- [[identification]]
- [[headers]]
