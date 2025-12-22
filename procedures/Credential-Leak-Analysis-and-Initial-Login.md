---
tags:
  - information-disclosure
  - credential-leak
  - 2fa-bypass
type: procedure
tools:
  - '[[tools/Curl]]'
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/curl-trace-log]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:32:58.242Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 60ed6410-f03e-4d30-8dba-cd1c32426911
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Credential-Leak-Analysis-and-Initial-Login

## Summary

This procedure involves analyzing the leaked logger script and trace logs to extract credentials, followed by logging in and bypassing the initial 2FA using MD5 hash manipulation.

## Description

The exposed GitHub repo contains logger.php that base64-encodes credentials to bp_web_trace.log. Decoding reveals user creds and 2FA answers. Interception with Burp allows replacing the challenge_hash with the MD5 of the known answer for bypass.

## Requirements

1. Access to the leaked repo and log file
2. Burp Suite for request interception
3. Base64 decoder (e.g., online or openssl)

## Defense

- Avoid logging sensitive data; use secure logging practices
- Protect log files with authentication and encryption
- Implement proper 2FA with secure hashing (e.g., bcrypt) and rate limiting

## Objectives

1. Extract leaked credentials
2. Achieve initial user login
3. Bypass 2FA for session access

## Instructions

### Step 1: Analyze Logger Script

**Context**: Manually review logger.php from GitHub to understand log format.

No command; visit https://github.com/bounty-pay-code/request-logger/ and examine source.

> Logs requests as base64 JSON to bp_web_trace.log.

### Step 2: Download Trace Log

**Context**: Retrieve the log file containing encoded credentials.

**Command** ([[commands/curl-trace-log]]):
```bash
curl -sk https://app.bountypay.h1ctf.com/bp_web_trace.log
```

> Download and base64-decode to get brian.oliver:V7h0inzX and 2FA bD83Jk27dQ.

### Step 3: Login and 2FA Bypass

**Context**: Use creds to login; intercept 2FA request.

Use Burp Suite to replace challenge_hash with MD5( bD83Jk27dQ ) = 5828c689761cce705a1c84d9b1a1ed5e.

> Successful login to user dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-trace-log]]

## Tools Used

- [[tools/Curl]]
- [[tools/Burp-Suite]]

## Tags

- [[information-disclosure]]
- [[credential-leak]]
- [[2fa-bypass]]
