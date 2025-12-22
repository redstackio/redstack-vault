---
id: uuid-placeholder-2
tags:
  - cookie-injection
  - dnn
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-add-cookie]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:54.242Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Add DNNPersonalization Cookie to Request

## Summary

This procedure adds a custom DNNPersonalization cookie to HTTP requests targeting 404 pages, enabling subsequent payload delivery for deserialization exploitation.

## Description

The DNNPersonalization cookie is processed during 404 handling in vulnerable DNN apps. By including a base64-encoded or XML payload in this cookie, attackers can control deserialization input. This targets .NET-based web apps; outcomes include cookie acceptance and deserialization trigger.

## Requirements

1. HTTP client like curl
2. Knowledge of target URL
3. Placeholder payload ready

## Defense

Defensive measures and detection strategies:

- Validate and sign cookies
- Log anomalous cookie values
- Use WAF to block suspicious headers

## Objectives

1. Include custom cookie in request
2. Ensure server processes it
3. Avoid rejection or errors

## Instructions

### Step 1: Craft Basic Cookie Header

**Context**: Prepare the cookie with a placeholder value.

**Command** ([[commands/curl-add-cookie]]):
```bash
curl -v "https://target.com/nonexistent-page" -H "Cookie: DNNPersonalization=placeholder-base64"
```

> Sends request with cookie; check verbose output for acceptance.

### Step 2: Confirm Cookie Processing

**Context**: Verify no immediate blocks.

**Command** ([[commands/curl-add-cookie]]):
```bash
curl -I "https://target.com/nonexistent-page" -H "Cookie: DNNPersonalization=placeholder"
```

> Head request to check headers without full body.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-add-cookie]]

## Tools Used


## Tags

- cookie-injection
- dnn
