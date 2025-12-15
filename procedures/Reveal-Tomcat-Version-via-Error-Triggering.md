---
id: proc-error-trigger-001
tags:
  - error-based-enum
  - stack-trace
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-login-attempt]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:24:15.244Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Reveal-Tomcat-Version-via-Error-Triggering

## Summary

Trigger backend errors through invalid inputs or paths to expose stack traces revealing server versions like Tomcat 5.5.20.

## Description

A failed login with 'admin' credentials led to a backend error and empty page, but URL manipulation exposed the Tomcat stack trace, enabling targeted CVE exploitation.

## Requirements

1. Access to login endpoint
2. Default or guessed credentials
3. Ability to tamper with URLs

## Defense

- Suppress detailed error messages in production
- Use custom error pages without stack traces
- Rate-limit login attempts

## Objectives

1. Expose server version info
2. Identify exploitable components
3. Guide vulnerability selection

## Instructions

### Step 1: Attempt Default Login

**Context**: Test admin credentials to potentially trigger errors.

**Command** ([[commands/curl-login-attempt]]):
```bash
curl -X POST http://www.example.starbucks.com.sg/josso/signin -d "username=admin&password=admin"
```

> Returns 'success' but empty page; credentials disabled post-attempt.

### Step 2: Manipulate URL for Stack Trace

**Context**: Append invalid paths to force exception.

**Command** ([[commands/curl-login-attempt]]):
```bash
curl http://www.example.starbucks.com.sg/josso/invalid-path
```

> Outputs Apache Tomcat 5.5.20 stack trace.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-login-attempt]]

## Tools Used

- None

## Tags

- [[error-based-enum]]
- [[stack-trace]]
